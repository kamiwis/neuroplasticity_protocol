from random import randint
from tkinter import Tk, Canvas, Label, Entry, PhotoImage, Button
import math
import chime

BACKGROUND_COLOR = "#6e8ee5"
TITLE_COLOR = "#05132d"
RED = "#e7305b"
FONT_NAME = "Arial"
WORK_MIN = 4
SHORT_BREAK_MIN = 1
CHECKMARK = "✓"
PROMPT = "How many 10 minute repetitions would you like to do? (Max=9)"

class TimerInterface():
    """
    A class used to represent the GUI for the Neuroplasticity Timer.
    ...

    Attributes:
        reps (int): number of repetitions of learning completed.
        total_reps (int): number of total repetitions needed based on user input.
        marks (str): checkmark string denoting how many reps have been completed.
        status (str): status of current timer mode - None, "work", or "break".

    Methods
        start_timer(self)
            Sets time for number of minutes depending on the rep.
        countdown(self, count)
            Takes a time as the argument and countsdown from that time to 0.
        reset_timer(self)
            Resets timer once four reps have been done.
        rest_chime(self):
            Generates chime to indicate rest time.
    """

    def __init__(self):
        """The constructor of the TimerInterface class."""
        self.reps = 0
        self.total_reps = 0
        self.status = None
        self.marks = ""
        self.timer = None
        # Create window.
        self.window = Tk()
        self.window.title("Neuroplasticity Timer")
        # Configure window by adding padding to provide more space around image.
        self.window.config(padx=20, pady=20, bg=BACKGROUND_COLOR)

        # Create labels for timer.
        self.timer_label = Label(text="Neuroplasticity Timer", fg=TITLE_COLOR, bg=BACKGROUND_COLOR, font=(FONT_NAME, 50, "bold"))
        self.timer_label.grid(column=0, row=0, columnspan=3)

        # Create canvas for window.
        self.canvas = Canvas(width=500, height=300, bg=BACKGROUND_COLOR, highlightthickness=0)
        # # Adds tomoato image to canvas and displays it on the window.
        self.timer_text = self.canvas.create_text(250, 150, width=480, text=PROMPT, fill=TITLE_COLOR, font=(FONT_NAME, 25, "bold"))
        self.canvas.grid(column=0, row=1, columnspan=3)

        # self.prompt = Label(text=prompt_text, fg=TITLE_COLOR, bg=BACKGROUND_COLOR, font=(FONT_NAME, 20, "bold"))
        # self.prompt.grid(row=1, column=0, columnspan=2)

        self.entry = Entry(width=10)
        self.entry.insert(0, string="1")
        self.canvas.create_window(250, 220, window=self.entry)

        self.checkmark = Label(fg="black", bg=BACKGROUND_COLOR, font=(FONT_NAME, 20, "bold"))
        self.checkmark.grid(column=1, row=2)

        #Create buttons for Start and Reset.
        start_img = PhotoImage(file="button_images/start.png")
        self.true_button = Button(image=start_img, highlightthickness=0, command=self.start_timer)
        self.true_button.grid(row=2, column=0)

        reset_img = PhotoImage(file="button_images/reset.png")
        self.true_button = Button(image=reset_img, highlightthickness=0, command=self.reset_timer)
        self.true_button.grid(row=2, column=2)

        self.window.mainloop()

    def start_timer(self):
        """Sets time for number of minutes depending on the rep."""
        # Set the reps remaining to the user's input * 2.
        if self.total_reps == 0:
            self.total_reps = int(self.entry.get()) * 2
        self.reps += 1
        work_sec = WORK_MIN * 60
        break_sec = SHORT_BREAK_MIN * 60
        # If there are no reps remaining, timer is finished.
        if self.reps > self.total_reps:
            self.timer_label.config(text="DONE!", fg=RED)
            self.status = None
            # self.countdown(long_break_sec)
        # If the number of reps is even, set work timer.
        if self.reps % 2 == 0:
            self.status = "break"
            self.timer_label.config(text="Break", fg=RED)
            self.countdown(break_sec)
        else:
            self.status = "work"
            self.timer_label.config(text="Work", fg=RED)
            self.countdown(work_sec)

    def countdown(self, count):
        """Takes a time as the argument and countsdown from that time to 0."""
        count_min = math.floor(count / 60)
        count_sec = count % 60
        if count_sec == 0:
            count_sec = "00"
        # Reformat countdown when less than 10 seconds.
        if count < 10:
            count_sec = f"0{count_sec}"
        if self.status == "work" and count_min % 2 == 0 and count_sec == "05":
            chime.theme("big-sur")
            chime.success()
        self.canvas.itemconfig(self.timer_text, text=f"{count_min}:{count_sec}", font=(FONT_NAME, 45, "bold"))
        # Countdown timer.
        if count > 0:
            self.timer = self.window.after(1000, self.countdown, count - 1)
        if count == 0:
            self.start_timer()
            self.marks = ""
            for _ in range(self.reps // 2):
                self.marks += CHECKMARK
            self.checkmark.config(text=f"{self.marks}")

    def reset_timer(self):
        """Resets timer once four reps have been done."""
        # Cancel timer
        self.window.after_cancel(self.timer)
        # Set timer_text back to 00:00
        self.canvas.itemconfig(self.timer_text, text="Neuroplasticity Timer", font=(FONT_NAME, 50, "bold"))
        # Set timer_label back to Timer
        self.timer_label.config(text="Neuroplasticity Timer", fg="white")
        # Reset marks to empyty string and change checkmarks
        self.checkmark.config(text="")
        self.reps = 0
        self.total_reps = 0
        self.status = None

    def rest_chime(self):
        """Generates chime to indicate rest time."""
        chime.theme("big-sur")
        chime.success()
