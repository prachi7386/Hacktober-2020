#Creating a function of Horizontal projectile motion.
def  Horizontal():
    print "You have chosen horizontal projection"
    print "What would you like to find:"
    print """ 1. Time of flight
2. Maximum horizontal range
3. Velocity at any point """
    ch=int(raw_input("Enter your choice:"))
    if ch==1:
        height=float(raw_input("Enter the horizontal height(H):"))
        print " Now by using the formula..... T=[2*(H)/g]**0.5" # ** indicates to the power, and 'g' indicates force of gravity (9.8 m/s**2), T is time of flight.
        T=((2*height)/9.8)**0.5
        print " The Time of flight is:",T
    if ch==2:
        initial=float(raw_input("Enter the initial velocity of the projectile(U):"))
        height=float(raw_input("Enter the horizontal height(H):"))
        print " Now by using the formula......R=u*[2*(H)/g]**0.5" # ** indicates to the power, and 'g' indicates force of gravity (9.8 m/s**2), R is the maximum horizontal range.
        R= initial*(2*(height)/9.8)**0.5
        print " The Horizontal range is :",R
    if ch==3:
        initial=float(raw_input("Enter the initial velocity of the projectile(U):"))
        Time=float(raw_input("Enter the time taken(T):"))
        print " Now by using the formula....V=[U**2 + (g*T)**2]**0.5" # ** indicates to the power, and 'g' indicates force of gravity (9.8 m/s**2), T is time of filght , U is the initial velocity.
        V=(initial**2 + (9.8*Time)**2)**0.5 # V is the Velocity at that point
        print "The velocity at that point is:",V

            
            
            
            
            
        

