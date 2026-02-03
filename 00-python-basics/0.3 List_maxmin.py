# youtube UNQ coder version 
def find_largest_smallest(input_list): 
    max=0 
    for i in input_list:
        if i>max:
            max=i
            return max
input_list = [23,45,12,67,34,89,5]
print("Largest element is: ", find_largest_smallest(input_list))

#modified to find both largest and smallest
def find_largest_smallest(input_list):
    largest = input_list[0]
    smallest = input_list[0]

    for i in input_list:
        if i > largest:
            largest = i
        if i < smallest:
            smallest = i

    return largest, smallest
        
input_list = [23, 45, 12, 67, 34, 89, 5]
largest, smallest = find_largest_smallest(input_list)
print("Largest element is:", largest)
print("Smallest element is:", smallest)


# mine
mylist = []
n = 4
for i in range(0,n):
    list_input = int(input("Enter number of elements in the list: "))
    mylist.append(list_input)
    largest = max(mylist)
    smallest = min(mylist)
print("largest value is: ", largest)
print("smallest value is: ", smallest)

# find largest and smallest element in list
mylist1 = [2, 5, 1, 3, 3, 5]
largest1 = max(mylist1)
smallest1 = min(mylist1)
print("Largest element is: ", largest1)
print("Smallest element is: ", smallest1)

# another method to find largest and smallest element in list
mylist2 = [45, 12, 78, 34, 23, 56]
mylist2.sort()
smallest2 = mylist2[0]
largest2 = mylist2[-1]
print("Smallest element is: ", smallest2)
print("Largest element is: ", largest2)
