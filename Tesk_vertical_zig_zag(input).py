def print_pattern(rows):
    """Prints the pattern of asterisks based on the number of rows provided.

    Args:
        rows: An integer representing the number of rows in the pattern.
    """

    # Outer loop for rows
    for i in range(rows):
        # Print spaces for the upper half
        for j in range(rows - i - 1):
            print(" ", end="")

        # Print asterisks
        for j in range(2 * i + 1):
            print("*", end="")

        # Move to the next line
        print()

    # Outer loop for lower half (excluding the middle row)
    for i in range(rows - 2, -1, -1):
        # Print spaces for the lower half
        for j in range(rows - i - 1):
            print(" ", end="")

        # Print asterisks
        for j in range(2 * i + 1):
            print("*", end="")

        # Move to the next line
        print()

# Get user input for the number of rows
rows = int(input("Enter the number of rows: "))

# Print the pattern
print_pattern(rows)
