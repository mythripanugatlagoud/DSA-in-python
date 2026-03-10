def fib(x):
    if x == 0:
        return 0
    elif x == 1:
        return 1
    else:
        return fib(x-1) + fib(x-2)


def fibonacci_recursive(n):
    result = []
    for i in range(n):
        result.append(fib(i))
    return result


n = int(input("Enter n: "))
