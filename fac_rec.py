def factorial(a):
    if a == 1:
        return 1
    if a == 0:
        return 1
    return a * factorial(a-1)


factorial(8)
print(factorial(6))
