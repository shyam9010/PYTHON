num = int(input("Enter the desired number: "))
if num > 1:
    for i in range(2, num):
        if (num % i) == 0:
            print("The provided number is not a prime number")
        else:
            print("The number is a prime number")
else:
    print("The number is not a prime number")
