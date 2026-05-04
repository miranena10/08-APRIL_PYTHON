from functools import reduce

numbers = [1, 2, 3, 4, 5]

def multiply(x, y):
    return x * y

product = reduce(multiply, numbers)

print("List:", numbers)
print("Product of elements:", product)