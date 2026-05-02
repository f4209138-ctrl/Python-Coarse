print("Pyramid of stars")
n = int(input("Enter the numbers of rows:"))
for i in range(n):
    for j in range(i+1):
        print("*", end=" ")
    print()