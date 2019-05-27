# importing module.py
# import message_to_code

# caesar function

'''
def caesar(data, order):
    message = ''
    for x in data:
        if x == ' ':
            message += ' '
        chr_to_Ascii = ord(x)
        if(chr_to_Ascii >= 65 and chr_to_Ascii <= 90):
            Ascii_to_Uchr = chr(chr_to_Ascii+order)
            if (ord(Ascii_to_Uchr) > 90):
                Ascii_to_Uchr = chr(97)
            message += Ascii_to_Uchr

        elif(chr_to_Ascii >= 97 and chr_to_Ascii <= 122):  # trabajamos con minusculas
            Ascii_to_Lchr = chr(chr_to_Ascii+order)
            if ord(Ascii_to_Lchr) > 122:
                Ascii_to_Lchr = chr(65)
            message += Ascii_to_Lchr

    return message


def main():
    message = input('Give me a message: ')  # input message GUI
    # input integer GUI
    order = int(input('Give me a order number to cipher: '))

    data = caesar(message, order)
    print(data)


if __name__ == "__main__":
    main()
'''
import tkinter as tk
from tkinter import ttk
# importing index's entry value
#from ... import index


def caesar(data, order):
    # print(data)
    message = ''
    for x in data:
        if x == ' ':
            message += ' '
        chr_to_Ascii = ord(x)
        if(chr_to_Ascii >= 65 and chr_to_Ascii <= 90):
            Ascii_to_Uchr = chr(chr_to_Ascii+order)
            print(Ascii_to_Uchr)
            if (ord(Ascii_to_Uchr) > 90):
                Ascii_to_Uchr = chr(97)
            message += Ascii_to_Uchr

        elif(chr_to_Ascii >= 97 and chr_to_Ascii <= 122):  # trabajamos con minusculas
            Ascii_to_Lchr = chr(chr_to_Ascii+order)
            if ord(Ascii_to_Lchr) > 122:
                Ascii_to_Lchr = chr(65)
            message += Ascii_to_Lchr

    print(message)


def gui_entry(frame_entry, message):
    label = ttk.Label(frame_entry, text="Insert Text here...", anchor='center')
    label.place(x=80, y=10)

    # print message imported
    label = ttk.Label(frame_entry, text="TEXT IMPORTED", anchor='center')
    label.place(x=200, y=10)

    # entry
    label_entry = ttk.Label(frame_entry, text='Enter key [number]')
    label_entry.place(x=130, y=50)

    entry = ttk.Entry(frame_entry)
    entry.place(x=120, y=80)

    # Buttons Ok and Quit
    # boton ok coge el valor de entry y llama a caesar con mensaje y order
    button_Ok = ttk.Button(frame_entry, text='Ok',
                           command=lambda: caesar(message, int(entry.get()))).place(x=300, y=160)
    button_quit = ttk.Button(frame_entry, text='Exit',
                             command=quit).place(x=20, y=160)


def gui_skeleton(root, message):
    label = ttk.Label(root, text='Caesar Method', font=(
        "Helvetica", 16), background='#716060', anchor='center')
    label.pack(fill=tk.BOTH)

    # Frame_entry
    style_entry = ttk.Style()
    style_entry.configure("Frame_entry.TFrame", background='gray')

    frame_entry = ttk.Frame(root, style="Frame_entry.TFrame")
    frame_entry.pack(ipadx=200, ipady=100)

    gui_entry(frame_entry, message)


def gui(message):
    root = tk.Tk()
    root.minsize(width=300, height=200)
    root.resizable(False, False)
    root.title('Caesar Method')

    root.configure(bg='gray')
    gui_skeleton(root, message)

    root.mainloop()
