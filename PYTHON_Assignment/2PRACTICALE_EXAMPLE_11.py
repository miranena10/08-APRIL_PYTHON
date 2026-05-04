# List of strings
List1 = ['apple', 'banana', 'mango']

# String to search
search_item = input("Enter the fruit to search: ")

# Flag to check if found
found = False

# Loop through list
for fruit in List1:
    if fruit == search_item:
        print(search_item, "found in the list")
        found = True
        break

# If not found
if not found:
    print(search_item, "not found in the list")