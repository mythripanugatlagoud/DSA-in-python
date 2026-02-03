mylist = [1,2,3,4]
sum_of_elements = sum(mylist)
print("Sum of elements in the list:", sum_of_elements)
# other method
mylist = [1, 2, 3, 4] 
total = 0
for num in mylist:
    total += num
print("Sum of elements using loop:", total)

# using function
# def list_sum(lst):
#     total = 0
#     for num in lst:
#         total += num
#     return total
 
def sum_of_list_elements(lst):
    sum =0
    for i in lst:
        sum += i
        # print("Current sum:", sum)  
    return sum 
lst = [1, 2, 3, 4]
print("Sum of elements using function:", sum_of_list_elements(lst))



            
