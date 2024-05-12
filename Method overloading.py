class Calculator:
    def add(self, x, y=0, z=0):
        print(x+y+z)


result1 = Calculator()
result1.add(5)

result2 = Calculator()
result2.add(3, 4)

result3 = Calculator()
result3.add(3,4,5)
