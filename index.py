#importing modules
import tkinter as tk
from tkinter import ttk
# -----------------------------------------------
# importing encryption scripts
# from [carpeta] import [script]
#    [script].funcion()
from AES_method import aes_method
from Blake import blake
from Caesar import caesar
from Fernet import fernet
from Hash import hash_method
from Personal_algorithm import personal
# -----------------------------------------------
bg_gray = 'gray'
ipad_x1 = 100
ipad_x2 = 30
ipad_x3 = 50
ipad_y1 = 10
ipad_y2 = 30

height_button = 1
width_button = 15
def gui_buttonMatrix(frame2,frame3):
    
def gui_inputs(root):
    entry = ttk.Entry(root, text='Enter text here',justify=tk.CENTER, show='*',width = 30 )
    #entry.config(state=tk.NORMAL)
    entry.place()

def gui_quit(root):
    #Quit Button
    cancel = ttk.Button(root, text='Quit', command = quit).place(x=400, y=659)

def gui_frames(root):
    #Label
    label = ttk.Label(root, text='Welcome To CryptoApp', font=("Helvetica", 16), background = '#716060', anchor = 'center')
    label.pack(fill = tk.BOTH)

    #Frames
    frame_entry = ttk.Frame(root)
    frame_entry.pack(ipadx=ipad_x1, ipady=ipad_y1)

    frame_matrix = ttk.Frame(root)
    frame_matrix.pack(ipadx=ipad_x2, ipady=ipad_y1, pady=30)

    frame2 = ttk.Frame(frame_matrix)
    frame2.pack(ipadx=ipad_x1, ipady=ipad_y1)

    frame3 = ttk.Frame(frame_matrix)
    frame3.pack(ipadx=ipad_x1, ipady=ipad_y1)
    
    gui_inputs(frame_entry)
    gui_buttonMatrix(frame2,frame3)
    '''
    gui_buttonMatrix(frame2, frame3)
    gui_output(frame_text)
    '''

def gui_functions(root):
    gui_frames(root)
    gui_quit(root)

def main():
    #window creation
    root = tk.Tk()
    # Not Resizable
    #root.resizable(False, False)
    # giving window's size
    root.minsize(width=500, height=700)
    # Window Title
    root.title('CryptoApp')
    # background
    root.configure(bg='gray')

    #calling methods
    gui_functions(root)

    root.mainloop()

if __name__ == "__main__":
    main()


