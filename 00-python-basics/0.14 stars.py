# This code defines a function `print_star_pyramid` that takes an integer `n` as input and
# prints a pyramid of stars with `n` rows. Each row contains a certain number of spaces followed by a certain number of stars, creating a centered pyramid shape.
# The user is prompted to enter the number of rows for the pyramid, and the function is called with that input.
def print_star_pyramid(n):
    for i in range(1, n + 1):
        spaces = n - i
        stars = i
        print(" " * spaces + "*" * stars)
        
n = int(input("Enter number of rows: "))
print_star_pyramid(n)                                                                                                                     
