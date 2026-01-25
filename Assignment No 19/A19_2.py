def main():

    num1=int(input("Enter the 1st Number=>"))
    num2=int(input("Enter the 2nd Number=>"))

    Multiplication=lambda num1,num2 : num1* num2

    Result=Multiplication(num1,num2)
    print("Multiplication of Number=>",Result)

if __name__=="__main__":
    main()    