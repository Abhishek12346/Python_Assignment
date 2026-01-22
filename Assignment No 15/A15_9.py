from functools import reduce


def main():

    data=[12,43,45,65,23,28]

    result=lambda num,ans:ans* num
    rdata=reduce(result,data)
    print("Produc of all Number=>",rdata)

if __name__=="__main__":
    main()
