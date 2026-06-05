class A:
    def show(self):
        print("Class A")

class B(A):
    pass

class C(A):
    pass

b = B()
c = C()

b.show()
c.show()