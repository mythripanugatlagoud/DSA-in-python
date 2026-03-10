# fibonacci series using iteration in fuction
def fibonacci_iterative(n):
    fib = []
    a, b = 0, 1

    for i in range(n):
        fib.append(a)
        a, b = b, a + b

    return fib

n = int(input("Enter n: "))
print(fibonacci_iterative(n))
n = int(input("Enter number of terms: "))

# fibonacci series using iteration in loop
a = 0
b = 1

print("Fibonacci Series:")

for i in range(n):
    print(a, end=" ")
    c = a + b
    a = b
    b = c
