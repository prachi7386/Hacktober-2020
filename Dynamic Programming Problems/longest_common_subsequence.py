
a=input("Enter the longest subsequence :")

b=input("Enter the shorter subsequence :")

la=list(a)

lb=list(b)

l=[]

for i in range(len(lb)+1):
    l.append([0]*(len(la)+1))



for i in range(1,len(lb)+1):

    for j in range(1,len(la)+1):

        if(lb[i-1]==la[j-1]):
            l[i][j]=l[i-1][j-1]+1

        else:
            l[i][j]=max(l[i-1][j],l[i][j-1])

print(l)


temp=l[len(lb)][len(la)]

c=0
p=len(la)

i=len(lb)

while(i!=0):

    if(l[i][p]==l[i-1][p]):
        i=i-1
    elif(l[i][p]==l[i][p-1]):
        p=p-1
    else:
        p=p-1
        c=c+1
        i=i-1
print("The longest common subsequence is of length :",c)


        
        
    
