def stress():  #Stress Module
    print "You have chosen to calculate stress."
    print "FORMULA: Stress=Force/Area"
    choice=int(raw_input("Type 1 for SI units and 2 for CGS units."))
    force=float(raw_input("Enter the force:"))
    area=float(raw_input("Enter the area:"))
    stress=force/area
    if choice==1:
        print "The stress =",stress,"N/m^^2"
    elif choice==2:
        print "The stress =",stress,"dyne/cm^^2"
    else:
        print "ERROR:Choice of units doesn't exist." 
    
