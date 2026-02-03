mylist = [4, 3, 1, 7]
list.sort(mylist)
print("Second largest element:", mylist[-2])
# other method
def second_largest_element(mylist):
    first = second = float('-inf')
    for number in mylist:
        if number > first:
            second = first
            first = number
        elif first > number > second:
            second = number
    return second
mylist = [4, 3, 1, 7]
print("Second largest element using function:", second_largest_element(mylist))
# using loop
mylist = [4, 3, 1, 7]
first = second = float('-inf')
for number in mylist:
    if number > first:
        second = first
        first = number
    elif first > number > second:
        second = number
print("Second largest element using loop:", second)
