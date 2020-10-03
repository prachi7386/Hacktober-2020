def quiz():
    import random
    for i in range(1,6):
        r=(random.randint(1,10))
        if r==1:
            print "A stone is thrown horizontally with a speed of (2gh)**0.5 from the top of wall of height h. It strikes the level ground through the foot of the wall at a distance x from the wall.What is the value of x?"
            print """1)3g/2
2)2h
3)7h
4)4h"""
            option1=int(raw_input("Enter your option:"))
            if option1==2:
                print "Correct"
            else:
                print "Wrong"
                print "Solution:"
                print """The time taken to fall through height h=(2g/h)**0.5
Now (2gh)**0.5 = x/(2h/g)**0.5) ; By solving the equation we get
x=2h"""
            print  " ______________________________________________________________________________________________________________________________________ "
        elif r==2:
            print "The maximum range of projectile is 2/(3)**0.5 times its actual range. What is the angle of projection for the actual range?"
            print """1)75
2)60
3)30
4)45"""
            option2=int(raw_input("Enter your option:"))
            if option2==3:
                print "Correct"
            else:
                print "Wrong"
                print "Solution:"
                print """ v**2/g = v**2 *sin2(angle)/g * 2/(3)**0.5
sin2(angle)=(3)**0.5/2
angle=60"""
            print "_______________________________________________________________________________________________________________________________________"            
        elif r==3:
            print "Find the depth of a lake for which the density of water will be 10% higher than the density at the surface. Compressiblity of water is 0.00005 per atmosphere. Given:average density of sea water=1100 kg m**-3"
            print """1)12 m
2)15 km
3)17 km
4)17 m"""
            option3=int(raw_input("Enter your choice:"))
            if option3==3:
                print "Correct"
            else:
                print "Wrong"
                print "Solution:"
                print """d=density ,  d=m/V   d'=m/V-v
d/d'=m/V * (V-v)/m
v/V = 1-d/d' = d'-d/d' = 10/110
B = 1/(5*10**-5 atm) = 1.01 * 10**5/d*10**-5 N m**-2
P=dgh
B=hdg/v/V = 1.01*10**5/ 5*10**-5 *1/11 * 1/1100*9.8
m=17 km"""        
            print "_______________________________________________________________________________________________________________________________________"
        elif r==4:
            print "What mass must be suspended from a steel wire 2m long and 1mm diameter to stretch it by 1mm? Givem: Young's modulus= 2*10**12 dyne cm**-2."
            print """ 1)8.009 kg
2) 17 kg
3) 8 g
4) 17 g """
            option4=int(raw_input("Enter your choice:"))
            if option4==1:
                print "Correct"
            else:
                print "Wrong"
                print "Solution:"
                print """ Y = (F*L)/(A*delta(L))
M = 2*10**12 * 22 * 0.05 *0.05*0.1/7*981*200 = 8.009 kg"""
            print "_______________________________________________________________________________________________________________________________________"
            
        elif r==5:
            print " Can the rectangular component of a vector be greater than the vector itself ?"
            option5=raw_input("Enter yes/no:")
            if option5=="yes":
                print "Correct"
            else:
                print "Wrong"
            print "_______________________________________________________________________________________________________________________________________"
        elif r==6:
            print "If the given components of a given vector are perpendicular to each other , then they are called ____________"
            option6=raw_input("Fill in the blank:")
            if option6 in "rectangular componens":
                print "Correct"
            else:
                print "False"
            print "_______________________________________________________________________________________________________________________________________"
        elif r==7:
            print "Two masses 8 kg and 12 kg are connected at the two ends of a frictionless pulley. Find the acceleration of the masses , and the tension in the string when the masses are released ?"
            print """1) 7 ms**-2 , 100 N
2)4 ms**-2 ,  87 N
3) 2 ms**-2 , 96 N
4) 3 ms**-2 , 79 N """
            option7=int(raw_input("Enter your choice:"))
            if option7==3:
                print "Correct"
            else:
                print "Wrong"
                print "Solution:"
                print """ a=(m1-m2)/(m1+m2) = 12-8/12+8 = 2 ms**-2
T = 2m1m2/m1+m2 = 2(12)(8)/12+8 = 96 N"""
            print "_______________________________________________________________________________________________________________________________________"
        elif r==8:
            print " The angle through which the outer edge is raised above the inner edge is called _______________"
            option8=raw_input("Fill in the blank:")
            if option8 in "angle of banking":
                print "Correct"
            else:
                print "Wrong"
            print "_______________________________________________________________________________________________________________________________________"
        elif r==9:
            print "70 kg man jumps to a height of a 0.8m . Find the impulse provided by ground to man ?"
            print """1) 318.9 kg
2)283.32 kg
3)121.32 kg
4)277.2 kg"""
            option9=int(raw_input("Enter your choice:"))
            if option9==4:
                print "Correct"
            else:
                print "Wrong"
                print "Solution:"
                print """ Impulse provided = Change in momentum of the person
m(vf-vi)=m((2gh)**0.5-0)
= 70*3.96 = 277.2 kgms**-1"""
            print "_______________________________________________________________________________________________________________________________________"
        elif r==10:
            print "The kinetic energy of a body is increased by 21% . What is the percentage increase in the linear momentum of the body ?"
            print """1)10%
2)12%
3)17%
4)7%"""
            option10=int(raw_input("Enter your choice:"))
            if option10==1:
                print "Correct"
            else:
                print "Wrong"
                print "Solution:"
                print """ Ek2=121*EKI/100
v2=11*v1/10 or m2v2=11/10*m*v1
p2=11*p1/10
p2-p1/p*100=1/10*100 = 10%"""
            print "_______________________________________________________________________________________________________________________________________"
            
            
            

        
             
            
            
    
        
        

                

            
        
                

                
