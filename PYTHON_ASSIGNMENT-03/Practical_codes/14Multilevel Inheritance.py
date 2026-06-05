class A:
    def show(self):
        print("Class A")

class B(A):
    pass

class C(B):
    pass

obj = C()
obj.show()