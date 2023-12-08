def even():
    number1 = int(input("Enter a number : "))

    while True:
        if number1 % 2 == 0:
            print(f"The number {number1} is even")
            b = int(input("enter a number"))
            if b % 2 == 0:
                break
        else:
            print(f"The number {number1} is odd")
even()
