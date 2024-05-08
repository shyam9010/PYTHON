a = [1, 2, 3, 4, 1, 2, 3, 1, 2, 1]
b = {}

for i in a:
    if i in b:
        b[i] = b[i] + 1
    else:
        b[i] = 1
for key, value in b.items():
    print(f"{key} : {value}")
