a = float(input("Enter your marks of english in decimal:"))
b = float(input("Enter your marks of hindi in decimal:"))
c= float(input("Enter your marks of maths in decimal:"))
d = float(input("Enter your marks of science in decimal:"))
e = float(input("Enter your marks of social science in decimal:"))
f = (a+b+c+d+e)
print("Your scored is:", f)
if f > 400:
    print("You have got an A, Congratulations")
elif f > 300:
    print("You have got a B, Great Job")
elif f > 200:
    print("You got a C, Good")
elif f > 100:
    print("You got a D, Great but you can improve")
else:
    print("You scored", f,"Try scoring more next time.")
