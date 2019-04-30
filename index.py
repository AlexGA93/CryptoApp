# importing modules
import tkinter as tk
from tkinter import ttk
from tkinter.ttk import *
# -----------------------------------------------
# importing encryption scripts
# from [carpeta] import [script]
#    [script].funcion()
from AES_method import aes_method
from Blake import blake
from Caesar import Caesar
from Fernet import Fernet
from Hash import hash_method
from personal_algorithm import personal
# -----------------------------------------------
bg_gray = 'gray'
ipad_x1 = 200
ipad_x2 = 200
ipad_x3 = 50
ipad_y1 = 50
ipad_y2 = 30

height_button = 1
width_button = 15


def gui_buttonMatrix(frame2, frame3):

    style_buttons = ttk.Style("Style_buttons.TButton")
    style_buttons.configure()
    # buttons
    button1 = ttk.Button(frame2, text="button1").pack()
    button1 = ttk.Button(frame2, text="button1").pack()
    button1 = ttk.Button(frame2, text="button1").pack()


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
    style_entry.configure("Frame_entry.TFrame", background="black")
    # Frames
    frame_entry = ttk.Frame(root, style="Frame_entry.TFrame")
    frame_entry.pack(ipadx=ipad_x1, ipady=ipad_y1)

    style_buttns = ttk.Style()
    style_buttns.configure("FrameB.TFrame", background='blue')
    frame_matrix = ttk.Frame(root, style='FrameB.TFrame')
    frame_matrix.pack(ipadx=ipad_x2, ipady=ipad_y1)

    # Frame2 and 3

    frame2 = ttk.Frame(frame_matrix)
    frame2.pack(ipadx=ipad_x1, ipady=ipad_y1)

    frame3 = ttk.Frame(frame_matrix)
    frame3.pack(ipadx=ipad_x1, ipady=ipad_y1)

    gui_inputs(frame_entry)
    gui_buttonMatrix(frame2, frame3)

    '''
    gui_output(frame_text)
    '''


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
