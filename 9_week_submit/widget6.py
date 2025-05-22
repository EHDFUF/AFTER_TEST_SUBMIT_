from tkinter import *
from tkinter import messagebox

window = Tk()

def Funk1():
    if chk.get() == 0:
        messagebox.showinfo("","체크박스꺼짐")
    else:
        messagebox.showinfo("","체크박스켜짐")

chk = IntVar()

cb1 = Checkbutton(window, text = "클릭", variable=chk, command=Funk1)

cb1.pack()

window.mainloop()