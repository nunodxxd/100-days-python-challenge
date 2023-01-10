from tkinter import *
from tkinter import messagebox
import random
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    entry_passwd.delete(0,END)
    passwd = ""
    for i in range(0,15):
        passwd += chr(random.randint(33,126))
    entry_passwd.insert(0,passwd)
    pyperclip.copy(passwd)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = entry_website.get()
    email = entry_username.get()
    password = entry_passwd.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops",message="Please don't leave any fields empty!")
    else:   
        is_ok = messagebox.askokcancel(title=website,message=f"These are the details entered: \nEmail: {email} \nPassword: {password} \nIs it ok to save?")

        if is_ok:
            with open("data.txt","a") as data_file:
                data_file.write(f"{website} | {email} | {password}\n")
                entry_website.delete(0,END)
                entry_passwd.delete(0,END)
                messagebox.showinfo(title="Success",message="Your data has been saved")

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Passowrd Manager")
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

#label's
label_website = Label(text="Website:")
label_website.grid(column=0,row=1)
label_username = Label(text="Email/Username:")
label_username.grid(column=0,row=2)
label_passwd = Label(text="Password:")
label_passwd.grid(column=0,row=3)

#entry 's
entry_website = Entry(width=35)
entry_website.grid(column=1,row=1,columnspan=2)
entry_username = Entry(width=35)
entry_username.grid(column=1,row=2,columnspan=2)
entry_passwd = Entry(width=17)
entry_passwd.grid(column=1,row=3)

#button's
button_generator = Button(text="Generate Password",command=generate_password)
button_generator.grid(column=2,row=3)

button_save = Button(text="Add",width=30,command=save)
button_save.grid(column=1,row=4,columnspan=2)


window.mainloop()
