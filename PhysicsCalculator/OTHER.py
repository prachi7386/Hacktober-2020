def othersolidprop():
    print "You have chosen to calculate other solid properties."
    print """What would you like to calculate?
             1)Compressibility
             2)Elastic Potenial Energy
             3)Poisson's Ratio"""
    choice1=int(raw_input("Enter your choice(NUMBER)."))
    if choice1==1:
        print "You have chosen to calculate Compressibility."
        bmodu=float(raw_input("Enter the Bulk's Modulus:"))
        compr=1/bmodu
        print "FORMULA: Compressiblity= 1/Bulk's Modulus"
        print "Compressibilty=",compr
    elif choice1==2:
        print "You have chosen to calculate Elastic Potential Energy."
        ymodulus1=float(raw_input("Enter the Young's Modulus:"))
        strain1=float(raw_input("Enter the strain:"))
        ymodulus=(1/2)*ymodulus1
        strain=(strain1)**2
        epe=ymodulus/strain
        print "FORMULA: Elastic Potential Energy=1/2 * Young's Modulus/Strain^^2 "
        print "Elastic Potential Energy=",epe
    elif choice1==3:
        print "You have chosen to calculate Poisson's Ratio."
        lastrain=float(raw_input("Enter the Lateral Strain:"))
        lostrain=float(raw_input("Enter the Longitudinal Strain:"))
        poratio=lastrain/lostrain
        print "FORMULA: Poisson's Ratio= Lateral Strain/Longitudinal Strain"
        print "Poisson's Ratio=",poratio
    else:
        print "ERROR: The choice of calculation doesn't exist."










        
        
