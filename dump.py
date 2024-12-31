# n = int(input("Enter Any number: "))
n = 4
for i in range(n):
    for j in range(i,n):
        print( end=" ")
    if i == 0:
        print("*")
    else:
        for j in range(i * 3):
            print("*", end="")        
        print()

