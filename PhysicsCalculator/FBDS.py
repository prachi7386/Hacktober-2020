#Python program for FBD's of blocks attached by string one below the other
def two_blocks(m1,m2):
    g=10
    t=(m2*g)
    t1=(m1*g)+t
    return t1,"N",t,"N"
 #and
#to calculate the acceleration of the block
def acc_blocks(a,b):
    g=10
    acc1=(g*(2*a-b))/(4*a+b)
    acc2=2*acc1
    return acc1,acc2
def lift():
#to calculate the tension of bob in a moving lift
    m=float(raw_input("Enter the mass of the bob"))
    n=int(raw_input(" 1.Is the lift is moving up,\n 2.Or is the lift  moving down"))
    acc=float(raw_input("Enter the acc of the lift"))
    g=10
    if n==1 and acc>0:
        t=m*(g+acc)
        return t
    elif  n==2 and acc>0:
         t=m*(g-acc)
         return t
print(" Press 1 for Tension related problem\n Press 2 for Acceleration of the blocks\n Press 3 for Lift based problems")
choice=int(raw_input(""))
if(choice==2):
    a=float(raw_input("Enter the mass of heavier block"))
    b=float(raw_input("Enter the mass of lighter block"))
    result=acc_blocks(a,b)
    print "The acceleration of the blocks are",result
if(choice==1):
    m1=float(raw_input("Enter the mass of one block :"))
    m2=float(raw_input("Enter the mass of the second block :"))
    print "The two tensions are",two_blocks(m1,m2)
if(choice==3):
    tension=lift()
    print "The value of Tension is",tension
   
    
    
    
    
