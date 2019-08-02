# importing modules
from CRC import CRC_method
from TranspMod import transmod
from Inverted import Inverted
from Hash import hash_method
from Fernet import Fernet
from Caesar import Caesar
from Blake import blake
from Atbash import atbash
from AES_method import aes_method
import tkinter as tk
from tkinter import ttk
from tkinter import simpledialog
from tkinter import StringVar, IntVar
# -----------------------------------------------
from Hash import hash_method
# importing scripts

# -----------------------------------------------
# styles variables
font_app = 'Times'
bg_app = '#303F9F'  # 'gray26'
bg_label = '#FF9800'
fr_app = 'White'
fr_label = 'blue'

ipad_x1 = 1
ipad_x2 = 1
ipad_x3 = 1
ipad_x4 = 1
ipad_y1 = 50
ipad_y2 = 30
ipad_y3 = 1
ipad_y4 = 30

# PopupScreen to enter keys


def popupScreen(root):

    answer = simpledialog.askinteger(
        "Key Neccessary", "Enter a key: ", parent=root)
    return answer


def update_text(text_widget, text):
    text_widget.configure(state="normal")
    text_widget.delete('1.0', tk.END)
    text_widget.insert('1.0', text)
    text_widget.configure(state="disabled")


def methods(method, value, text_widget, root):

    if method == 'AES':  # elif method's button is clicked, it submit a code
        # calling to method's script with our messsage
        var = aes_method.encrypt(value)
        update_text(text_widget, var)  # update output label's value

    elif method == 'ATB':
        var = atbash.Atbash_encrypt(value)
        update_text(text_widget, var)

    elif method == 'BLK':
        # elif we need to enter a key, it'll be done by the function
        f = popupScreen(root)
        var = blake.main(value, f)
        update_text(text_widget, var)

    elif method == 'CAESAR':
        g = popupScreen(root)
        var = Caesar.caesar(value, g)
        update_text(text_widget, var)

    elif method == 'FNT':
        var = Fernet.main(value)
        update_text(text_widget, var)

    elif method == 'HSH':
        h = popupScreen(root)
        var = hash_method.hashing_methods(value, h)
        update_text(text_widget, var)
    elif method == 'BNR':
        var = Inverted.toBinary(value)
        update_text(text_widget, var)

    elif method == 'TRANS':
        f = popupScreen(root)
        var = transmod.encryption(value, f)
        textlbl.set(var, font=(font_app, 2))

    elif method == 'CRC':
        j = popupScreen(root)
        var = CRC_method.main(value, j)
        update_text(text_widget, var)


# function to reset entry and output values
def resetFunction(text_entry, text_output):
    # set default values to 'entry' and 'output'

    entry_default = ' '
    output_default = 'Data Ouput.'

    # reset values
    text_entry.set(entry_default)
    update_text(text_output, output_default)

# render function


