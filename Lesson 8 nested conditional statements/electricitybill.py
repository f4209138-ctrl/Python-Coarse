units = int(input("PLease enter the units consumed:"))
if(units < 50):
    amount = units * 2.60
    surcharge = 25
elif(units <=100):
    amount = 130 + ((units-50) * 3.25)
    surcharge = 45
elif(units <= 200):
    amount = 130 + 162.50 +((units-200) * 5.26)
    surcharge = 75
else:
    amount = 130 +162.50 +526 +((units-200)*8.45)
total = amount+surcharge
print("Electricity bill = %.2f" %total)