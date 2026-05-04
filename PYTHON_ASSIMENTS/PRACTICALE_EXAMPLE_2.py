# Numeric Data Types
num_int = 10                 # int
num_float = 5.5              # float
num_complex = 2 + 3j         # complex

# Sequence Data Types
text = "Hello Python"        # str
my_list = [1, "apple", 3.5]  # list
my_tuple = (10, 20, 30)      # tuple
my_range = range(1, 5)       # range

# Map Data Type
my_dict = {
    "name": "Mira",
    "age": 21
}                            # dict

# Set Data Type
my_set = {1, 2, 3, 3, 4}     # set (duplicates removed)

# Boolean Data Type
is_valid = True              # bool

# Display values and their types
print("Integer:", num_int, type(num_int))
print("Float:", num_float, type(num_float))
print("Complex:", num_complex, type(num_complex))

print("String:", text, type(text))
print("List:", my_list, type(my_list))
print("Tuple:", my_tuple, type(my_tuple))
print("Range:", list(my_range), type(my_range))

print("Dictionary:", my_dict, type(my_dict))
print("Set:", my_set, type(my_set))

print("Boolean:", is_valid, type(is_valid))