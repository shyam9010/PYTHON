a = [2, 8, 7, 15]

max = a[0]
max1 = a[0]
for i in a:
    if i > max:
        max = i
for j in a:
    if j > max1 and max1 < max:
        max1 = j
product = max * max1
print(product)
