try:
    age=int(input("Enter your age: "))
    if age<0:
        print("Age cannot be negative.")
    elif age%2==0:
        print("Your age is even.")
    else:
        print("Your age is odd.")
except ValueError as ex:
    print("Exception",ex)