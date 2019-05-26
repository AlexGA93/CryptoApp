# importing modules

import tkinter as tk
from tkinter import ttk

# -----------------------------------------------
# importing encryption scripts
# from [carpeta] import [script]
#    [script].funcion()
'''
from AES_method import aes_method
from Blake import blake
from Caesar import Caesar
from Fernet import Fernet
from Hash import hash_method
from personal_algorithm import personal
'''
# -----------------------------------------------
bg_gray = 'gray'
ipad_x1 = 200
ipad_x2 = 1
ipad_x3 = 1
ipad_y1 = 50
ipad_y2 = 30
ipad_y3 = 1

height_button = 1
width_button = 15


def gui_output(frame_output):
    output = ttk.Label(frame_output)
    output.pack(ipadx=190, ipady = 150)


def gui_buttonMatrix(frame_matrix):

    style_buttons = ttk.Style()
    style_buttons.configure("Style_buttons.TButton")
    # buttons
    button1 = ttk.Button(frame_matrix, text="button1")
    button2 = ttk.Button(frame_matrix, text="button2")
    button3 = ttk.Button(frame_matrix, text="button3")

    button4 = ttk.Button(frame_matrix, text="button4")
    button5 = ttk.Button(frame_matrix, text="button5")
    button6 = ttk.Button(frame_matrix, text="button6")

    button7 = ttk.Button(frame_matrix, text="button7")
    button8 = ttk.Button(frame_matrix, text="button8")
    button9 = ttk.Button(frame_matrix, text="button9")

    button1.grid(row = 0, column = 0, padx = 10, pady = 10)
    button2.grid(row = 0, column = 1, padx = 10, pady = 10)
    button3.grid(row = 0, column = 2, padx = 10, pady = 10)
    button4.grid(row = 1, column = 0, padx = 10, pady = 10)
    button5.grid(row = 1, column = 1, padx = 10, pady = 10)
    button6.grid(row = 1, column = 2, padx = 10, pady = 10)
    button7.grid(row = 2, column = 0, padx = 10, pady = 10)
    button8.grid(row = 2, column = 1, padx = 10, pady = 10)
    button9.grid(row = 2, column = 2, padx = 10, pady = 10)


def gui_inputs(frame_entry):
    label = ttk.Label(frame_entry, text="Insert Text here...", anchor='center')
    label.place(x=77, y=50)
    entry = ttk.Entry(frame_entry)
    entry.place(x=180, y=50)


def gui_quit(root):
    # Quit Button
    cancel = ttk.Button(root, text='Quit', command=quit).place(x=400, y=659)


def gui_frames(root):
    # Label
    label = ttk.Label(root, text='Welcome To CryptoApp', font=(
        "Helvetica", 16), background='#716060', anchor='center')
    label.pack(fill=tk.BOTH)

    style_entry = ttk.Style()
    style_entry.configure("Frame_entry.TFrame", background=bg_gray)
    # Frames
    frame_entry = ttk.Frame(root, style="Frame_entry.TFrame")
    frame_entry.pack(ipadx=ipad_x1, ipady=ipad_y1)

    style_buttns = ttk.Style()
    style_buttns.configure("FrameB.TFrame", background=bg_gray)
    frame_matrix = ttk.Frame(root, style='FrameB.TFrame')
    frame_matrix.pack(ipadx=ipad_x2, ipady=ipad_y2)

    #Frame Text(output)
    style_output = ttk.Style()
    style_output.configure("Frame_output.TFrame", background = bg_gray)
    frame_output = ttk.Frame(root, style = 'Frame_output.TFrame')
    frame_output.pack(ipadx = ipad_x3, ipady = ipad_y3)

    gui_inputs(frame_entry)
    gui_buttonMatrix(frame_matrix)
    gui_output(frame_output)
    


def gui_functions(root):
    gui_frames(root)
    gui_quit(root)


def main():
    # window creation
    root = tk.Tk()
    # Not Resizable
    #root.resizable(False, False)
    # giving window's size
    root.minsize(width=500, height=700)
    # Window Title
    root.title('CryptoApp')
    # background
    root.configure(bg='gray')

    # calling methods
    gui_functions(root)

    root.mainloop()


if __name__ == "__main__":
    main()
