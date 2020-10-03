from Tkinter import *


    
    
def t2014():
    def nextt():
        master = Toplevel()
        photo1 = PhotoImage(file = '2.gif')
        label1 = Label(master , image = photo1)
        label1.pack()
        master.mainloop()
        
        
    root = Toplevel()
    photo = PhotoImage(file = '1.gif')
    button = Button(root,text = 'next' ,command = nextt)
    button.pack()
    label = Label(root , image = photo)
    label.pack()
    root.mainloop()

def t2015():
    def nextt():
        master = Toplevel()
        photo1 = PhotoImage(file = '4.gif')
        label1 = Label(master , image = photo1)
        label1.pack()
        master.mainloop()
        
        
    root = Toplevel()
    photo = PhotoImage(file = '3.gif')
    button = Button(root,text = 'next' ,command = nextt)
    button.pack()
    label = Label(root , image = photo)
    label.pack()
    root.mainloop()

def t2016():
    
    def nextt():
        master = Toplevel()
        photo1 = PhotoImage(file = '6.gif')
        label1 = Label(master , image = photo1)
        label1.pack()
        master.mainloop()
        
        
        
    root = Toplevel()
    photo = PhotoImage(file = '5.gif')
    button = Button(root,text = 'next' ,command = nextt)
    button.pack()
    label = Label(root , image = photo)
    label.pack()
    root.mainloop()
    
def confirm():
    l = [t2014,t2015,t2016]
    l1 = [2014,2015,2016]
    value =  entry1.get()
    for i in range(len(l)):
        if int(value)== l1[i]:
            l[i]()
            
            

        
root1 = Tk()
label1 = Label(root1 , text = "Enter the year (2014/2015/2016)")
entry1 = Entry(root1)
label1.grid(row = 0 , column = 1)
entry1.grid(row = 0 , column = 2)
button1 = Button(root1 , text = "Enter" , command = confirm)
button1.grid(columnspan = 2)
root1.mainloop()


    



