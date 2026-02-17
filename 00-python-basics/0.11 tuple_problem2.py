#find index of an item in a tuple
tuple = (1, 2, 3, 4, 5)
find= 3
for i in range(len(tuple)):
    if (find == tuple[i]):
        print("element index is", i) 
        break

# Output: element index is 2
# count occurrences of an item in a tuple
tuple = (1, 2, 3, 4, 5, 3, 3)
find= 3
count = 0
for i in range(len(tuple)):
    if (find == tuple[i]):
        count += 1
print("element count is", count)
# Output: element count is 3
