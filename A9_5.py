def  CheckDiv35(No):
    if No % 3 ==0 and No % 5==0 :
        return True
  
def main():
    Ret=False

    Num=int(input("Enter The Number =>"))
    Ret=CheckDiv35(Num)
    if Ret==True:
        print("Divisible by 3 and 5 ")

if __name__=="__main__":
    main()