from tkinter import *


#Functions

    #The yes or no button
def click():
    #Taking the written words in the entry box
    enteredText=textentry.get()
    #
    output.delete(0.0, END)
    try:
        definition = myTextOutput[enteredText]
    except:
        definition = "Bruv, it's litteraly a yes or no question"
    output.insert(END, definition)

    #The exit buttin command
def close():
    window.destroy()
    exit()


### Main ###
window = Tk()
window.title("Kalkulator")
window.configure(background="black")

#Picture
photo1 = PhotoImage(file="skole\Tkinter\me1.png")
Label (window, image=photo1, bg="black") .grid(row=0, column=0, sticky=W)

#Create label
Label (window, text="\nDo you like the cut G?", bg="black", fg="white", font="none 12 bold") .grid(row=1, column=0, sticky=W)

#Create text entry box
textentry = Entry(window, width=20, bg="white")
textentry.grid(row=2, column=0, sticky=W)

#Add button
Button(window, text="Speak to nigga", width=20, command=click) .grid(row=2, column=0, sticky=E)

#Text box
output = Text(window, width=70, height=6, wrap=WORD, background="white")
output.grid(row=3, column=0, columnspan=2, sticky=W)

#Text box output
myTextOutput = {
    'yes': '*Smacks the nigga*', 'no': '*Nigga smacks you*'
}

#Exit label
Label (window, text="EXIT HERE!", bg="black", fg="white", font="none 12 bold") .grid(row=4, column=0, sticky=W)

#Exit button
Button (window, text="EXIT!", width=20, command=close) .grid(row=5, column=0, sticky=W)



###Run the main loop
window.mainloop()