
def factorial(Size):
    sum=1
    for i in range(1,Size+1):
        sum=sum*i
    print(sum)

def main():    
    Size=int(input(" Enter the Number=>"))
    factorial(Size)
    
if __name__=="__main__":
    main()