#Creating a module for Vertical projectile motion
def Angular():
    import math
    print "You have chosen Angular projectile motion"
    print "What would you like to find:"
    print """ 1. Time of filght
2. Horizonatal range
3.Maximum height"""
    ch=int(raw_input("Enter your choice:"))
    if ch==1:
        initial=float(raw_input("Enter the initial velocity(U):"))
        angle=float(raw_input("Enter the angle of projectile:"))
        print "By using the formula... T=2*U*sin(angle)/g" # where T is the time of flight , 'g' is the force of gravity(9.8m/s**2) , U is the initial velocity.
        T=(2*initial*math.sin(math.radians(angle)))/9.8
        print "Time of flight of the projectile is:",T
    elif ch==2:
        initial=float(raw_input("Enter the initial velocity of the projectile(U):"))
        angle=float(raw_input("Enter the angle of the projectile:"))
        print " By using the formula.... R=U*cos(angle)*2*U*sin(angle)/g" # where R is the horizontal range , U is the initial velocity , 'g' is the force of gratvity.
        R=(initial*math.cos(math.radians(angle))*2*initial*math.sin(angle))/9.8
        print " The horizontal range is:",R
    elif ch==3:
        initial=float(raw_input("Enter the initial velocity of the projectile(U):"))
        angle=float(raw_input("Enter the angle of the projectile:"))
        print "By using the formula... H=U**2*sin(angle)**2/2g" # where H is the horizontal range , U is the initial velocity of the projectile.
        H=((initial**2)*(math.sin(math.radians(angle))**2))/19.6
        print "The horizontal range is:",H




