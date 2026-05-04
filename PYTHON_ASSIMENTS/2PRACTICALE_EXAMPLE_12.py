# Number of rows
rows = 5

# Outer loop for rows
for i in range(1, rows + 1):
    # Inner loop for stars
    for j in range(i):
        print("*", end="")
    print()  # Move to next line