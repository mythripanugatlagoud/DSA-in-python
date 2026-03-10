# print even number elements in the list
def filter_even_numbers(numbers):
    even_numbers = []       
    for num in numbers:
        if num % 2 == 0:   
            even_numbers.append(num)
    return even_numbers
numbers = [1, 2, 3, 4, 5, 6]
result = filter_even_numbers(numbers)
print(result)

list = [1, 2, 3, 4, 5, 6]
even_number = []
for n in list:
    if n % 2 == 0:
        even_number.append(n)
        print(n)
        
def print_even_numbers(lst):
    for n in lst:
        if n % 2 == 0:
            print(n)
lst = [1, 2, 3, 4, 5, 6]
print_even_numbers(lst) 
