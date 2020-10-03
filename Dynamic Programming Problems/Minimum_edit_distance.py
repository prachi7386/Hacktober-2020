a=list(input("Enter the first string :"))
b=list(input("Enter the second string :"))
l=[]

for i in range(len(b)+1):
    l.append([0]*(len(a)+1))
    l[i][0]=i
    l[0][i]=i


l[0][len(l[0])-1]=len(a)

for i in range(len(b)+1):

    for j in range(len(a)+1):

        print(l[i][j],end=" ")
    print(" ")


print(" ")
print(" ")
    
for i in range(1,len(b)+1):

    for j in range(1,len(a)+1):

        if(b[i-1]==a[j-1]):
            l[i][j]=l[i-1][j-1]

        else:
            l[i][j]=min(l[i-1][j-1],l[i][j-1],l[i-1][j])+1

for i in range(len(b)+1):

    for j in range(len(a)+1):

        print(l[i][j],end=" ")
    print(" ")

print("The minimum no of edits is :",l[len(b)][len(a)])

