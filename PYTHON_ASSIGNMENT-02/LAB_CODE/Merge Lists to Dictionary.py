# Create two lists
keys = ["id", "name", "city"]
values = [101, "Mira", "Rajkot"]

# Create empty dictionary
data = {}

# Merge lists using loop
for i in range(len(keys)):
    data[keys[i]] = values[i]

print(data)