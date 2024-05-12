a = [2, 8, 7, 15]

max = a[0]
max1 = a[0]
for i in a:
    if i > max:
        max = i
for j in a:
    if j > max1 and j < max:
        max1 = j
product = max * max1
print(product)

# second approach if we have 2 num same

a = [1, 4, 67, 89]
max = a[0]
max1 = a[0]
ind = 0

for i in range(0, len(a)):
    if a[i] > max:
        max = a[i]
        ind = i
for j in range(0, len(a)):
    if a[j] > max1 and a[j] <= max and j != ind:
        max1 = a[j]

print(max * max1)
