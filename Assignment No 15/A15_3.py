
def main():
    data=[12,23,45,67,78,43]
    result=lambda num: num %2!=0

    rdata=list(filter(result,data))
    print("Reduce Function is=>",rdata)
   
if __name__=="__main__":
    main()



