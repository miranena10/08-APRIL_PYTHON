class Demo:
    def add(self, a, b=0):
        print(a + b)

obj = Demo()
obj.add(10)
obj.add(10, 20)