def gui_frames(root):
    # Label
    label = ttk.Label(root, text='Welcome To CryptoApp', font=(
        font_app, 16), background=bg_label, anchor='center')
    label.pack(fill=tk.BOTH)

    style_entry = ttk.Style()
    style_entry.configure("Frame_entry.TFrame", background=bg_app)
    # Frames
    frame_entry = ttk.Frame(root, style="Frame_entry.TFrame")
    frame_entry.pack(ipadx=ipad_x1, ipady=ipad_y1)

    style_buttns = ttk.Style()
    style_buttns.configure("FrameB.TFrame", background=bg_app)
    frame_matrix = ttk.Frame(root, style='FrameB.TFrame')
    frame_matrix.pack(ipadx=ipad_x2, ipady=ipad_y2)

    # Frame Text(output)
    style_output = ttk.Style()
    style_output.configure("Frame_output.TFrame", background=bg_app)
    frame_output = ttk.Frame(root, style='Frame_output.TFrame')
    frame_output.pack(ipadx=ipad_x3, ipady=ipad_y3)

    # ---------------------------------------------------------------
    label = ttk.Label(frame_entry, text="Insert Text here...",
                      anchor='center', background=bg_app, foreground=bg_label,
                      font=(font_app, 10))
    label.pack(side="left")
    # INPUT
    text_entry = StringVar()
    text_entry.set('')

    entry = ttk.Entry(frame_entry, textvariable=text_entry)
    entry.pack(side="left")
    # ---------------------------------------------------------------
    style_buttons = ttk.Style()
    style_buttons.configure("Style_buttons.TButton")

    # sustituir por elmento que permita scroll como un entry?
    xscrollbar = tk.Scrollbar(frame_output, orient=tk.HORIZONTAL)
    yscrollbar = tk.Scrollbar(frame_output)

    text_output = tk.Text(frame_output,
                          width=10,
                          height=2,
                          font=(font_app, 10),
                          wrap=tk.NONE,
                          xscrollcommand=xscrollbar.set,
                          yscrollcommand=yscrollbar.set)
    text_output.bind("<1>", lambda event: text_output.focus_set())
    xscrollbar.config(command=text_output.xview)
    yscrollbar.config(command=text_output.yview)

    yscrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    xscrollbar.pack(side=tk.BOTTOM, fill=tk.X)
    text_output.pack(expand=tk.TRUE, fill=tk.BOTH, ipadx=190, ipady=150)
    update_text(text_output, "Data Output.")
    # buttons

    aesButton = ttk.Button(frame_matrix, text="AES",
                           command=lambda: methods('AES', entry.get(), text_output, root))

    atbashButton = ttk.Button(frame_matrix, text="Atbash", command=lambda: methods(
        'ATB', entry.get(), text_output, root))

    blakeButton = ttk.Button(frame_matrix, text="Blake", command=lambda: methods(
        'BLK', entry.get(), text_output, root))

    caesarButton = ttk.Button(frame_matrix, text="Caesar",
                              command=lambda: methods('CAESAR', entry.get(), text_output, root))

    fernetButton = ttk.Button(frame_matrix, text="Fernet", command=lambda: methods(
        'FNT', entry.get(), text_output, root))

    hashButton = ttk.Button(frame_matrix, text="Hash", command=lambda: methods(
        'HSH', entry.get(), text_output, root))

    doubleBinButton = ttk.Button(frame_matrix, text="DoubleBin", command=lambda: methods(
        'BNR', entry.get(), text_output, root))

    transpositionButton = ttk.Button(
        frame_matrix, text="Transposition", command=lambda: methods('TRANS', entry.get(), text_output, root))

    button9 = ttk.Button(frame_matrix, text="CRC", command=lambda: methods(
        'CRC', entry.get(), text_output, root))

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

    # Reset Button

    tk.Button(root, text='Reset', command=lambda: resetFunction(
        text_entry, text_output), background=bg_label, activeforeground=fr_app, activebackground="blue", height=1, width=10).place(x=20, y=700)

    # Quit Button

    tk.Button(
        root, text='Cancel', command=quit, background=bg_label, activeforeground=fr_app, activebackground="red", height=1, width=10).place(x=400, y=700)

# main function


def main():
    # window creation
    root = tk.Tk()
    # Not Resizable
    root.resizable(False, False)

    # Render at center's screen (aprox.)
    # Gets the requested values of the height and widht.
    winWidth = root.winfo_reqwidth()
    winHeight = root.winfo_reqheight()
    print("Width: {} \nHeight: {}".format(winWidth, winHeight))

    # Gets both half the screen width/height and window width/height
    posRight = int(root.winfo_screenwidth()/2 - (winWidth+500)/2)
    posDown = int(root.winfo_screenheight()/2 - (winHeight+500)/2)
    print("position right: {}, Position down: {}".format(
        posRight, posDown))
    # Positions the window in the center of the page.
    root.geometry("+{}+{}".format(posRight, posDown))

    # giving window's size
    root.minsize(width=500, height=750)
    # rendering at screen's center

    # Window Title
    root.title('CryptoApp')
    # background
    root.configure(bg=bg_app)
    # calling methods
    gui_frames(root)

    root.mainloop()


if __name__ == "__main__":
    main()
