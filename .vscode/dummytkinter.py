from tkinter import *
from tkinter import messagebox

def onClick(color):
    #messagebox._show("Message", "pulsado")
    labelText.set('pressed ' + color)
    label1.config(bg = color)

root = Tk()

labelText = StringVar()
labelText.set('texto')

label1 = Label(root, textvariable=labelText)
label1.pack()

Button(root, text="ButtonRed", command=lambda:onClick('red')).pack()
Button(root, text="ButtonBlue", command=lambda:onClick('blue')).pack()
Button(root, text="ButtonBlack", command=lambda:onClick('black')).pack()

root.mainloop()