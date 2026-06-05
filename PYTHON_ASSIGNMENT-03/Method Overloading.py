class Demo:
    def add(self, a, b=0):
        print(a + b)

obj = Demo()
obj.add(5)
obj.add(5, 10)