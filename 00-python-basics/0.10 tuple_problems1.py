# access elements of tuple
my_tuple = (10, 20, 30, 40, 50)
print("First element:", my_tuple[0])
print("Last element:", my_tuple[-1])

# add elements to tuple
n = 4 
main_tuple = (10, 40)
for i in range(0,n):
    new_value = input("Enter value: ")
    main_tuple = main_tuple + (new_value,)
    print(main_tuple)
# iterate through tuple
    for i in range(0,len(main_tuple)):  
        print(f"Element at index {i}: {main_tuple[i]}")
    

    
