from Tkinter import *

def key4():
    if var4.get() == 1:
        print "correct"
    else:
        print "False"
    
def key5():
    if var5.get() == 1:
        print "correct"
    else:
        print "False"
    
def key6():
    if var6.get() == 1:
        print "correct"
    else:
        print "False"
root = Tk()
label4 = Label(root , text = " 4.If the flux of the electric field through a closed surface is zero..")
var4 = IntVar()
button14 = Checkbutton(root , text = "The electric field must be zero everywhere on the surface ", command = key4)
button14.place(relx =.13 , rely =.15 , anchor = "c" )
button15 = Checkbutton(root , text = "The electric field may be zero everywhere on the surface", variable = var4, command = key4)
button15.place(relx =.125 , rely =.20 , anchor = "c" )
button16 = Checkbutton(root , text = "The charge inside the surface must be zero", command = key4)
button16.place(relx =.1 , rely =.25 , anchor = "c")
button17 = Checkbutton(root , text = "The charge in the vicinity of the surface must be zero", command = key4)
button17.place(relx =.12 , rely =.30 , anchor = "c")
label4.place(relx =.12 , rely =.1 , anchor = "c")

label5 = Label(root , text = " 5.An electric dipole is placed at the centre of the sphere..")
var5 = IntVar()
button18 = Checkbutton(root , text = "The flux of the electric field through the sphere is zero.", variable = var5, command = key5)
button18.place(relx =.12 , rely =.40 , anchor = "c" )
button19 = Checkbutton(root , text = "The electric filed is zero at every point of the sphere", command = key5)
button19.place(relx =.115, rely =.45 , anchor = "c")
button20 = Checkbutton(root , text = "The electric field is not zero anywhere on the sphere.", command = key5)
button20.place(relx =.115 , rely =.50 , anchor = "c")
button21 = Checkbutton(root , text = "The electric field is zero on a circle of the sphere", command = key5)
button21.place(relx =.105 , rely =.55 , anchor = "c")
label5.place(relx =.11 , rely =.35 , anchor = "c")

label6 = Label(root , text = " 6.A positive point charge q is bought near an isolated metal cube ..")
var6 = IntVar()
button22 = Checkbutton(root , text = "The cube becomes negatively charged", command = key6)
button22.place(relx =.09 , rely =.65 , anchor = "c")
button23 = Checkbutton(root , text = "The cube becomes positively charged", command = key6)
button23.place(relx =.09, rely =.70 , anchor = "c")
button24 = Checkbutton(root , text = "The interior becomes positively charged and the surface becomes negatively charged", variable = var6, command = key6)
button24.place(relx =.18, rely =.75 , anchor = "c" )
button25 = Checkbutton(root , text = "The interior remains charge free and the surface gets non-uniform charge distribution.", command = key6)
button25.place(relx =.18, rely =.80 , anchor = "c")
label6.place(relx =.13 , rely =.60 , anchor = "c")

root.mainloop()
