name = input("Enter a Name  :")
b = -1
list = []
for i in name:
    if len(name) > 1:
        list.append(name[b])
        b = b-1
print(list)
