try:
    num1, num2 = eval(input("Enter two numbers: "))
    result = num1 / num2
    print(result)
except ZeroDivisionError:
    print("Divison by zero is error.")
except SyntaxError:
    print("Syntax error.")   
except Exception: 
    print("Wrong input.")
else:
    print("No exception")
finally:
    print("This will always execute.")