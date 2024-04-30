a = [2, 3, 5, 7]
max = a[0]
min = a[0]
for i in a:
    if i > max:
        max = i
    if i < min:
        min = i
print(max, min)
