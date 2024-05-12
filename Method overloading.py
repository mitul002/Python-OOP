class Calculator:
    def add(self, x, y=0, z=0):
        print(x+y+z)


result1 = Calculator()
result1.add(5)

result2 = Calculator()
result2.add(3, 4)

result3 = Calculator()
result3.add(3,4,5)



'''class Calculator:
    def add(self, x, y, z=0):
        print(x + y + z)


result = Calculator()
result.add(5, 6)
result.add(5, 6, 9)'''

'''
# Using constructor
class Calculator:
    def __init__(self,x,y,z=0):
        print(x+y+z)

result1= Calculator(2,6,)
result= Calculator(2,7,2)

'''
