from tkinter import *

HEIGHT = 800
WIDTH = 800
N = 0
#Commands
def bye():
    root.destroy()
    exit()

#Gutta gjer matten
def math(N):
    outputText = "Dine primtall er: "
    x = 2
    while x <= N:
    
        if N % x == 0:
            outputText = (outputText + "\n" + str(x))
            N = N/x
            x = 2
        else:
            x += 1
    return outputText

#Finne ut om du e domdom
def primtall():
    enteredText = textentry.get()
    output.delete(0.0, END)
    if enteredText.isdigit():
        N = enteredText
        N = int(N)
        tall(N)
    else:
        outputText = "Skriv in et tall domdom. (PS: Det må vær positivt)"
    
    output.insert(END, outputText)

#Sjekke kas tall du har skreve inn
def tall(N):  
    if N >= 2:
        outputText = math(N)
    elif N == 1 or N == 0:
        outputText = "Bruh, detta bør du konna"
    else:
        outputText = "Skriv inn et positivt tall madafaka!"
    output.insert(END, outputText)


###
root = Tk()
root.title("Stian's primtall :))")
###

canvas = Canvas (root, height=HEIGHT, width=WIDTH)
canvas.pack()

#Bakgrunns bilde
photo1 = PhotoImage(file="Tkinter\windows.png")
canv1 =Label (root, image=photo1, bg="black", bd=0)
canv1.place(relwidth=1, relheight=1)

#Skriv inn primtall#
inter = Frame(root, bg="black") 
inter.place(relx=0.05, rely=0.05, relwidth=0.9, relheight=0.75)

#Tekst felt: write prime
txt = Label(inter, text="Write your number below:", bg="white", fg="black", font="IMPACT 30 bold")
txt.place(relx=0.1, rely=0.05, relwidth=0.8, relheight=0.1)

#Writing box
textentry = Entry(inter, width=20, bg="white", font="none 20 bold")
textentry.place(relx=0.1, rely=0.20, relwidth=0.5, relheight=0.05)

#Number button
numButL = Label(inter, bg="black", bd=0)
numButL.place(relx=0.65, rely=0.20, relwidth=0.25, relheight=0.05)

numBut = Button(numButL, text="Yea, thats my number!", font="none 10 bold", bd=5, command=primtall)
numBut.pack(fill="both", expand=True)

#Text over output
txt1 = Label(inter, text="The Facts:      ", bg="black", fg="white", font="none 15 bold")
txt1.place(relx=0.1, rely=0.30, relwidth=0.2, relheight=0.1)

#Output box
output = Text(inter, width=70, height=6, wrap=WORD, background="white")
output.place(relx=0.1, rely=0.40, relwidth=0.8, relheight=0.5)


### Exit Button ###
frame = Frame(root, bg="black", bd=5)
frame.place(relx=0.5, rely=0.95, relwidth=0.5, relheight=0.1, anchor="s")

exitBut = Button(frame, text="Exit", font="none 20 bold", bd=10, command=bye)
exitBut.pack(fill="both", expand=True)
####################


root.mainloop()