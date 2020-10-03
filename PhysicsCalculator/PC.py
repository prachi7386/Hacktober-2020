import centre
import MODULI
import OTHER
import STRAIN
import STRESS
import Angular
import Horizontal
import SECONDLAW
import Vector
i=True
while i==True:
    print "What would you like to do ,User:"
    print """1) Centre of Mass
2) Free body diagram
3) Modulus
4) Projectile Motion
5) Secondary law of motion
6) Vector """
    choice=int(raw_input("What would you like to do ?:"))
    if choice==1:
        centre.centre()
    elif choice==2:
        import FBDS
    elif choice==3:
        print "What would you like to find ?"
        print """1) Modulus
2) Strain
3) Stress
4) Solid prop """
        option2=int(raw_input("Enter your choice:"))
        if option2==1:
            MODULI.modulus()
        elif option2==2:
            STRAIN.strain()
        elif option2==3:
            STRESS.stress()
        else:
            OTHER.othersolidprop()
    elif choice==4:
        print "What would you like to find ?"
        print """1) Angular projectile motion.
2) Linear projectile motion """
        choice3=int(raw_input("Enter your choice:"))
        if choice3==1:
            Angular.Angular()
        else:
            Horizontal.Horizontal()
    elif choice==5:
        SECONDLAW.SecondLawOfMotion()
    elif choice==6:
        Vector.vector()
    want=raw_input("Do you want to continue (Yes/no):")
    if want=="no":
            break                                                         
else:
    print "Please Re-run the program."
