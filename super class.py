class Phone:
    def p(self):
        print("Phone can call")

    def m(self):
        print("Any phone can message")


class Xiaomi(Phone):
    def ir(self):
        print("Phone can be used as remote")

    def m(self):
        super().m()  # Call the parent class's method
        print("Xiaomi phone can also message")  # Additional functionality


t1 = Xiaomi()
t1.ir()
t1.m()
t1.p()
