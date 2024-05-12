class phone:
    def __init__(self):
        print("This is a phone")

class samsung(phone):
    def __init__(self):
        super().__init__()
        print("This is samsung phone")


s= samsung()