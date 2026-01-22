def main():

    data=[10,23,25,65,34,50]

    result=lambda num: num %2==0 and num%5==0
    fdata=list(filter(result,data))
    print("Number is 2 and 5 Divisible=>",fdata)

if __name__=="__main__":
    main()    



