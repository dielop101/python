from tkinter import *

def itemFirst():
    print('open')
def quitApp():
    quit()


root = Tk()

menu = Menu(root)
root.config(menu = menu)

submenu = Menu(menu, tearoff = 0)
menu.add_cascade(label='Primer menu', menu= submenu)
submenu.add_command(label = "item 1", command=itemFirst)
submenu.add_separator()
submenu.add_command(label = "item 2", command= quitApp)

submenu2 = Menu(menu, tearoff = 0)
menu.add_cascade(label='Segundo menu', menu= submenu2)
submenu2.add_command(label = "item 3")
submenu2.add_separator()
submenu2.add_command(label = "item 4")


root.mainloop()