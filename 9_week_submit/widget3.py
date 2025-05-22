from tkinter import * 
window = Tk()

photo = PhotoImage(file="C:\\Users\\homii\OneDrive\\SUBMIT_\\widget_practice\\dog.gif") #\\로 \표시
label1 = Label(window, image=photo)

label1.pack()

window.mainloop()