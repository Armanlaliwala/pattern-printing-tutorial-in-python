current_value = 1
n = 5  # Number of terms to generate

print(f"{current_value}")

# Generate and print subsequent terms using the given pattern
for i in range(1, n):
    increment = 2 * i  # Calculate the increment (consecutive even numbers)
    current_value += increment
    # print(f'{current_value}')
    print(f"{current_value}")

for i in range(1,n) :
    for j in range(current_value) :
    
        print("*", end=" ")
    
    print() 
