from tkinter import *


def clicked():
    print("Button got Clicked.")
    text = input.get()
    label.config(text=text)


window = Tk()
window.title("GUI Project")
window.minsize(width=500, height=500)
window.config(padx=100, pady=100)

label = Label(text="This is a Label", font=("Impact", 24))
# label.pack()
# label.place(x=110, y=0)
label.grid(column=0, row=0)

button_1 = Button(text="Click Me", font=("Impact", 12), command=clicked)
button_1.grid(column=1, row=1)
button_1.config(padx=10, pady=10, background="yellow")


button_2 = Button(text="Click Me", font=("Impact", 12))
button_2.grid(column=2, row=0)
button_2.config(padx=10, pady=10, background="yellow")


input = Entry(background="grey", width=10)
input.grid(column=3, row=2)
input.focus()
print(input.get())

window.mainloop()
