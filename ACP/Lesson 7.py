a = int(input("Enter the first number to be replaced:"))
b = int(input("Enter the second number to be replaced:"))
c = int(input("Enter the third number to be replaced:"))
print("NOTE:THE FIRST NUMBER WILL BE REPLACE WITH THE THIRD NUMBER,THE SECOND NUMBER WILL BE REPLACED WITH FIRST AND THE THIRD ONE WILL BE REPLACED WITH THE SECOND ONE.")
a, b, c = c, a, b
print(a,b,c)