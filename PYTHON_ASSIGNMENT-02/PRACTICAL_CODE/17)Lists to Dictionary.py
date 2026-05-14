# Create two lists
keys = ["id", "name", "city"]
values = [101, "Mira", "Rajkot"]

# Convert lists into dictionary
my_dict = {}

for i in range(len(keys)):
    my_dict[keys[i]] = values[i]

print(my_dict)