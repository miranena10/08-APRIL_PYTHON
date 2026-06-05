class A:
    def show1(self):
        print("Class A")

class B:
    def show2(self):
        print("Class B")

class C(A, B):
    pass

obj = C()
obj.show1()
obj.show2()