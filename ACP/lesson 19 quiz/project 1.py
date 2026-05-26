def add(x,y):
    return x+y
def subtract (x,y):
    return x-y
def multiply(x,y):
    return x*y
def divide(x,y):
    return x/y
def calculator():
    print("The calculator")
    print("Operations= +,-,*,/")

try:
 choice= input("Enter operation:")
 num1=float(input("Enter a number:"))
 num2=float(input("Enter a number:"))
 if choice =="+":
            print(num1+num2)
 elif choice =="-":
            print(num1-num2)
 elif choice =="*":
            print(num1*num2)
 elif choice =="/":
            print(num1/num2)
except ZeroDivisionError:
       print("Cannot be divided by zero")
calculator()
            