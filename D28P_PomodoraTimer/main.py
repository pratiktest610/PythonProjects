from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#5BB318"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
checkmark = ""
timer = None
#9bdeac
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text=f"00:00")
    global checkmark
    checkmark = ""
    checkmark_label.config(text=checkmark)
    timer_label.config(text="Timer", fg=GREEN)


# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    global reps
    reps += 1
    if reps in range(1, 8, 2):
        countdown(WORK_MIN * 60)
        timer_label.config(text="Work")
    if reps in range(2, 7, 2):
        countdown(SHORT_BREAK_MIN * 60)
        timer_label.config(text="Break", fg=PINK)
    if reps == 8:
        countdown(LONG_BREAK_MIN * 60)
        timer_label.config(text="Break", fg=RED)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 


def countdown(count):
    count_min = int(count / 60)
    count_sec = count % 60

    if count_sec < 10:
        count_sec = f"0{count_sec}"

    if count_min < 10:
        count_min = f"0{count_min}"

    if count >= 0:
        canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
        global timer
        timer = window.after(1000, countdown, count - 1)
    else:
        start_timer()
        global checkmark
        if reps % 2 == 0:
            checkmark += "✔"
            checkmark_label.config(text=checkmark)

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Pomodoro")
window.config(bg=YELLOW, pady=100, padx=100)

tomato_img = PhotoImage(file="tomato.png")

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill=YELLOW, font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

timer_label = Label(text="TIMER", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 35, "bold"),)
timer_label.grid(column=1, row=0)

start_button = Button(text="start", fg=GREEN, bg=RED, font=(FONT_NAME, 16, "bold"), highlightcolor=GREEN, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="reset", fg=GREEN, bg=RED, font=(FONT_NAME, 16, "bold"), highlightcolor=GREEN,  command=reset_timer)
reset_button.grid(column=2, row=2)

checkmark_label = Label(fg=RED, bg=YELLOW, font=(FONT_NAME, 16, "bold"))
checkmark_label.grid(column=1, row=3)

window.mainloop()
