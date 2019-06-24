from tkinter import *

root = Tk()

l1 = Label(root, text="Primera label", bg="red")
l1.grid(row=0,column=0, ipadx="20", ipady="20")
l2 = Label(root, text="Segunda label", bg="yellow")
l2.grid(row=0,column=1, ipady="20")
l3 = Label(root, text="Tercera label", bg="blue")
l3.grid(row=1,column=0, padx="20", pady="20")
l4 = Label(root, text="Cuarta label", bg="green")
l4.grid(row=1,column=1, ipadx="20")

l5 = Label(root, text="Quinta label", bg="green")
l5.grid(row=0,column=2, sticky="WE")
l6 = Label(root, text="Sexta label", bg="red")
l6.grid(row=1,column=2, sticky="NS")

root.mainloop()