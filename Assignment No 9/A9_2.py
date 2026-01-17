

def ChkGreater(No1,No2):

    if No1 > No2 :
        print(No1,"Number is Greater")
    else:
        print(No2,"Number is greater")

def main():
    Num1=int(input("Enter The 1st Number =>"))
    Num2=int(input("Enter The 2nd Number =>"))
    ChkGreater(Num1,Num2) 

if __name__=="__main__":
    main()
