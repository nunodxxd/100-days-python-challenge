from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    entry_passwd.delete(0, END)
    passwd = ""
    for _ in range(0, 15):
        passwd += chr(random.randint(33, 126))
    entry_passwd.insert(0, passwd)
    pyperclip.copy(passwd)

# ---------------------------- SEARCH ACCOUNT ------------------------------- #

def search():
    website = entry_website.get()
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found.")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {website} exists.")


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    website = entry_website.get()
    email = entry_username.get()
    password = entry_passwd.get()
    new_data = {website: {"email": email, "password": password}}

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(
            title="Oops", message="Please don't leave any fields empty!")
    else:
        try:
            with open("data.json", "r") as data_file:
                # reading old data
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            with open("data.json", "w") as data_file:
                # updating old data with new data
                data.update(new_data)
                # saving updated data
                json.dump(data, data_file, indent=4)
        finally:
                entry_website.delete(0, END)
                entry_passwd.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Passowrd Manager")
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

# label's
label_website = Label(text="Website:")
label_website.grid(column=0, row=1)
label_username = Label(text="Email/Username:")
label_username.grid(column=0, row=2)
label_passwd = Label(text="Password:")
label_passwd.grid(column=0, row=3)

# entry 's
entry_website = Entry(width=17)
entry_website.grid(column=1, row=1)
entry_username = Entry(width=35)
entry_username.grid(column=1, row=2, columnspan=2)
entry_username.insert(0, "@gmail.com")
entry_passwd = Entry(width=17)
entry_passwd.grid(column=1, row=3)

# button's
button_generator = Button(text="Generate Password", command=generate_password)
button_generator.grid(column=2, row=3)

button_search = Button(text="Search", width=13, command=search)
button_search.grid(column=2, row=1)

button_save = Button(text="Add", width=30, command=save)
button_save.grid(column=1, row=4, columnspan=2)


window.mainloop()
