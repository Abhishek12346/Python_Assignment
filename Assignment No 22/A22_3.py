class Arithmatic:

    def __init__(self):
        self.Value1=0
        self.Value2=0

    def Accept(self):

        self.Value1=int(input("Enter the Value 1st =>"))
        self.Value2=int(input("Enter the Value 2nd =>"))

    def Addition(self):
        return self.Value1 + self.Value2

    def Subtraction(self):
        return self.Value1 - self.Value2

    def Multiplication(self):
        return self.Value1 * self.Value2

    def Division(self):
        if self.Value2 != 0:
            return self.Value1 / self.Value2
        else:
            return "Division by zero not allowed"

A1 = Arithmatic()

A1.Accept()
print("-"*44)

print("Addition =", A1.Addition())
print("Subtraction =", A1.Subtraction())
print("Multiplication =", A1.Multiplication())
print("Division =", A1.Division())

A2 = Arithmatic()
print("-"*45)

A2.Accept()
print("-"*45)
print("Addition =", A2.Addition())
print("Subtraction =", A2.Subtraction())
print("Multiplication =", A2.Multiplication())
print("Division =", A2.Division())
