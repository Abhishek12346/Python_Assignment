
def sum(num):
    sum = 0

    while num > 0:
      sum =sum + ( num % 10)
      num = num // 10

    
def main():
        num = int(input("Enter a number: "))
        sum(num) 
        print("Sum of digits:",sum)


if __name__=="__main__":
    main()

