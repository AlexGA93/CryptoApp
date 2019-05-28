# importing modules

import tkinter as tk
from tkinter import ttk
from tkinter import simpledialog
from tkinter import StringVar, IntVar
# -----------------------------------------------
# importing encryption scripts
# from [carpeta] import [script]
#    [script].funcion()

from AES_method import aes_method
from Atbash import atbash
from Blake import blake
from Caesar import Caesar
from Fernet import Fernet
from Hash import hash_method
from personal_algorithm import personal
from TranspMod import transmod

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


def popupscreen(root):  # render to get additional data
    #app = tk.Tk()
    # pp.geometry("1x1")
    answer = simpledialog.askinteger(
        "Key", "Give me a key: ", parent=root)
    return answer


# working with 'button's code', 'key' and label's text variable to update
def methods(method, value, textlbl, root):
    #
    if method == 'AES':
        var = aes_method.encrypt(value)
        textlbl.set(var)

    if method == 'ATB':
        var = atbash.Atbash_encrypt(value)
        textlbl.set(var)

    if method == 'BLK':
        f = popupscreen(root)
        var = blake.main(value, f)
        textlbl.set(var)

    if method == 'CAESAR':
        g = popupscreen(root)  # additional data to Caesar's method
        var = Caesar.caesar(value, g)  # caesar function from script
        textlbl.set(var)  # updating label value

    if method == 'FNT':
        var = Fernet.main(value)
        textlbl.set(var)

    if method == 'HSH':
        h = popupscreen(root)
        var = hash_method.hashing_methods(value, h)
        textlbl.set(var)
    if method == 'BNR':
        var = personal.toBinary(value)
        textlbl.set(var)

    if method == 'TRANS':
        f = popupscreen(root)
        var = transmod.encryption(value, f)
        textlbl.set(var, font=("Helvetica", 9))


def gui_quit(root):
    # Quit Button
    cancel = ttk.Button(root, text='Quit', command=quit).place(x=400, y=700)


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

    # Frame Text(output)
    style_output = ttk.Style()
    style_output.configure("Frame_output.TFrame", background=bg_gray)
    frame_output = ttk.Frame(root, style='Frame_output.TFrame')
    frame_output.pack(ipadx=ipad_x3, ipady=ipad_y3)

    # ---------------------------------------------------------------
    label = ttk.Label(frame_entry, text="Insert Text here...", anchor='center')
    label.place(x=77, y=50)

    # INPUT
    entry = ttk.Entry(frame_entry)
    entry.place(x=180, y=50)
    # ---------------------------------------------------------------
    style_buttons = ttk.Style()
    style_buttons.configure("Style_buttons.TButton")

    # Update label value?
    text = StringVar()
    text.set('Data Ouput')
    outputlbl = ttk.Label(frame_output, width=10,
                          textvariable=text, font=("Helvetica", 10))
    outputlbl.pack(ipadx=190, ipady=150)

    # buttons
    aesButton = ttk.Button(frame_matrix, text="AES",
                           command=lambda: methods('AES', entry.get(), text, root))

    atbashButton = ttk.Button(frame_matrix, text="Atbash", command=lambda: methods(
        'ATB', entry.get(), text, root))

    blakeButton = ttk.Button(frame_matrix, text="Blake", command=lambda: methods(
        'BLK', entry.get(), text, root))

    caesarButton = ttk.Button(frame_matrix, text="Caesar",
                              command=lambda: methods('CAESAR', entry.get(), text, root))

    fernetButton = ttk.Button(frame_matrix, text="Fernet", command=lambda: methods(
        'FNT', entry.get(), text, root))

    hashButton = ttk.Button(frame_matrix, text="Hash", command=lambda: methods(
        'HSH', entry.get(), text, root))

    doubleBinButton = ttk.Button(frame_matrix, text="DoubleBin", command=lambda: methods(
        'BNR', entry.get(), text, root))

    transpositionButton = ttk.Button(
        frame_matrix, text="Transposition", command=lambda: methods('TRANS', entry.get(), text, root))

    button9 = ttk.Button(frame_matrix, text="[Not Avaible]")

    aesButton.grid(row=0, column=0, padx=10, pady=10)
    atbashButton.grid(row=0, column=1, padx=10, pady=10)
    blakeButton.grid(row=0, column=2, padx=10, pady=10)
    caesarButton.grid(row=1, column=0, padx=10, pady=10)
    fernetButton.grid(row=1, column=1, padx=10, pady=10)
    hashButton.grid(row=1, column=2, padx=10, pady=10)
    doubleBinButton.grid(row=2, column=0, padx=10, pady=10)
    transpositionButton.grid(row=2, column=1, padx=10, pady=10)
    button9.grid(row=2, column=2, padx=10, pady=10)
    # ---------------------------------------------------------------


def gui_functions(root):
    gui_frames(root)
    gui_quit(root)


def main():
    # window creation
    root = tk.Tk()
    # Not Resizable
    root.resizable(False, False)
    # giving window's size
    root.minsize(width=500, height=750)
    # Window Title
    root.title('CryptoApp')
    # background
    root.configure(bg='gray')
    # calling methods
    gui_functions(root)

    root.mainloop()


if __name__ == "__main__":
    main()
