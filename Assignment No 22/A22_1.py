class Demo:
    # class variable
    Value = 0

    # constructor
    def __init__(self, no1, no2):
        self.no1 = no1
        self.no2 = no2

    # instance method
    def Fun(self):
        print("Fun method:")
        print("no1 =", self.no1)
        print("no2 =", self.no2)

    # instance method
    def Gun(self):
        print("Gun method:")
        print("no1 =", self.no1)
        print("no2 =", self.no2)


# Creating objects
Obj1 = Demo(11, 21)
Obj2 = Demo(51, 101)

# Calling methods in given sequence
Obj1.Fun()
Obj2.Fun()
Obj1.Gun()
Obj2.Gun()
