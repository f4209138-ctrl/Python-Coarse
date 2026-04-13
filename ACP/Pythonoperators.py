c = input("Input a charecter: ")
if len(c) == 1:
    v = ord(c)
    if 65 <= v <= 90: 
        t = "Upper-Case"
    elif 97 <= v <= 122: 
        t = "Lower-Case"
    elif 48 <= v <= 57: 
        t = "Digit"
    elif v == 32: 
        t = "Space"
    else: 
        t = "Special"
print("The value of",c,"is",v,"and the type of",c,"is",t)