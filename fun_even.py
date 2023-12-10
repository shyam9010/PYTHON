def iseven(a):

    if a % 2 == 0:
        return True
    else:
        return False


a = int(input("Enter a Number : "))

result = iseven(a)

if result is True:
    print(a, "is even number ")
else:
    print(a, "is odd number ")
