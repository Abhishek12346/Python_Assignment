from functools import reduce

def main():
    data = []  

    size = int(input("Enter the Size of List => "))

    for i in range(size):
        num = int(input("Enter element => "))
        data.append(num)    
    print("Element of the List=>",data)
    
    result=lambda Num: Num >= 70 and Num <= 90
    fdata=list(filter(result,data))
    print("List after filter =", fdata)

     
    result=lambda No:No+10
    mdata=list(map(result,data))
    print("Map Function is =>",mdata)


    result=lambda a,b:a*b
    rdata=(reduce(result,data))
    print("Combine Result =>",rdata)

if __name__ == "__main__":
    main()