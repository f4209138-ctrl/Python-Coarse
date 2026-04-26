decimal_number= int(input("Enter a number:"))
binary_string= ""
if decimal_number == 0:
    binary_string:"0"
else:
    while decimal_number > 0:
        remainder = decimal_number % 2
        binary_string = str(remainder)+ binary_string
        decimal_number = decimal_number//2
print("The binary number is:",binary_string)