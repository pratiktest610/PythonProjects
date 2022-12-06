import pandas
from tkinter import *
import random
import time
bg = "#B1DDC6"
score = ""
# -------------------- Working on CSV -------------------- #
try:
    data = pandas.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    data = pandas.read_csv("./data/french_words.csv")

data_dict = {row.French: row.English for (index, row) in data.iterrows()}
key = random.choice(list(data_dict.keys()))
# -------------------- Brain -------------------- #


def test(i):
    timer_label.config(text=i)
    timer = window.after(1000, test, i - 1)
    if i == 0:
        window.after_cancel(timer)
        canvas.itemconfig(lang_text, text="ENGLISH")
        canvas.itemconfig(card_img, image=front_img)
        canvas.itemconfig(word_text, text=data_dict[key])


def reset():
    global key
    key = random.choice(list(data_dict.keys()))
    canvas.itemconfig(lang_text, text="FRENCH")
    canvas.itemconfig(card_img, image=back_img)
    canvas.itemconfig(word_text, text=key)
    test(5)


def correct():
    global score
    del data_dict[key]
    score += "✅"
    score_label.config(text=score)
    reset()


def wrong():
    global score
    score += "❎"
    score_label.config(text=score)
    reset()

# -------------------- UI SETUP -------------------- #
window = Tk()
window.title("Flash Card")
window.config(bg=bg, pady=50, padx=50)

canvas = Canvas(width=800, height=526, highlightthickness=0, bg=bg)
canvas.grid(row=0, column=0, columnspan=3)

back_img = PhotoImage(file="./images/card_back.png")
front_img = PhotoImage(file="./images/card_front.png")
card_img = canvas.create_image(400, 263, image=back_img)

lang_text = canvas.create_text(400, 75, text="FRENCH", fill="#002B5B", font=("Algerian", 36))
word_text = canvas.create_text(400, 263, text=key, fill="#002B5B", font=("Algerian", 72))

wrong_image = PhotoImage(file="./images/wrong.png")
wrong_button = Button(image=wrong_image, width=100, height=100, bg=bg, command=wrong)
wrong_button.grid(row=1, column=0)

right_image = PhotoImage(file="./images/right.png")
right_button = Button(image=right_image, width=100, height=100, bg=bg, command=correct)
right_button.grid(row=1, column=2)

timer_label = Label(text=0, font=("Algerian", 50), bg=bg, fg="#002B5B")
timer_label.grid(column=1, row=1)

score_label = Label(text="", font=("Algerian", 25), bg=bg, fg="#002B5B")
score_label.grid(row=2, column=0, columnspan=3)

test(3)

window.mainloop()

key_list = list(data_dict.keys())
value_list = list(data_dict.values())

new_data_dict = {
    "French": key_list,
    "English": value_list
}

df = pandas.DataFrame(new_data_dict)
df.to_csv("./data/words_to_learn.csv")