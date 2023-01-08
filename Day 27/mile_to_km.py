from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.config(padx=20,pady=20)

def convert_mph_km():
    mph = entry_mph.get()
    km = int(mph) * 1.609344
    label_value.config(text=f"{km}")
    
#entry
entry_mph = Entry(width=10)
entry_mph.grid(column=1,row=0)

#label's
label_miles = Label(text="Miles")
label_miles.grid(column=2,row=0)

label_km = Label(text="Km")
label_km.grid(column=2,row=1)

label_equal = Label(text="is equal to")
label_equal.grid(column=0,row=1)

label_value = Label(text="0")
label_value.grid(column=1,row=1)

#button
button = Button(text="Calculate",command=convert_mph_km)
button.grid(column=1,row=2)



window.mainloop()