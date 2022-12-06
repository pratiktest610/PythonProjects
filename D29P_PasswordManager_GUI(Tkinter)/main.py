from tkinter import *
from tkinter import messagebox
import random
import pyperclip

bg = "#393E46"
fg = "#EEEEEE"
bg2 = "#222831"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def gen_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list1 = [random.choice(letters) for char in range(nr_letters)]
    password_list2 = [random.choice(symbols) for char in range(nr_symbols)]
    password_list3 = [random.choice(numbers) for char in range(nr_numbers)]
    password_list = password_list3 + password_list2 + password_list1

    random.shuffle(password_list)
    password = "".join(password_list)
    password_input.delete(0, END)
    password_input.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #


def add_info():
    website = website_input.get()
    username = username_input.get()
    password = password_input.get()

    if len(website) < 1 or len(username) < 1 or len(password) < 1:
        messagebox.showinfo(title="Alert!!", message="Plese dont leave any field empty")
    else:
        is_ok = messagebox.askyesno(title=f"{website}", message=f"Is the following information correct?\n"
                                                                f" Username: {username}\n Password: {password}")
        if is_ok:
            with open("data.txt", "a") as file:
                file.write(f"{website} | {username} | {password}\n")
            website_input.delete(0, END)
            password_input.delete(0, END)
            messagebox.showinfo(message=f"Information saved successfully!\nPassword copied to clipboard.")
# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.minsize(width=500, height=500)
window.config(bg=bg, padx=50, pady=50)

logo = PhotoImage(file="logo.png")

canvas = Canvas(width=200, height=200, bg=bg, highlightthickness=0)
canvas.create_image(100, 100, image=logo)
canvas.grid(column=0, row=0, columnspan=3)

website_label = Label(text="Website : ", font=("High Tower", 12), fg=fg, bg=bg)
website_label.grid(column=0, row=1)

username_label = Label(text="Username/Email : ", font=("High Tower", 12), fg=fg, bg=bg)
username_label.grid(column=0, row=2)

Password_label = Label(text="Password : ", font=("High Tower", 12), fg=fg, bg=bg)
Password_label.grid(column=0, row=3)

website_input = Entry(bg=bg2, fg=fg, width=50)
website_input.focus()
website_input.grid(column=1, row=1, columnspan=2)

username_input = Entry(bg=bg2, fg=fg, width=50)
username_input.grid(column=1, row=2, columnspan=2)
username_input.insert(0, "pratik6102003")

password_input = Entry(bg=bg2, fg=fg, width=21)
password_input.grid(column=1, row=3)

generate_button = Button(text="Generate Password",font=("High Tower", 12), fg=fg, bg=bg2, command=gen_password)
generate_button.grid(column=2, row=3)

add_button = Button(text="Add", font=("High Tower", 10), fg=fg, bg=bg2, width=36, command=add_info)
add_button.grid(column=1, row=4, columnspan=2)


window.mainloop()
