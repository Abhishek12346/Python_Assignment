def fact(num):
    for i in range(1, num + 1):        
        if num % i == 0:
            print(i)

def main():
    num = int(input("Enter a number: "))
    fact(num)

if __name__=="__main__":
    main()    