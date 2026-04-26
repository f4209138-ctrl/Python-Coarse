num = input("Enter a number:")
if len(num)<3:
    print("The number is short ")
else:
    mdigit= num[1:-1]
    product = 1
    for digit in mdigit:
        product = product * int(digit)
        print("The middle digits are:",mdigit)
        print("The product of these digits is:",product)