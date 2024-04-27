a = 0
b = 1
count = 0
list = []
while count < 10:
    c = a + b
    list.append(c)
    a = b
    b = c
    count += 1
print(list)
