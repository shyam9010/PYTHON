name = input("Enter a Name  :")
b = -1
list = []
for i in name:
    if len(name) > 1:
        list.append(name[b])
        b = b-1
print(list)
# second Approach
a = "shyam"
b = ""
for i in a:
    b = i + b
print(b)
