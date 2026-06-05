class Parent:
    def show(self):
        print("Parent Class")

class Child(Parent):
    def show(self):
        print("Child Class")

obj = Child()
obj.show()