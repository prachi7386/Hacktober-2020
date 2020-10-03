# 0 1 1 2 3 5 8



a=0
b=1
n=int(input())

if(n==1 or n==2):
    if(n==1):
        print(a)
    else:
        print(b)
else:
    for i in range(n-1):
        c=a+b
        a,b=b,c
    print(c)
    
