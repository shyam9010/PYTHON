a = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
b = 0
for i in range(0, len(a)):
    for j in range(0, len(a[0])):
        b = b + a[i][j]
avg = b / (len(a) * len(a[0]))
print(avg)
