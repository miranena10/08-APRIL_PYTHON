class MyError(Exception):
    pass

try:
    age = int(input("Enter age: "))
    if age < 18:
        raise MyError("Age must be 18 or above")
except MyError as e:
    print(e)