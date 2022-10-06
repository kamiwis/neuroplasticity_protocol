from tkinter import *
import math
import chime

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 0.2
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
CHECKMARK = "✓"

class TimerInterface():
    """
    A class used to represent the GUI for the Neuroplasticity Timer.
    ...

    Attributes
    __________
    reps: number of repetitions of learning completed.
    timer: the time the timer is set to for each work/break rep.
    marks: checkmark string denoting how many reps have been completed.

    Methods
    _______
    start_timer()
        Sets time for number of minutes depending on the rep.
    countdown(self, count)
        Takes a time as the argument and countsdown from that time to 0.
    reset_timer(self)
        Resets timer once four reps have been done.
    """
    def __init__(self):
        self.reps = 0
        self.timer = None
        self.marks = ""
        # Create window.
        self.window = Tk()
        self.window.title("Neuroplasticity Timer")
        # Configure window by adding padding to provide more space around image.
        self.window.config(padx=100, pady=50, bg=YELLOW)

        # Create canvas for window.
        self.canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
        # Create PhotoImage in order to use image on canvas.
        tomato_image = PhotoImage(file="tomato.png")
        # Adds tomoato image to canvas and displays it on the window.
        self.canvas.create_image(100, 112, image=tomato_image)
        self.timer_text = self.canvas.create_text(100, 135, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
        self.canvas.grid(column=1, row=1)

        # Create labels for timer and checkmarks.
        self.timer_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50, "bold"))
        self.timer_label.grid(column=1, row=0)
        self.checkmark = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 40, "bold"))
        self.checkmark.grid(column=1, row=3)

        # Create buttons for Start and Reset.
        self.start = Button(text="Start", highlightbackground=YELLOW, fg=GREEN, command=self.start_timer)
        self.start.grid(column=0, row=2)
        self.reset = Button(text="Reset", highlightbackground=YELLOW, fg=GREEN, command=self.reset_timer)
        self.reset.grid(column=2, row=2)

        self.window.mainloop()
    
    def start_timer(self):
        """Sets time for number of minutes depending on the rep."""
        self.reps += 1
        work_sec = WORK_MIN * 60
        short_break_sec = SHORT_BREAK_MIN * 60
        long_break_sec = LONG_BREAK_MIN * 60
        if self.reps == 8:
            self.timer_label.config(text="Break", fg=RED)
            self.countdown(long_break_sec)
        if self.reps % 2 == 0:
            self.timer_label.config(text="Break", fg=RED)
            self.countdown(short_break_sec)
        else:
            self.timer_label.config(text="Work")
            self.countdown(work_sec)
        
    def countdown(self, count):
        """Takes a time as the argument and countsdown from that time to 0."""
        count_min = math.floor(count / 60)
        count_sec = count % 60
        if count_min % 2 == 0 and count_sec == 5:
            chime.theme("big-sur")
            chime.success()
        if count_sec == 0:
            count_sec = "00"
        if count < 10:
            count_sec = f"0{count_sec}"
        self.canvas.itemconfig(self.timer_text, text=f"{count_min}:{count_sec}")
        if count > 0:
            self.timer = self.window.after(1000, self.countdown, count - 1)
        if count == 0:
            self.start_timer()
            num_work_sessions = self.reps // 2
            self.marks = ""
            for _ in range(num_work_sessions):
                self.marks += CHECKMARK
            self.checkmark.config(text=f"{self.marks}")
    
    def reset_timer(self):
        """Resets timer once four reps have been done."""
        # Cancel timer
        self.window.after_cancel(self.timer)
        # Set timer_text back to 00:00
        self.canvas.itemconfig(self.timer_text, text="00:00")
        # Set timer_label back to Timer
        self.timer_label.config(text="Timer", fg=GREEN)
        # Reset marks to empyty string and change checkmarks
        self.checkmark.config(text="")
        self.reps = 0
    