def add(a,b):
    return a + b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    if b==0:
        return("0 is not Dividable.")
    return a / b
print("Select Operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
choice= input("Enter Choice 1-2-3-4:")
num1=float(input("Enter first number:"))
num2=float(input("Enter second number:"))
if choice == '1':
    print("Result is",add(num1,num2))
elif choice == '2':
    print("Result is",subtract(num1,num2))
elif choice == '3':
    print("Result is",multiply(num1,num2))
elif choice == '4':
    print("Result is",divide(num1,num2))
else:
    print("Invalid input")