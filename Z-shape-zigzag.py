row = int(input("Enter the number of rows: "))

for i in range(row):
    for j in range(3):
        if (i % 2 == 0 and j == 1) or ((i+j) % 2==0) :
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print("\n")
