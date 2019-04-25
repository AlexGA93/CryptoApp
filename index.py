import tkinter
from tkinter import ttk
#-----------------------------------------------
#importing encryption scripts
#from [carpeta] import [script]
#    [script].funcion()
from AES_method import aes_method
from Blake import blake
from Caesar import caesar
from Fernet import fernet
from Hash import hash_method
from Personal_algorithm import personal
#-----------------------------------------------
bg_gray = 'gray'
ipad_x1 = 10
ipad_x2 = 30
ipad_x3 = 50
ipad_y1 = 10
ipad_y2 = 30

def gui_inputs(frame_entry):
    #section 1- Inputs
    tkinter.Label(frame_entry, text='Please, enter here your text...',bg=bg_gray, font=("Helvetica", 13)).pack(ipadx=ipad_x3,ipady=ipad_y2,pady=1)
    tkinter.Entry(frame_entry).pack(expand=True, fill='both')

def gui_buttonMatrix(frame2, frame3):
    #section 2- button matrix
#-----------------------------------------------------------------------
    tkinter.Button(frame2, text='AES').pack(side=tkinter.LEFT)
    tkinter.Button(frame2, text='Blake').pack(side=tkinter.LEFT)
    tkinter.Button(frame2, text='Caesar').pack(side=tkinter.LEFT)

    tkinter.Button(frame3, text='Fernet').pack(side=tkinter.LEFT)
    tkinter.Button(frame3, text='Hashing').pack(side=tkinter.LEFT)
    tkinter.Button(frame3, text='Inverted Binary').pack(side=tkinter.LEFT)

    #tkinter.Button(frame4, text='example1').pack(side=tkinter.LEFT)
    #tkinter.Button(frame4, text='example1').pack(side=tkinter.LEFT)
    #tkinter.Button(frame4, text='example1').pack(side=tkinter.LEFT)

#-----------------------------------------------------------------------
def gui_output(frame_text):
    #section 3- output
    tkinter.Canvas(frame_text).pack(pady = 10,padx = 50)

def gui_quit(root):
    #Quit Button
    ttk.Button(root, text='Quit', command=quit).place(x=400, y=659)

def gui_frames(root):
    # Label
    tkinter.Label(root, text='Welcome To CryptoApp', bg='#716060',font=("Helvetica", 16)).pack(fill=tkinter.BOTH)
#-----------------------------------------------------------------------
    #Sections(frames)
    frame_entry = tkinter.Frame(root,bg=bg_gray)
    frame_entry.pack(ipadx=ipad_x1,ipady=ipad_y1)

    frame_matrix = tkinter.Frame(root, bg=bg_gray)
    frame_matrix.pack(ipadx=ipad_x2, ipady=ipad_y1, pady=30)

    frame2 = tkinter.Frame(frame_matrix, bg=bg_gray)
    frame2.pack(ipadx=ipad_x1, ipady=ipad_y1)

    frame3 = tkinter.Frame(frame_matrix, bg=bg_gray)
    frame3.pack(ipadx=ipad_x1, ipady=ipad_y1)

    #frame4 = tkinter.Frame(frame_matrix, bg = bg_gray)
    #frame4.pack(ipadx=ipad_x1 ,ipady = ipad_y1)

    frame_text = tkinter.Frame(root, bg=bg_gray )
    frame_text.pack()
#-----------------------------------------------------------------------
    gui_inputs(frame_entry)
    gui_buttonMatrix(frame2, frame3)
    gui_output(frame_text)

def gui_function(root):
    gui_frames(root)
    gui_quit(root)

def main():
    # Creating window
    root = tkinter.Tk()
    # Not Resizable
    root.resizable(False, False)
    # giving window's size
    root.minsize(width=500, height=700)
    # Window Title
    root.title('CryptoApp')
    # background
    root.configure(bg='gray')

    gui_function(root)
    root.mainloop()

if __name__ == '__main__':
    main()
    
    