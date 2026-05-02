n=int(input("enter the number of rows"))
for i in list(range(1,n+1))+list(range(n-1,0,-1)):
    print(" "*(n-i) + " ".join(str(j) for j in range(1,i+1)))