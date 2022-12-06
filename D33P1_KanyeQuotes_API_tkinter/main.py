from tkinter import *
import requests


def next_quote():
    response = requests.get(url="https://api.kanye.rest")
    res= response.json()['quote']
    if len(res) > 70:
        canvas.itemconfig(quote_text, text=res, font=("Ariel", 10, "bold"))
    elif len(res) > 150:
        canvas.itemconfig(quote_text, text=res, font=("Ariel", 5, "bold"))
    else:
        canvas.itemconfig(quote_text, text=res, font=("Arial", 15, "bold"))


bg = "#FF4A4A"

window = Tk()
window.title("Kanye Says....")
window.config(padx=50, pady=50, bg=bg)

canvas = Canvas(width=300, height=414, bg=bg, highlightthickness=0)
canvas.grid(column=0, row=0)

bg_img = PhotoImage(file="background.png")
canvas.create_image(150, 212, image=bg_img)

quote_text = canvas.create_text(150, 212, text="Kanye quotes here", fill="#000000", font=("Impact", 10))


kanye_img = PhotoImage(file="kanye.png")
next_button = Button(width=100, height=131, image=kanye_img, bg=bg, command=next_quote)
next_button.grid(column=0, row=1)
window.mainloop()
