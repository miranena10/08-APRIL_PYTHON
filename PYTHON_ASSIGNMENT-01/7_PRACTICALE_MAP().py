numbers = [1, 2, 3, 4, 5]

def square(x):
    return x ** 2

squared = list(map(square, numbers))

print("Original list:", numbers)
print("Squared list:", squared)