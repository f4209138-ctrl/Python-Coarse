L = [23, 45, 12, 89, 4, 56, 78]
print(L)

count = 0

for i in L:
    count += i

avg = count / len(L)

print(count)
print(avg)

L.sort()

print(L[0])
print(L[-1])