class A:
    def show(self):
        print("Class A")

class B(A):
    pass

class C(A):
    pass

class D(B, C):
    pass

obj = D()
obj.show()