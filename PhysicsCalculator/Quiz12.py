from Tkinter import *
def key1():
    if var1.get() == 1:
        print "correct"
    else:
        print "False"
        
def key2():
    if var2.get() == 1:
        print "correct"
    else:
        print "False"
        
def key3():
    if var3.get() == 1:
        print "correct"
    else:
        print "False"


root = Tk()

label1 = Label(root , text = " 1.When the seperation between two charges is increased , the electric potential energy of the charges..")
var1 = IntVar()
button1 = Checkbutton(root , text = "Increases", command = key1)
button1.place(relx =.1 , rely =.15 , anchor = "c" )
button2 = Checkbutton(root , text = "Decreases" ,variable=var1 , command = key1)
button2.place(relx =.1 , rely =.20 , anchor = "c" )
button3 = Checkbutton(root , text = "Same", command = key1)
button3.place(relx =.09 , rely =.25 , anchor = "c")
button4 = Checkbutton(root , text = "May increase or decrease", command = key1)
button4.place(relx =.1255 , rely =.30 , anchor = "c")
label1.place(relx =.2 , rely =.1 , anchor = "c")

label2 = Label(root , text = " 2.An electric dipole is placed in a uniform electric field. The net electric force on the dipole is ....")
var2 = IntVar()
button5 = Checkbutton(root , text = "always zero", variable=var2, command = key2)
button5.place(relx =.1 , rely =.40 , anchor = "c" )
button6 = Checkbutton(root , text = "Depends on orientation of dipole", command = key2)
button6.place(relx =.14, rely =.45 , anchor = "c")
button7 = Checkbutton(root , text = "Can never be zero", command = key2)
button7.place(relx =.11 , rely =.50 , anchor = "c")
button8 = Checkbutton(root , text = "Depends on the strength of the dipole", command = key2)
button8.place(relx =.15 , rely =.55 , anchor = "c")
label2.place(relx =.19 , rely =.35 , anchor = "c")

label3 = Label(root , text = " 3.If a body is charged by rubbing it then it's weight..")
var3 = IntVar()
button9 = Checkbutton(root , text = "remains precisely constant", command = key3)
button9.place(relx =.13 , rely =.65 , anchor = "c")
button10 = Checkbutton(root , text = "Increases slightly", command = key3)
button10.place(relx =.11, rely =.70 , anchor = "c")
button11 = Checkbutton(root , text = "Decreases slightly", command = key3)
button11.place(relx =.11 , rely =.75 , anchor = "c")
button12 = Checkbutton(root , text = "May increase or decrease slightly", variable=var3 , command = key3)
button12.place(relx =.14, rely =.80 , anchor = "c")
label3.place(relx =.1 , rely =.60 , anchor = "c")


root.mainloop()

import Q2



    
