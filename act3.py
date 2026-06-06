weather=(1,0,0,0,1,1,0)
rainy = 0
sunny = 0
for day in weather:
    if day == 1:
        rainy+=1
    else:
        sunny+=1
if rainy>sunny:
    print("It should rain")
elif sunny>rainy:
    print("It should be sunny")
else:
    print("The weather could be equally sunny and rainy")
