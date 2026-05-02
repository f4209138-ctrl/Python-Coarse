n=int(input("Enter a number:"))
for i in range(1,n+1):
    print(""*(n-i),end="")
    for j in range (1,0,i+1):
        print(j,end="")
    print()
for i in range (n-1,0,-1):
    print(" "*(n-1),end="")
    for j in range(n,i+1):
        print(j,end=" ")
    print()
