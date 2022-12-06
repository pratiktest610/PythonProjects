from tkinter import *


def calculate():
    m = int(miles_in.get())
    km = round(m*1.609, 2)
    km_out.config(text=km)


window = Tk()
window.title("Miles To Kilometers Converter")
window.minsize(width=300, height=300)
window.config(padx=100, pady=100)

miles = Label(text="Miles", font=("Impact", 12))
kilometer = Label(text="Kilometers", font=("Impact", 12))
equal = Label(text="is equal to", font=("Impact", 12))
km_out = Label(text=0, font=("Impact", 12))
miles_in = Entry(width=10)
miles_in.focus()
cal_button = Button(text="Calculate", font=("Impact", 12), command=calculate)

miles_in.grid(column=1, row=0)
miles.grid(column=2, row=0)
equal.grid(column=0, row=1)
km_out.grid(column=1, row=1)
kilometer.grid(column=2, row=1)
cal_button.grid(column=1, row=2)


window.mainloop()
