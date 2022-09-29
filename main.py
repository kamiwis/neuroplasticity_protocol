"""Time Management Timer App

This application is for timing your work/learning intervals.

It utilizes the following imported modules: `tkinter` and 'time' """
from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #
# Create window.
window = Tk()
window.title("Pomodoro")
# Configure window by adding padding to provide more space around image.
window.config(padx=100, pady=50, bg=YELLOW)

# Create canvas for window.
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
# Create PhotoImage in order to use image on canvas.
tomato_image = PhotoImage(file="tomato.png")
# Adds tomoato image to canvas and displays it on the window.
canvas.create_image(100, 112, image=tomato_image)
canvas.create_text(100, 135, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

# Create labels for timer and checkmarks.
timer_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50, "bold"))
timer_label.grid(column=1, row=0)
checkmark = Label(text="✓", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 40, "bold"))
checkmark.grid(column=1, row=3)

# Create buttons for Start and Reset.
start = Button(text="Start", highlightbackground=YELLOW, fg=GREEN)
start.grid(column=0, row=2)
reset = Button(text="Reset", highlightbackground=YELLOW, fg=GREEN)
reset.grid(column=2, row=2)




window.mainloop()
