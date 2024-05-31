def fib(a):
    if a == 1:
        return 0
    elif a == 2:
        return 1
    else:
        return fib(a-1) + fib(a-2)


print(fib(5))
