class phone:

  def p(self):
    print("phone can call")

  def m(self):
    print("any phone can message")


class xiaomi(phone):

  def ir(self):
    print("phone can call")

  def m(self):
    print("any phone can message")


t1 = xiaomi()
t1.ir()
t1.m()
t1.p()