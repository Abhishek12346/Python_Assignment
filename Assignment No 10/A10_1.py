def MulTable(no):
    for i in range(1,11):
        Table=no*i
        print(Table)
def main():
    Num=int(input(" Enter the Number=>"))

    MulTable(Num)

   

if __name__=="__main__":
    main()