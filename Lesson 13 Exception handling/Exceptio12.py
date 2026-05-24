try:
    number=int(input("Enter a number: "))
    print("The Number entered is:",number)
except ValueError as ex:
    print("Exception",ex)