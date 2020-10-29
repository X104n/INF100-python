from tkinter import *
import tkinter
import tkMessageBox

def click1():
    Label1 = Label (window, image=photo1, bg="black")
    Label1.grid(row=0, column=0, sticky=W)

def click2():
    Label2 = Label (window, image=photo2, bg="black")
    Label2.grid(row=0, column=0, sticky=W)
    tkMessageBox.showinfo("Yes", "No")

window = Tk()

photo1 = PhotoImage(file="skole\Tkinter\\bilde1.png")
photo2 = PhotoImage(file="skole\Tkinter\\bilde2.png")

Label1 = Label (window, image=photo1, bg="black")
Label1.grid(row=0, column=0, sticky=W)

Knapp1 = Button(window, text="Bilde 1", width=20, command=click1) 
Knapp1.grid(row=1, column=0, sticky=W)

Knapp2 = Button(window, text="Bilde 2", width=20, command=click2) 
Knapp2.grid(row=1, column=0, sticky=E)

window.mainloop()