def reverse_number(num):
    rev = 0
    while num > 0:
        rev = rev * 10 + num % 10
        num //= 10
    print(rev)    
   

def main():
    no = int(input("Enter a number: "))
    reverse_number(no)
    


if __name__=="__main__":
    main()