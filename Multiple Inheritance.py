class a:
    def display(self):
        print("This is class A")

class b:
    def display(self):
        print("This is class B")

class c(a,b):
    pass

obj3=c()
obj3.display()



class d(b,a):
    pass

obj4=d()
obj4.display()



