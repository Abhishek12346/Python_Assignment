
def Factors_addition(no):
    sum = 0
    for i in range(1, no + 1):
        if no % i == 0:
            sum = sum + i
    return sum


def main():
    num = int(input("Enter number=>"))
    Sum_All=Factors_addition(num)

    print("Addition of factors =", Sum_All)
if __name__=="__main__":
    main()    


