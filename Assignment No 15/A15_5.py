from functools import reduce

def main():

    data=[10,23,24,54,66,56,2]

    result=lambda num1,num2:max(num1,num2)

    rdata=reduce(result,data)
    print("Max Number is =>",rdata)


    data1=[10,23,24,54,66,56,2]  

    result=lambda num1,num2:min(num1,num2)

    rdataa=(reduce(result,data))
    print("Min Number of List=>",rdataa)

if __name__=="__main__":
    main()    

