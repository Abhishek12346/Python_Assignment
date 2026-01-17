
def NaturalNoSum(Size):
    sum=0
    for i in range(1,Size+1):
        sum=sum+i
    print(sum)

def main():    
    Size=int(input(" Enter the Number=>"))
    NaturalNoSum(Size)
    
if __name__=="__main__":
    main()