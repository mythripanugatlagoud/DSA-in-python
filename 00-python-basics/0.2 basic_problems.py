# PROBLEM 1: CHECK EVEN / ODD
# Logic : “If a number is divisible by 2, it is even. Otherwise odd.”
n = int(input("Enter an integer: "))
if n % 2 == 0:
    print(n, "is even.")
else:   
    print(n, "is odd.")
    
# PROBLEM 2: CALCULATE SUM OF TWO NUMBERS
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("The sum is:", a + b)

# PROBLEM 3: FIND LARGER NUMBER
x = int(input("Enter first number: "))
y = int(input("Enter second number: ")) 
if x > y:
    print(x, "is larger.")
else:
    print(y, "is larger.")

# PROBLEM 4: CALCULATE FACTORIAL
# Logic : “Factorial of a non-negative integer n is the product of all positive integers less than or equal to n.”
num = int(input("Enter a non-negative integer: "))
factorial = 1
for i in range(1, num + 1):
    factorial *= i
print("The factorial of", num, "is", factorial)

# PROBLEM 5: PRINT MULTIPLICATION TABLE
n = int(input("Enter an integer to print its multiplication table: "))
for i in range(1, 11):
    print(n, "x", i, "=", n * i)
# PROBLEM 6: CHECK PRIME NUMBER
# Logic : “A prime number is a natural number greater than 1 that cannot be formed by multiplying two smaller natural numbers.”
n = int(input("Enter a number: "))
is_prime = True
if n <= 1:
    is_prime = False
else:
    for i in range(2, n):
        if n % i == 0:
            is_prime = False
            break
if is_prime:
    print("Prime number")
else:
    print("Not a prime number") 
           
# PROBLEM 7: CALCULATE FIBONACCI SEQUENCE UPTO N TERMS
n = int(input("Enter number of terms: "))
a = 0
b = 1

if n <= 0:
    print("Enter a positive number")
elif n == 1:
    print(a)
else:
    print(a)
    print(b)
    for i in range(2, n):
        c = a + b
        print(c)
        a = b
        b = c


# PROBLEM 8: FIND GCD OF TWO NUMBERS
# Logic : “The greatest common divisor (GCD) of two integers is the largest positive    integer that divides both numbers without leaving a remainder.”
def gcd(x, y):
    while y:
        x, y = y, x % y
    return x        
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("The GCD of", a, "and", b, "is", gcd(a, b))
# PROBLEM 9: CHECK PALINDROME
# Logic : “A palindrome is a word, number, phrase, or other sequence of characters
# that reads the same forward and backward (ignoring spaces, punctuation, and capitalization).”
s = input("Enter a string: ")
is_palindrome = True

for i in range(len(s) // 2):
    if s[i] != s[len(s) - i - 1]:
        is_palindrome = False
        break

if is_palindrome:
    print("Palindrome")
else:
    print("Not a Palindrome")
           
# PROBLEM 10: CALCULATE POWER OF A NUMBER
base = float(input("Enter the base number: "))
exponent = int(input("Enter the exponent: "))           
result = base ** exponent
print(base, "raised to the power of", exponent, "is", result)         
  
# Additional Problems
# Sum of n numbers 
n = int(input("Enter n: "))

total = 0
for i in range(1, n + 1):
    total += i

print("Sum:", total)
    
# Swap two numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

temp = a
a = b
b = temp

print("After swap:")
print("a =", a)
print("b =", b)

# Number patterns 
n = int(input("Enter number of rows: "))

for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end="")
    print()

# Reverse number
num = int(input("Enter number: "))
rev = 0

while num > 0:
    digit = num % 10
    rev = rev * 10 + digit
    num //= 10

print("Reversed number:", rev)

# Sum of digits
num = int(input("Enter number: "))
s = 0

while num > 0:
    s += num % 10
    num //= 10

print("Sum of digits:", s)


   
        
# (You can implement these additional problems similarly if needed)       
# PROBLEM 11: CALCULATE AVERAGE OF A LIST OF NUMBERS
# PROBLEM 12: FIND MAXIMUM AND MINIMUM IN A LIST OF NUMBERS
# PROBLEM 13: SORT A LIST OF NUMBERS IN ASCENDING ORDER     
# PROBLEM 14: COUNT VOWELS IN A STRING
# PROBLEM 15: REVERSE A STRING
# PROBLEM 16: CHECK LEAP YEAR
# PROBLEM 17: CONVERT CELSIUS TO FAHRENHEIT 
# PROBLEM 18: FIND THE LENGTH OF A STRING
# PROBLEM 19: REMOVE DUPLICATES FROM A LIST 
# PROBLEM 20: CHECK IF A STRING IS A SUBSTRING OF ANOTHER STRING    
