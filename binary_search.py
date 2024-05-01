a = [1, 9, 4, 5, 38, 8, 2, 12, 16, 21, 23, 28]

a.sort()

num = int(input(" enter a number : "))

start = 0

end = len(a) - 1

while start <= end:
    mid = int((start + end) / 2)
    if a[mid] == num:
        print(mid)
        break
    elif a[mid] < num:
        start = mid + 1
    else:
        end = mid - 1
