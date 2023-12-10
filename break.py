def multi():
    number = int(input("Enter the starting number : "))
    end = int(input("Enter the ending number : "))
    while number <= end:
        if number % 5 != 0:
            print(number)
        number += 1


multi()


def fun2():
    number = int(input("Enter the starting number : "))
    end = int(input("Enter the ending number : "))
    while True:
        if number > end:
            break

        if number % 5 == 0:
            number += 1
            continue
        print(number)
        number = number+1


def fun3():
    i = 0
    end = int(input("Enter the end:"))
    while True:
        i = i + 1
        if i > end:
            break

        if i % 5 == 0:
            continue
        print(i)


fun3()
