def Frequency(data,No):
    Cnt=0
    for i in data:
        if i==No:
            Cnt+=1
    return Cnt


def main():
    data = []  

    size = int(input("Enter the Size of List => "))
    for i in range(size):
        num = int(input("Enter element => "))
        data.append(num)

    no=int(input("Enter the Serach  Number=>"))
    result=Frequency(data,no)
    print("Frequency of the Element=>",result)

if __name__ == "__main__":
    main()
