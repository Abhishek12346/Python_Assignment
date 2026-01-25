from functools import reduce

def main():
    data = []  

    size = int(input("Enter the Size of List => "))

    for i in range(size):
        num = int(input("Enter element => "))
        data.append(num)    
    print("Element of the List=>",data)
    
    result=lambda Num: Num%2==0
    fdata=list(filter(result,data))
    print("List Even Number use filter =", fdata)

     
    result=lambda No:No*No
    mdata=list(map(result,data))
    print("Map Square Function is =>",mdata)


    result=lambda a,b:a+b
    rdata=(reduce(result,data))
    print("Combine Result =>",rdata) 

if __name__ == "__main__":
    main()