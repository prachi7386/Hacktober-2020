from Tkinter import *
def SIGNUP():
    import Signup
def LOGIN():
    import Login


root = Tk()
button1 = Button(root , text = "Sign_up" , command = SIGNUP)
button2 = Button(root , text = "Login" , command = LOGIN)
button1.pack()
button2.pack()
root.mainloop()
