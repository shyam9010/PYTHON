a = open('open.txt', 'r')
count = 0
content = a.read()
spilt = content.split()
for i in spilt:
    count = count + 1
print(len(spilt))
print(count)
