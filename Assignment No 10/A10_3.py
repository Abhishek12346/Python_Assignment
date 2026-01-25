
def factorial(Size):
    fact=1
    for i in range(1,Size+1):
        fact=fact*i
    print(fact)

def main():    
    Size=int(input(" Enter the Number=>"))
    factorial(Size)
    
if __name__=="__main__":
    main()