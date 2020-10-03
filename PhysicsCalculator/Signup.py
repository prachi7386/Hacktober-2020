
from Tkinter import *

def check():
    fw = open(entry1.get()+".txt" , "w")
    if entry2.get().isalnum() == False:
        if entry3.get() == entry2.get():
            fw.write(entry2.get())
            print "Successfully created."
        else:
            print "Re_password is not matching the password"
    else:
        print "The password should contain alphabets , digits and special characters."

    
root = Tk()
label1 = Label(root , text = "Username")
label2 = Label(root , text = "Password")
label3 = Label(root , text = "Re_enter_Password")
entry1 = Entry(root)
entry2 = Entry(root)
entry3 = Entry(root)
button1 = Button(root , text = "Create" , command = check)
label1.grid(row = 0 , column = 1)
label2.grid(row = 1 , column = 1)
label3.grid(row = 2 , column = 1)
entry1.grid(row = 0 , column = 2)
entry2.grid(row = 1 , column = 2)
entry3.grid(row = 2 , column = 2)
button1.grid(columnspan = 2)
root.mainloop()

        
    
