#OPENING TKINTER WINDOW FROM ANOTHER CLASS USING INHERITANCE
from Tkinter import *
class Information(object):
    def info1(self):
        root1=Tk()
        self.label= Label(root1, text='''Chapter_1: Physical World

Physics _ scope and excitement; nature of physical laws; Physics, technology and society.

Chapter_2: Units and Measurements

Need for measurement: Units of measurement; systems of units; SI units, fundamental and derived units. Length, mass and time measurements; accuracy and precision of measuring instruments; errors in measurement; significant figures.

Dimensions of physical quantities, dimensional analysis and its applications.''',justify="center")
        self.label.place(x=20,y=40)
        self.weight=Label(root1,text="Weightage        3",font=("Helvetica",14))
        self.weight.pack()
        root1.mainloop()
    def info2(self):
        root2=Tk()
        self.label=Label(root2,text='''Frame of reference, Motion in a straight line: Position-time graph, speed and velocity.

Elementary concepts of differentiation and integration for describing motion.Uniform and non-uniform motion, average speed and instantaneous velocity. Uniformly accelerated motion, velocity time and position-time graphs.

Relations for uniformly accelerated motion (graphical treatment).''',justify="center")
        self.label.place(x=20,y=40)
        self.weight=Label(root2,text="Weightage        10",font=("Helvetica",14))
        self.weight.pack()
        root2.mainloop()
    def info3(self):
        root3=Tk()
        self.label=Label(root3,text='''Intuitive concept of force. Inertia, Newton's first law of motion; momentum and Newton's second law of motion; impulse; Newton's third law of motion.

Law of conservation of linear momentum and its applications.

Equilibrium of concurrent forces. Static and kinetic friction, laws of friction, rolling friction, lubrication.

Dynamics of uniform circular motion: Centripetal force, examples of circular motion (vehicle on a level circular road, vehicle on banked road).''',justify="center")
        self.label.place(x=20,y=40)
        self.weight=Label(root3,text="Weightage        10",font=("Helvetica",14))
        self.weight.pack()
        root3.mainloop()
    def info4(self):
        root4=Tk()
        self.label=Label(root4,text='''Work done by a constant force and a variable force; kinetic energy, work-energy theorem, power.

Notion of potential energy, potential energy of a spring, conservative forces: conservation of mechanical energy (kinetic and potential energies); non-conservative forces: motion in a vertical circle; elastic and inelastic collisions in one and two dimensions.''',justify="center")
        self.label.place(x=20,y=40)
        self.weight=Label(root4,text="Weightage        6",font=("Helvetica",14))
        self.weight.pack()
        root4.mainloop()
    def info5(self):
        root5=Tk()
        self.label=Label(root5,text='''Centre of mass of a two-particle system, momentum conservation and centre of mass motion. 

Centre of mass of a rigid body; centre of mass of a uniform rod.

Moment of a force, torque, angular momentum, laws of conservation of angular momentum and its applications.

Equilibrium of rigid bodies, rigid body rotation and equations of rotational motion, comparison of linear and rotational motions.

Moment of inertia, radius of gyration.Values of moments of inertia, for simple geometrical objects (no derivation). Statement of parallel and perpendicular axes theorems and their applications.''',justify="center")
        self.label.place(x=20,y=40)
        self.weight=Label(root5,text="Weightage        6",font=("Helvetica",14))
        self.weight.pack()
        root5.mainloop()
    def info6(self):
        root6=Tk()
        self.label=Label(root6,text='''Keplar's laws of planetary motion.The universal law of gravitation.

Acceleration due to gravity and its variation with altitude and depth.

Gravitational potential energy and gravitational potential. Escape velocity. Orbital velocity of a satellite. Geo-stationary satellites.''',justify="center")
        self.label.place(x=20,y=40)
        self.weight=Label(root6,text="Weightage        5",font=("Helvetica",14))
        self.weight.pack()
        root6.mainloop()
    def info7(self):
        root7=Tk()
        self.label=Label(root7,text='''Chapter_9: Mechanical Properties of Solids

Elastic behaviour, Stress-strain relationship, Hooke's law, Young's modulus, bulk modulus, shear modulus of rigidity, Poisson's ratio; elastic energy.

Chapter_10: Mechanical Properties of Fluids

Pressure due to a fluid column; Pascal's law and its applications (hydraulic lift and hydraulic brakes). Effect of gravity on fluid pressure.

Viscosity, Stokes' law, terminal velocity, streamline and turbulent flow, critical velocity.Bernoulli's theorem and its applications.

Surface energy and surface tension, angle of contact, excess of pressure across a curved surface, application of surface tension ideas to drops, bubbles and capillary rise.

Chapter_11: Thermal Properties of Matter

Heat, temperature, thermal expansion; thermal expansion of solids, liquids and gases, anomalous expansion of water; specific heat capacity; Cp, Cv - calorimetry; change of state - latent heat capacity.

Heat transfer-conduction, convection and radiation, thermal conductivity, Qualitative ideas of Blackbody radiation, Wein's displacement Law, Stefan's law, Green house effect. ''',justify="center")
        self.label.place(x=20,y=40)
        self.weight=Label(root7,text="Weightage        10",font=("Helvetica",14))
        self.weight.pack()
        root7.mainloop()
    def info8(self):
        root8=Tk()
        self.label=Label(root8,text='''Thermal equilibrium and definition of temperature (zeroth law of thermodynamics).Heat, work and internal energy. First law of thermodynamics. Isothermal and adiabatic processes.

Second law of thermodynamics: reversible and irreversible processes. Heat engine and refrigerator.''',justify="center")
        self.label.place(x=20,y=40)
        self.weight=Label(root8,text="Weightage        5",font=("Helvetica",14))
        self.weight.pack()
        root8.mainloop()
    def info9(self):
        root9=Tk()
        self.label=Label(root9,text='''Equation of state of a perfect gas, work done in compressing a gas.
Kinetic theory of gases - assumptions, concept of pressure. Kinetic interpretation of temperature; rms speed of gas molecules; degrees of freedom, law of equi-partition of energy (statement only) and application to specific heat capacities of gases;
concept of mean free path, Avogadro's number.''')
        self.label.place(x=20,y=40)
        self.weight=Label(root9,text="Weightage        5",font=("Helvetica",14))
        self.weight.pack()
        root9.mainloop()
    def info10(self):
        root10=Tk()
        self.label=Label(root10,text='''Chapter_14: Oscillations

Periodic motion - time period, frequency, displacement as a function of time. Periodic functions.

Simple harmonic motion (S.H.M) and its equation; phase; oscillations of a spring-restoring force and force constant; energy in S.H.M. Kinetic and potential energies; simple pendulum derivation of expression for its time period.

Free, forced and damped oscillations (qualitative ideas only), resonance.

Chapter_15: Waves

Wave motion. Transverse and longitudinal waves, speed of wave motion. Displacement relation for a progressive wave. Principle of superposition of waves, reflection of waves, standing waves in strings and organ pipes, fundamental mode and harmonics,
Beats, Doppler effect.''')
        self.label.place(x=20,y=40)
        self.weight=Label(root10,text="Weightage        10",font=("Helvetica",14))
        self.weight.pack()
        root10.mainloop()        

