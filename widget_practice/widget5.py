from tkinter import *
from tkinter import messagebox 

def Func1():
    messagebox.showinfo("강아지버튼", "so cute")

window = Tk()

photo = PhotoImage(file="C:\\Users\\homii\OneDrive\\SUBMIT_\\widget_practice\\dog.gif")

button1 = Button(window, image=photo, command=Func1)

button1.pack()

window.mainloop()