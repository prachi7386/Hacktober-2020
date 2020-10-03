l=list(map(int,input("Enter the elements in subset:").split()))
l.sort()

s=int(input("Enter the sum to be obtained :"))


total=0
temp=[[0 for i in range(s+1)]  for i in range(len(l)+1)]
temp[0][0]=1

for i in range(1,len(temp)):
  
    total=total+i
    t=l[i-1]
    for j in range(0,s+1):
        
        if(j<t):
            temp[i][j]=temp[i-1][j]

        else:
            if(temp[i-1][j]==1):
                temp[i][j]=1
            else:
                temp[i][j]=temp[i-1][j-t]


for i in range(0,len(temp)):
    for j in range(len(temp[i])):
        print(temp[i][j],end=" ")
    print("")

if(temp[len(l)-1][s]==1):
    print("There is a subset")
else:
     print("There is no subset")
