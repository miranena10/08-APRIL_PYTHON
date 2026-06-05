class A:
    def show(self):
        print("Class A")

class B(A):
    pass

class C(A):
    pass

B().show()
C().show()