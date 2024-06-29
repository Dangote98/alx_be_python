# pattern_drawing.py

# Prompt user for input
size = int(input("Enter the size of the pattern: "))

# Ensure the size is positive
if size > 0:
    # Draw the pattern using nested loops
    row = 0
    while row < size:
        for col in range(size):
            print("*", end="")
        print()  # Move to the next line after each row
        row += 1
else:
    print("Please enter a positive integer.")