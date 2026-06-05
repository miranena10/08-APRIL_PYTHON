class A:
    def __init__(self):
        print("Parent Constructor")

class B(A):
    def __init__(self):
        super().__init__()
        print("Child Constructor")

obj = B()