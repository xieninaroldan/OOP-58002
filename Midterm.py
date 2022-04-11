from tkinter import *
class MyWindow:
 def __init__(self, win):
    self.lbl1=Label(win, text='Enter your fullname:', fg='Red')
    self.lbl1.place(x=20, y=70)
    self.t1=Entry()
    self.t1.place(x=220, y=70)
    self.t1.place(width=180, height=30)
    self.t2 = Entry()
    self.t2.place(x=220, y=100)
    self.t2.place(width=180, height=30)

    button=Button(window,text = "Click to display your fullname", fg = "red", font =("Verdana",8))
    button.place(x=20,y=100)


window = Tk()
MyWindow = MyWindow(window)
window.title('Midterm in OOP')
window.geometry("300x200+10+10")
window.mainloop()