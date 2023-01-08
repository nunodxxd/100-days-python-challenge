from tkinter import *

window = Tk()
window.title("Widget Examples")
window.minsize(width=500, height=500)
window.config(padx=20,pady=20)

#label
label = Label(text="Label")
label.grid(column=0,row=0)

#button
button = Button(text="Click Me")
button.grid(column=1,row=1)

#button
new_button = Button(text="Click Me")
new_button.grid(column=2,row=0)

#entry
entry = Entry(width=30)
print(entry.get())
entry.grid(column=3,row=3)

window.mainloop()