class phone:
    def call(self):
        print("All phone can call")

    def message(self):
        print("All phone can message")

class xiaomi(phone):  #call, message method came from phone class
    def ir_bluster(self):
        print("xiaomi phone has IR bluster")


p=phone()
p.call()
p.message()


x=xiaomi()
x.ir_bluster()

#call, message method came from phone class
x.call()
x.message()