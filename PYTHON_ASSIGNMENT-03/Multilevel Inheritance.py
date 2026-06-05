class A:
    def show1(self):
        print("Class A")

class B(A):
    pass

class C(B):
    pass

obj = C()
obj.show1()