num = int(input("Enter a number:"))
if num <0 :
    num = -num
sum = 0
while num > 0:
    las = num%10
    sum += las
    num = num // 10
print(sum)