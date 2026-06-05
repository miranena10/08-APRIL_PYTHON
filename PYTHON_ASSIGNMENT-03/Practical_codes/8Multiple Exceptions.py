try:
    f = open("data.txt", "r")
    a = 10 / 0
except FileNotFoundError:
    print("File not found")
except ZeroDivisionError:
    print("Division by zero")