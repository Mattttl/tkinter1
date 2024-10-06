from tkinter import *
from datetime import date

root = Tk()
root.title('Getting Started with widgets')
root.geometry("400x300")

labelle = Label(text="Hey There!",bg="#030B76",fg="white",height=1,width=300)
name_labelle = Label(text="Full Name", bg="#3895D3")
name_entry = Entry()

text_box = Text(height=3)
def display():
    name = name_entry.get()

    global message
    message = "Welcome to the Application! \nToday's date is: " 
    greet= f"Hello {name}!"
    text_box.insert(END,greet)
    text_box.insert(END,message)
    text_box.insert(END,date.today())
btn = Button(text="Run", command=display, height=1,bg = "#030B76", fg='white')

labelle.pack()
name_labelle.pack()
name_entry.pack()
btn.pack()
text_box.pack()

root.mainloop()