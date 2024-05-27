class ball:
    def __init__(self):
        print("Ball created")

    def who_i_am(self):
        print("I am ball")

class football(ball):
    def __init__(self):
        ball.__init__(self)
        print("Football created")

    def who_i_am(self):
        print("I am football")


f1 = football()
f1.zwho_i_am()
