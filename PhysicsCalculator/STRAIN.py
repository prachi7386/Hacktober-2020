def strain():
    print "You have chosen to calculate strain."
    print """What would you like to calculate?
             1) Longitudinal Strain
             2) Volumetric Strain
             3) Lateral Strain"""
    choice1=int(raw_input("Enter your choice(NUMBER)."))
    if choice1==1:
        print "You have chosen to calculate Longitudinal strain."
        length=float(raw_input("Enter the length:"))
        changelength=float(raw_input("Enter the change in length:"))
        print "FORMULAE: Longitudinal Strain= change in length/original length"
        lstrain=changelength/length
        print "The longitudinal strain=",lstrain
    elif choice1==2:
        print "You have chosen to calculate Volumetric Strain."
        volume=float(raw_input("Enter the volume:"))
        changevolume=float(raw_input("Enter the change in volume:"))
        print "FORMULAE: Volumetric Strain= change in volume/original volume"
        vstrain=changevolume/volume
        print "The volumetric strain=",vstrain
    elif choice1==3:
        print "You have chosen to calculate Lateral Strain."
        laterallength=float(raw_input("Enter the lateral length:"))
        changelaterallength=float(raw_input("Enter the change in lateral length:"))
        print "FORMULAE: Lateral Strain= -(Change In Lateral Length/Lateral Length)"
        lateralstrain1=changelaterallength/laterallength
        lateralstrain=-(lateralstrain1)
        print "The lateral strain=",lateralstrain
    else:
        print "ERROR: Choice of calculation doesn't exist." 
























        
            
            
            
    
                
