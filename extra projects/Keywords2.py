def find_even_numbers():
    even_numbers = []
    for i in range(1, 100):
        if i % 2 != 0:
            continue
        elif i == 20:
            even_numbers.append(i)
            break
        elif i > 20:
            pass
        even_numbers.append(i)
    return even_numbers


result = find_even_numbers()
print(result)