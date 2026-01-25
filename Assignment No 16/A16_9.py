
def Even(no):
    for i in range(1,no+1):
        if i %2==0:
            print(i,end=" ")

def main():

    Num=int(input("Enter the Number=>"))
    Even(Num)

if __name__=="__main__":
    main()




