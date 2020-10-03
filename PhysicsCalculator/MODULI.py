def modulus():
    print "You have chosen to calculate elastic moduli."
    print """What would you like to calculate?
             1)Young's Modulus
             2)Bulk's Modulus
             3)Shear Modulus"""
    choice1=int(raw_input("Enter your choice(NUMBER)."))
    if choice1==1:
        print "You have chosen to calculate Young's Modulus."
        ystress=float(raw_input("Enter the stress:"))
        ystrain=float(raw_input("Enter the longitudinal strain:"))
        ymodulus=ystress/ystrain
        print "FORMULA: Young's Modulus= Stress/Longitudinal Strain"
        print "Young's Modulus=",ymodulus
    elif choice1==2:
        print "You have chosen to calculate Bulk's Modulus."
        bstress=float(raw_input("Enter the stress:"))
        bstrain=float(raw_input("Enter the volumetric strain:"))
        bmodulus=bstress/bstrain
        print "FORMULA: Bulk's Modulus= Stress/Volumetric Strain"
        print "Bulk's Modulus=",bmodulus
    elif choice1==3:
        print "You have chosen to calculate Shear's Modulus."
        shstress=float(raw_input("Enter the tangential stress:"))
        shstrain=float(raw_input("Enter the shear strain:"))
        shmodulus=shstress/shstrain
        print "FORMULA: Bulk's Modulus= Tangential Stress/Shear Strain"
        print "Shear Modulus=",shmodulus
    else:
        print "ERROR: Choice of calculation doesn't exist."
     

    
    
    
