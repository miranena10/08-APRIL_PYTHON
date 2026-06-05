x = 100  # Global variable

class Demo:
    def show(self):
        y = 50  # Local variable
        print("Local:", y)
        print("Global:", x)

d = Demo()
d.show()