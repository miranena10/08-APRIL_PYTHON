class A:
    def show(self):
        print("Parent Class")

class B(A):
    pass

obj = B()
obj.show()