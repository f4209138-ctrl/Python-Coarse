def multiply_tuple(numbers):
    product = 1
    for num in numbers:
        product *= num
    return product


tup1 = (4, 3, 2, 2, -1, 18)
tup2 = (2, 4, 8, 8, 3, 2, 9)

print(multiply_tuple(tup1))
print(multiply_tuple(tup2))