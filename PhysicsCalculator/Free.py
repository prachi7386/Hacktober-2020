#python program for FBD's of blocks attached by string one below the other
def two_blocks(m1,m2):
    g=10
    t=(m2*g)
    t1=(m1*g)+t
    return t1,"N",t,"N"

    
m1=float(raw_input("enter the mass of one block"))
m2=float(raw_input("enter the mass of the second block"))
print "the two tensions are",two_blocks(m1,m2)




                  #and
#to calculate the acceleration of the block
def acc_blocks(a,b):
    g=10
    acc1=(g*(2*a-b))/(4*a+b)
    acc2=2*acc1
    return acc1,acc2
    
    
    
    
a=float(raw_input("enter the mass of heavier block"))
b=float(raw_input("enter the mass of lighter block"))
result=acc_blocks(a,b)
print "the acceleration of the block is",result


#to calculate the tension of bob in a moving lift
m=float(raw_input("enter the mass of the bob"))
n=raw_input("enter the condition ")
acc=float(raw_input("enter the acc of thw lift"))
g=10
if n=="up" and acc>0:
    t=m*(g+acc)
    print "the tension is ",t
elif  n=="up" and acc<0:
    t=m*(g+acc)
    print "the tension is ",t
elif  n=="down" and acc>0:
     t=m*(g-acc)
     print "the tension is ",t
elif  n=="down" and acc<0:
    t=m*(g-acc)
    print "the tension is ",t
    

    

    
    

