from tkinter import *
window = Tk()

label1 = Label(window, text="COOKBOOK") #Label함수로 레이블만들기 
label2 = Label(window, text="열심히", font=("궁서체", 30), fg="blue")
label3 = Label(window, text="공부중", bg="magenta", width=20, height=5, anchor=SE)

label1.pack() #만들어진레이블을 pack()을 통해 화면에 표시시
label2.pack()
label3.pack()

window.mainloop()