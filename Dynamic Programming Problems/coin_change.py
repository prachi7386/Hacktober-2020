N=int(input("Enter the total required :"))

coins=list(map(int,input().split()))

m=len(coins) #no of coins in the array

table = [[0 for x in range(N+1)] for y in range(m+1)]

for i in range(0,m+1):
	table[i][0]=1

for i in range(1,len(coins)+1):
    for j in range(1,N+1):                

        if(j>=coins[i-1]):
            table[i][j]=table[i-1][j] + table[i][j-coins[i-1]]

        else:
            table[i][j]=table[i-1][j]

print("The number of ways is :",table[m][N])
