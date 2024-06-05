def reverse(a, b, list):
    while a < b:
        list[a], list[b] = list[b], list[a]
        a = a+1
        b = b-1


r = 3
list = [1, 2, 3, 4, 5]
r = r % len(list)


reverse(0, r-2, list)
reverse(r-1, len(list)-1, list)
reverse(0, len(list)-1, list)
print(list)