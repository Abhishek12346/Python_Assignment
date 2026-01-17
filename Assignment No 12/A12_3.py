def Arithmatic(no1,no2):
    addition=no1+no2
    print("Addtion of Number=>",addition)

def Substraction(no1,no2):
    substraction=no1-no2
    print("Substraction of Number=>",substraction)

def multiplaction(no1,no2):
    multiplaction=no1*no2
    print("Multiplication of Number=>",multiplaction)

def division(no1,no2):
    division=no1/no2
    print("Division of Number=>",division)

def main():

    num1=int(input("Enter the 1 st Number=>"))
    num2=int(input("Entter the 2nd Number=>"))

    print("***************************************")

    Arithmatic(num1,num2)
    Substraction(num1,num2)
    multiplaction(num1,num2)
    division(num1,num2)


if __name__=="__main__":
    main()