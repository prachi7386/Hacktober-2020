
weight=list(map(int,input("Enter the weights: ").split()))
val=list(map(int,input("Enter the values: ").split()))
tot_wt=int(input("Enter the total weight :"))

l=[]
d={}

for i in range(len(weight)):

    d[weight[i]]=val[i]
    l.append([0]*(tot_wt+1))


for i in range(len(weight)):

    for j in range(tot_wt+1):

        if(i==0):
            if(weight[i]<=j):
                l[i][j]=val[i]

        else:
            if(weight[i]>j):
                l[i][j]=l[i-1][j]
            else:
                l[i][j]=max(l[i-1][j],val[i]+l[i-1][j-weight[i]])


temp=l[len(weight)-1][tot_wt]
p=tot_wt
s=0

for i in range(len(weight)-1,-1,-1):
    

    if(i==0):
        break

    elif(temp==l[i-1][p]):
        temp=l[i-1][p]

    else:
        p=p-weight[i]
        s=s+val[i]
        temp=l[i-1][p]
        

print("The maximum value for the given weight is : ",s)
 


    
                
