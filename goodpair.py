a = [1, 4, 6, 8, 2]
b = 10

for i in range(0, len(a)):
    for j in range(0, len(a)):
        if i != j and a[i] + a[j] == b:
            print("good pair", a[i], a[j])
