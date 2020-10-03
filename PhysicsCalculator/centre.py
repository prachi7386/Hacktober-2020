#to calculate centre of mass on x and y plane.
def centre():
    mass=eval(raw_input("Enter the masses(in lists):"))
    x=eval(raw_input("Enter the x coordinates(in list):"))
    y=eval(raw_input("Enter the y coordinates(in list):"))
    length=len(mass)
    m=[]
    for a in range(0,length):
        m.insert(a,mass[a]*x[a])
    
    length=len(m)
    s=0
    for j in range(0,length):
        s=s+m[j]

    s1=0
    for k in range(0,length):
        s1=s1+mass[k]

    
    X=float((s))/float(s1)
    print "The x coordinate  centre of mass:",X
    l=[]
    for b in range(0,length):
        l.insert(b,mass[b]*y[b])
    
    length=len(l)
    s2=0
    for c in range(0,length):
        s2=s2+l[c]

    s3=0
    for o in range(0,length):
        s3=s3+mass[o]

    
    Y=float((s2))/float(s3)
    print "The y coordinate  centre of mass:",Y








    
    
    
    

