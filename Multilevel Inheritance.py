class a:
    def display1(self):
        print("This is class A")

class b(a):
    def display2(self):
        print("This is class B")

class c(b):
    def display3(self):
        print("This is class C")

obj1=a()
obj1.display1()

print("\n")

obj2=b()
obj2.display1()
obj2.display2()

print("\n")

obj3=c()
obj3.display1()
obj3.display2()
obj3.display3()