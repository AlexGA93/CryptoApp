import tkinter
# widgets
from tkinter import ttk


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

bg_gray = 'gray'
ipad_x1 = 10
ipad_x2 = 30
ipad_x3 = 50
ipad_y1 = 10
ipad_y2 = 30

# Label
tkinter.Label(root, text='Welcome To CryptoApp', bg='#716060',
              font=("Helvetica", 16)).pack(fill=tkinter.BOTH)

#Sections(frames)
frame_entry = tkinter.Frame(root,bg=bg_gray)
frame_entry.pack(ipadx=ipad_x1,ipady=ipad_y1)

frame_matrix = tkinter.Frame(root, bg=bg_gray)
frame_matrix.pack(ipadx=30, ipady=ipad_y1)

frame2 = tkinter.Frame(frame_matrix, bg=bg_gray)
frame2.pack(ipadx=ipad_x1, ipady=ipad_y1)

frame3 = tkinter.Frame(frame_matrix, bg=bg_gray)
frame3.pack(ipadx=ipad_x1, ipady=ipad_y1)

frame_text = tkinter.Frame(root, bg=bg_gray )
frame_text.pack()

#section 1- Inputs
tkinter.Label(frame_entry, text='Please, enter here your text...',
              bg=bg_gray, font=("Helvetica", 13)).pack(ipadx=ipad_x3,ipady=ipad_y2,pady=1)
tkinter.Entry(frame_entry).pack()

#section 2- button matrix
tkinter.Button(frame2, text='example1').pack(side=tkinter.LEFT)
tkinter.Button(frame2, text='example1').pack(side=tkinter.LEFT)
tkinter.Button(frame2, text='example1').pack(side=tkinter.LEFT)

tkinter.Button(frame3, text='example1').pack(side=tkinter.LEFT)
tkinter.Button(frame3, text='example1').pack(side=tkinter.LEFT)
tkinter.Button(frame3, text='example1').pack(side=tkinter.LEFT)

#section 3- output
quote = "hello wordl!"

tkinter.Canvas(frame_text).pack(pady=100)

'''
text_out = tkinter.Text(root)
text_out.pack(side = n, padx=10, pady=10)
text_out.insert(tkinter.INSERT,quote)
'''
#Quit Button
ttk.Button(root, text='Quit', command=quit).place(x=400, y=659)
root.mainloop()
