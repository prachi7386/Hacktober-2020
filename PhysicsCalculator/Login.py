
from Tkinter import *

def confirm():
    try:
        fr = open(entry1.get()+".txt" , "r")
    except IOError:
        print "There is no username existing."
    else:
        check = fr.read()
        if check == entry2.get():
            print "Successfully loged in."
            import Main
        else:
            print "Enter valid password."

    
root = Tk()

label1 = Label(root , text = "Username")
label2 = Label(root , text = "Password")
entry1 = Entry(root)
entry2 = Entry(root)
button1 = Button(root , text = "Login" , command = confirm)
label1.grid(row = 0 , column = 1)
label2.grid(row = 1 , column = 1)
entry1.grid(row = 0 , column = 2)
entry2.grid(row = 1 , column = 2)
button1.grid(columnspan = 2)

root.mainloop()

