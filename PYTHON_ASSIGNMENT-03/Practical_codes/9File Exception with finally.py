try:
    f = open("data.txt", "r")
    print(f.read())
except FileNotFoundError:
    print("File not found")
finally:
    try:
        f.close()
        print("File closed")
    except:
        pass