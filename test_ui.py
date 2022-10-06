from random import randint
from tkinter import *
import math
import chime
from timer_text import prompt_text

BACKGROUND_COLOR = "#6e8ee5"
TITLE_COLOR = "#05132d"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Arial"
WORK_MIN = 1
REST_SEC = 11
SHORT_BREAK_MIN = 1
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
        self.total_reps = 0
        self.num_work_sessions = 0
        self.status = None
        self.timer = None
        self.marks = ""
        self.rest_times = [randint(1,9), randint(1,9), randint(1,9), randint(1,9)]
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
        self.timer_text = self.canvas.create_text(250, 150, width=480, text=prompt_text, fill=TITLE_COLOR, font=(FONT_NAME, 25, "bold"))
        self.canvas.grid(column=0, row=1, columnspan=3)

        # self.prompt = Label(text=prompt_text, fg=TITLE_COLOR, bg=BACKGROUND_COLOR, font=(FONT_NAME, 20, "bold"))
        # self.prompt.grid(row=1, column=0, columnspan=2)

        self.entry = Entry(width=10)
        self.entry.insert(0, string="1")
        self.canvas.create_window(250, 220, window=self.entry)

        self.checkmark = Label(fg="black", bg=BACKGROUND_COLOR, font=(FONT_NAME, 20, "bold"))
        self.checkmark.grid(column=1, row=2)

        #Create buttons for Start and Reset.
        start_img = PhotoImage(file="images/start.png")
        self.true_button = Button(image=start_img, highlightthickness=0, command=self.start_timer)
        self.true_button.grid(row=2, column=0)

        reset_img = PhotoImage(file="images/reset.png")
        self.true_button = Button(image=reset_img, highlightthickness=0, command=self.reset_timer)
        self.true_button.grid(row=2, column=2)

        self.window.mainloop()
    
    def start_timer(self):
        """Sets time for number of minutes depending on the rep."""
        # Set the reps remaining to the user's input * 2.
        if self.total_reps == 0:
            self.reps_left = int(self.entry.get()) * 2
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
        if count_min % 2 == 0 and count_sec == 5:
            chime.theme("big-sur")
            chime.success()
        # Reformat countdown when at 0 seconds.
        if count_sec == 0:
            count_sec = "00"
        # Reformat countdown when less than 10 seconds.
        if count < 10:
            count_sec = f"0{count_sec}"
        self.canvas.itemconfig(self.timer_text, text=f"{count_min}:{count_sec}", font=(FONT_NAME, 45, "bold"))
        # Sound chime when time for random rest.
        # if self.status == "work":
        #     if count_min == 2 and count_sec == f"0{self.rest_times[0]}":
        #         self.rest_chime()
        #         if count_min == 1 and count_sec == 60 + (self.rest_times[0] - REST_SEC):
        #             self.rest_chime()
        #     if count_min == 4 and count_sec == f"0{self.rest_times[1]}":
        #         self.rest_chime()
        #         if count_min == 3 and count_sec == 60 + (self.rest_times[1] - REST_SEC):
        #             self.rest_chime()
        #     if count_min == 6 and count_sec == self.rest_times[2]:
        #         self.rest_chime()
        #         if count_min == 5 and count_sec == 60 + (self.rest_times[2] - REST_SEC):
        #             self.rest_chime()
        #     if count_min == 8 and count_sec == self.rest_times[3]:
        #         self.rest_chime()
        #         if count_min == 7 and count_sec == 60 + (self.rest_times[3] - REST_SEC):
        #             self.rest_chime()
        # Countdown timer.
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
        #self.canvas.itemconfig(self.timer_text, text="00:00")
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
