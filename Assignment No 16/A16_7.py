
def Divisible(no):

    return no%5==0

def main():

    Num=int(input("Enter the Number=>"))
    Ans=Divisible(Num)
    print("Number is Divisible by 5=>",Ans)

if __name__=="__main__":
    main()    