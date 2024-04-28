# merge and remove duplicates in list

a = [1, 2, 3, 4]
b = [2, 3, 4]
c = a + b

d = set()
for i in c:
    d.add(i)

e = list(d)
print(d)
