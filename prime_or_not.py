num = int(input("Enter the desired number: "))
count = 0
if num > 1:
    for i in range(1, num+1):
        if (num % i) == 0:
            count = count + 1
else:
    print("The number is not a prime number")

if count == 2:
    print(num, "is a prime number")
else:
    print(num, "is not a prime number")
