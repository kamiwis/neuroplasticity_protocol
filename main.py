"""Time Management Timer App

This application is for timing your work/learning intervals.

It utilizes the following imported modules: `tkinter` """
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
canvas.pack()




window.mainloop()
