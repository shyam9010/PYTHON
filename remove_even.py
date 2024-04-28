# remove even from the list and print the resluting list
a = [1, 2, 3, 4]
b = []
for i in a:
    if i % 2 != 0:
        b.append(i)
print(b)
