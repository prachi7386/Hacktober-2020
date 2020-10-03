s=input("Enter the string :")

l=[]

for i in range(len(s)):

    l.append([0]*len(s))
    l[i][i]=1
    
print(l)


for i in range(len(s)):
    for j in range(len(s)):
        
