from tkinter import *

root = Tk()

def ShowTable():
   number = int(entry.get())
   for var in range(0,11):
        result = var * number
        resultString = str(number) + ' x ' + str(var) + ' = ' + str(result)
        varSelected = labelList.__getitem__(var)
        varSelected.set(resultString)

entry = Entry(root)
entry.pack()

Button(root, text="show table", command=ShowTable).pack()

labelList = []
colorList = ['green', 'red', 'yellow', 'black', 'orange', 'blue', 'pink', 'white', 'gray', 'green', 'blue']
for lab in range(0,11):
    var = StringVar()
    Label(root, textvariable = var, bg = colorList.__getitem__(lab)).pack()
    labelList.append(var)

root.mainloop()