a = [1, 2, 3, 4, 5]
b = 0

c = len(a) - 1

while b < c:
    a[b], a[c] = a[c], a[b]
    b = b + 1
    c = c - 1
print(a)
