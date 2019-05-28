
'''
import tkinter as tk
import time


class A:
    def __init__(root, master):
        root.label = tk.Label(master)
        root.label.grid(row=0, column=0)
        root.label.configure(text=' ')
        root.count = 0

        # root.update_label()

    def update_label(root):
        if root.count < 10:
            root.label.configure(text='count: {}'.format(root.count))
            # call this method again in 1,000 milliseconds
            root.label.after(1000, root.update_label)
            root.count += 1
        print(root.count)


root = tk.Tk()
A(root)

root.mainloop()
'''
from tkinter import *
from time import sleep

root = Tk()
var = StringVar()
var.set('hello')

l = Label(root, textvariable = var)
l.pack()

for i in range(6):
    sleep(1) # Need this to slow the changes down
    var.set('goodbye' if i%2 else 'hello')
    root.update_idletasks()