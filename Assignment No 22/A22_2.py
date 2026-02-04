class Circle:
    Pi=3.14

    def __init__(self):
        self.Radius=0.0
        self.Area=0.0
        self.Circumference=0.0

    def Accept(self):
        self.Radius=int(input("Enter the Radius of Circle=>"))

    def CalculateArea(self):
        self.Area=Circle.Pi * self.Radius * self.Radius

    def CalculateCircumference(self):
        self.Cal_Circum=2 * Circle.Pi * self.Radius * self.Radius  

    def Display(self):

        print("Radius of the Circle=>",self.Radius)
        print("Area Of Circle=>",self.Area)
        print("Circumference of Circle=>",self.Cal_Circum)


c1=Circle()

c1.Accept()
print("-"*45)
c1.CalculateArea()
c1.CalculateCircumference()
c1.Display()

