a = [1, 2, 4, 5]
b = [4, 5, 9, 7]
c = []
for i in a:
    for j in b:
        if i == j:
            c.append(i)
            print(i)
print(c)
