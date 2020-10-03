from Tkinter import *
root=Tk()
def Fact1():
    print '''FACT NUMBER #1:
As Small as a Sugar Cube
Atoms have 99.9999999999999 per cent empty space. If you force all the atoms jointly, eradicating the space between them, grinding them down so the all those vast empty cathedrals would compressed into the small nuclei, a single teaspoon or sugar cube of the resulting mass would weigh five billion tons; about ten times the weight of all the humans who are currently alive.'''
def Fact2():
    print '''FACT NUMBER #2:
The Inconsistent Light
We are always told to be as fast as light. Well here is answer for all those who hate being told that. Light travels fast only in a vacuum. It is slowed whenever it passes through something, being measured as traveling as slowly as just 38 miles per hour at absolute zero (-273.15C) through ultra-cooled rubidium.'''
def Fact3():
    print '''FACT NUMBER #3:
The Mysterious Question
Despite all the advances made in astrophysics in recent years, we dont know what makes up the majority of the universe. The possible to make reasonable estimates of the mass of the universe, except the visible matter (stars, planets, stellar objects) only accounts for 2% of that;what exactly makes up the rest-so- called 'dark matter' and 'dark energy' remains a mystery'''
def Fact4():
    print '''FACT NUMBER #4:
The Smart Swimmer
One of the most amazing & interesting fact about Physics on earth is The Dead Sea which is known for its density due to the presence of salt, as a result of which you can easily float on it without drowning, so one can always claim to be a swimmer there.'''
def Fact5():
    print '''FACT NUMBER #5:
Ultimate expansion:
It is proved by scientific theories that the universe is constantly expanding. It is expanding at a decent pace and it is believed that galaxies will evaporate in the coming 10^19 to 10^20 years. It has been learnt from a number of theories by different Physicists worldwide that only White Dwarfs (a type of star) would be able to survive as their lifetime is more than 10^32 years.'''
l1=Label(root,text="PHYSICS FACTS!",fg="blue",cursor="dot",bg="pink")
b=Button(root,text="Fact Number 1",activebackground="green",fg='blue',bg='yellow',command=Fact1)
b1=Button(root,text="Fact Number 2",activebackground="green",fg='blue',bg='yellow',command=Fact2)
b2=Button(root,text="Fact Number 3",activebackground="green",fg='blue',bg='yellow',command=Fact3)
b3=Button(root,text="Fact Number 4",activebackground="green",fg='blue',bg='yellow',command=Fact4)
b4=Button(root,text="Fact Number 5",activebackground="green",fg='blue',bg='yellow',command=Fact5)
l1.pack()
b.pack()
b1.pack()
b2.pack()
b3.pack()
b4.pack()
root.mainloop()
