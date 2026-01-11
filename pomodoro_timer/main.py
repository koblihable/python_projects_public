import tkinter as tk
from tkinter import PhotoImage
import math

# ---------------------------- CONSTANTS ------------------------------- #
DARK_GREEN = "#0A400C"
GREEN = "#819067"
YELLOW = "#B1AB86"
FONT_NAME = "Courier"
WORK_MIN = 10
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 10
CHECK_MARK = "✓"
reps = 0
check_text = ""
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    global reps
    global timer

    reps = 0

    window.after_cancel(timer)
    timer_label.config(text="Timer")
    canvas.itemconfig(timer_text, text="0:00")
    check_label.config(text="")


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1
    work_min =  WORK_MIN #* 60
    short_break = SHORT_BREAK_MIN #* 60
    long_break = LONG_BREAK_MIN #* 60

    if reps % 8 == 0:
        count_down(long_break)
        timer_label.config(text="Break")

    elif reps % 2 == 0:
        count_down(short_break)
        timer_label.config(text="Break")
    else:
        count_down(work_min)
        timer_label.config(text="Work")

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    global reps
    global check_text

    count_mins = math.floor(count / 60)
    count_secs = count % 60
    if count_secs < 10:
        count_secs = f"0{count_secs}"

    canvas.itemconfig(timer_text, text=f"{count_mins}:{count_secs}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        session_no = math.floor(reps/2)
        for i in range(session_no):
            check_text += CHECK_MARK
            check_label.config(text=check_text)

# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

timer_label = tk.Label(text="Timer", font=("FONT_NAME", 40), fg=GREEN, bg=YELLOW)
timer_label.grid(column=2, row=1)

start_button = tk.Button(text="Start", bg=YELLOW, highlightthickness=0, command=start_timer)
start_button.grid(column=1, row=3)

reset_button = tk.Button(text="Reset", bg=YELLOW, highlightthickness=0, command=reset_timer)
reset_button.grid(column=3, row=3)

check_label = tk.Label(text="", fg=DARK_GREEN, bg=YELLOW)
check_label.grid(column=2,row=4)

canvas = tk.Canvas(width=201, height= 224, bg=YELLOW, highlightthickness=0)
image = PhotoImage(file="tomato.png")
canvas.create_image(101, 112, image=image)
timer_text = canvas.create_text(101, 130, text="0:00", fill="white", font=(FONT_NAME, 35, "bold"))

canvas.grid(column=2, row=2)







window.mainloop()