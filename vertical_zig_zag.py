n = int(input("Enter Any number: "))

for i in range(1, n + 1):
    for j in range(1, 4):
        if (i % 4 == 1 and j == 1) or (i % 4 == 3 and j == 3) or (i % 4 == 2 and j == 2) or (i % 4 == 0 and j == 2):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
