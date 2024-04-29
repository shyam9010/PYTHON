a = [6, 3, 2, 1, 4, 9]

b = len(a)

for i in range(0, b):
    for j in range(0, b-1):
        if a[j] > a[j + 1]:
            a[j], a[j + 1] = a[j + 1], a[j]
print(a)
