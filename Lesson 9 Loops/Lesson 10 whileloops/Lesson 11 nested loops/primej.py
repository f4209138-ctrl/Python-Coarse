low = int(input("Enter a number in lower range:"))
hig= int(input("Enter a number in upper range:"))
print("Prime no. in the ",low,"and ", hig,"are:")
for num in range(low,hig) +1:
    for i in range (2,num):
        if(num%i)== 0:
            break
    else:
        print(num)