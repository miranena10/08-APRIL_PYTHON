# Generator function
def generate_even_numbers():
    for i in range(1, 11):
        yield i * 2

# Using the generator
for num in generate_even_numbers():
    print(num)