#MAIN WINDOW

        
class MyFirstGUI(Information):
    def __init__(self, master):
        self.master = master
        master.title("Chapters")
        self.label = Label(master, text="PHYSICS CLASS 11 CHAPTERS",font=("Helvetica", 16))
        self.label.pack()

        self.label1= Label(master, text="1.Physical World and Measurement")
        self.label1.place(x=20,y=40)
        self.info_button1= Button(master, text="Info", command=self.info1)
        self.info_button1.place(x=600,y=40)
        
        self.label2 = Label(master, text="2.Kinematics")
        self.label2.place(x=20,y=60)
        self.info_button2= Button(master, text="Info", command=self.info2)
        self.info_button2.place(x=600,y=60)

        self.label3 = Label(master, text="3.Laws of Motion")
        self.label3.place(x=20,y=80)
        self.info_button3 = Button(master, text="Info", command=self.info3)
        self.info_button3.place(x=600,y=80)

        self.label4 = Label(master, text="4.Work, Energy and Power")
        self.label4.place(x=20,y=100)
        self.info_button4 = Button(master, text="Info", command=self.info4)
        self.info_button4.place(x=600,y=100)

        self.label5 = Label(master, text="5.Motion of System of Particles")
        self.label5.place(x=20,y=120)
        self.info_button5 = Button(master, text="Info", command=self.info5)
        self.info_button5.place(x=600,y=120)
        
        self.label6 = Label(master, text="6.Gravitation")
        self.label6.place(x=20,y=140)
        self.info_button6= Button(master, text="Info", command=self.info6)
        self.info_button6.place(x=600,y=140)

        self.label7 = Label(master, text="7.Properties of Bulk Matter")
        self.label7.place(x=20,y=160)
        self.info_button7 = Button(master, text="Info", command=self.info7)
        self.info_button7.place(x=600,y=160)

        self.label8 = Label(master, text="8.Thermodynamics")
        self.label8.place(x=20,y=180)
        self.info_button8 = Button(master, text="Info", command=self.info8)
        self.info_button8.place(x=600,y=180)

        self.label9 = Label(master, text="9.Kinetic Theory of Gases")
        self.label9.place(x=20,y=200)
        self.info_button9 = Button(master, text="Info", command=self.info9)
        self.info_button9.place(x=600,y=200)

        self.label10 = Label(master, text="10.Oscillation & Waves")
        self.label10.place(x=20,y=220)
        self.info_button10 = Button(master, text="Info", command=self.info10)
        self.info_button10.place(x=600,y=220)  
root = Tk()
my_gui = MyFirstGUI(root)
root.mainloop()

