import tkinter
# widgets
from tkinter import ttk


# Creating window
root = tkinter.Tk()
# Not Resizable
root.resizable(False, False)
# giving window's size
root.minsize(width=500, height=500)
root.maxsize(width=900, height=900)
# Window Title
root.title('CryptoApp')
# background
root.configure(bg='gray')

# Label
tkinter.Label(root, text='Welcome To CryptoApp', bg='gray',
              font=("Helvetica", 16)).pack(fill=tkinter.BOTH)

# Separator to first block of content
tkinter.Label(root, text='Please, enter here your text...',
              bg='gray', font=("Helvetica", 13)).pack(ipadx=50, ipady=50)
tkinter.Entry(root).pack()

# Buttons Matrix(calling functions in another script and return the result to print here)
frame = tkinter.Frame(root, bg='blue')
frame.pack(ipadx=30, ipady=10)

frame2 = tkinter.Frame(frame, bg='red')
frame2.pack(ipadx=50, ipady=50)

tkinter.Button(frame2, text='example1').pack(side=tkinter.LEFT)
tkinter.Button(frame2, text='example1').pack(side=tkinter.LEFT)
tkinter.Button(frame2, text='example1').pack(side=tkinter.LEFT)
# Frame with buttons inside???

# Text Area to print result


# Button creation with root as a windos where it'll render
ttk.Button(root, text='Quit', command=quit).place(x=400, y=450)
root.mainloop()
