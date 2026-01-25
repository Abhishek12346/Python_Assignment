
def List_Addition(data):
   
    for i in data:
        total=total+i
    return total    


def main():


    size=int(input("Enter the Size of the List =>"))
    data=[]


    for i in range(size): 
        num=int(input("Enter the Number =>"))
        data.append(num)

    Result=List_Addition(data)
    print(Result)


if __name__=="__main__":
    main()    


    
    