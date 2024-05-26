name = input("Enter a Name  :")
b = -1
list = []
list_2 = []
for i in name:
    list_2.append(i)
    if len(name) > 1:
        list.append(name[b])
        b = b-1
if list == list_2:
    print(name, " is a palindrome")
else:
    print(name, " is not a palindrome")
# second approach

c = ["s", "a", "s"]
d = 0
e = len(c) - 1
while (d < e):
    if c[d] == c[e]:
        d = d + 1
        e = e - 1
    else:
        print("not a palindrome")
        break
