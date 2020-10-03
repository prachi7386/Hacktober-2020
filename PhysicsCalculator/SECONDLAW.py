def SecondLawOfMotion():
    print """Based on Second Law,what would you like to calculate?
              1)Acceleration
              2)Force
              3)Mass
              4)Momentum"""
    choice1=int(raw_input("Enter your choice:"))
    if choice1==1:
        print "ACCELERATION."
        force=float(raw_input("Enter force:"))
        mass=float(raw_input("Enter mass:"))
        accel=force/mass
        print "FORMULA USED: Acceleration=Force/Mass"
        print "The acceleration is=",accel
    if choice1==2:
        print "FORCE."
        mass=float(raw_input("Enter mass:"))
        accel=float(raw_input("Enter acceleration:"))
        force=mass*accel
        print "FORMULA USED: Force=Mass*Acceleration"
        print "The force is=",force
    if choice1==3:
        print "MASS."
        accel=float(raw_input("Enter acceleration:"))
        force=float(raw_input("Enter force:"))
        mass=force/accel
        print "FORMULA USED: Mass=Force/Acceleration"
        print "The mass is=",mass
    if choice1==4:
        print "MOMENTUM."
        mass=float(raw_input("Enter mass:"))
        velocity=float(raw_input("Enter velocity:"))
        momentum=mass*velocity
        print "FORMULA USED: Momentum=Mass*Velocity"
        print "The momentum is=",momentum

        
        
            
              
