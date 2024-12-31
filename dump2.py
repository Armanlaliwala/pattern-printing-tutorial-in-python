current_value = 1
n = 5  # Number of terms to generate


print(" " * (2 * (n )) + "*")
for i in range(1,n) :
    increment = 2 * i  # Calculate the increment (consecutive even numbers)
    current_value += increment
    
    for j in range(i, n):
        print(" ", end=" ") 
    
    for j in range(1,current_value+1):
        print("*", end=" ")        
    print()
    # for j in range() :
    #     print("*", end=" ")        
    # print()
