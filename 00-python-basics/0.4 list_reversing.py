# reversing a list entered by the user
mylist = []
n = 3
for i in range(0, n):
    list_input = input("Enter elements of the list : ")
    mylist.append(list_input)
    print(mylist)
mylist.reverse()
print("Reversed list is : ", mylist)
# reverse a list
mylist1 = [10, 20, 30, 40, 50]
mylist1.reverse()   
print("Reversed list is : ", mylist1)
# another method to reverse a list
mylist2 = [100, 200, 300, 400, 500]
reversed_list = mylist2[::-1]
print("Reversed list is : ", reversed_list)
# reversing a list using reversed() function
mylist3 = [1, 2, 3, 4, 5]
reversed_list2 = list(reversed(mylist3))
print("Reversed list is : ", reversed_list2)
