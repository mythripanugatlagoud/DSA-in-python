fruits = ("apple", "banana", "cherry")
numbers = (1, 2, 3, 4, 5)

first_fruit = fruits[0]
last_fruit = fruits[-1]
print(first_fruit)  # Output: apple
print(last_fruit)   # Output: cherry
  
length = len(fruits)
combined = fruits + ("date", "elderberry")
sliced = fruits[1:3]
repeated = numbers * 2

print(length)       # Output: 3
print(combined)     # Output: ('apple', 'banana', 'cherry', 'date', 'elderberry')
print(sliced)      # Output: ('banana', 'cherry')
print(fruits)      # Output: ('apple', 'banana', 'cherry')
print(repeated)   # Output: (1, 2, 3, 4, 5, 1, 2, 3, 4, 5)
 
