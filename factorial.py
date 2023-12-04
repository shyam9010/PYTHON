def factorial(n):
    # Initialize the result to 1
    result = 1
    while n > 1:
        result = result * n
        n = n - 1

    return result

number = int(input("Enter a non-negative integer: "))

if number < 0:
    print("Factorial is not defined for negative numbers.")
else:
    result = factorial(number)
    print(f"The factorial of ",number, "is:" ,result)
