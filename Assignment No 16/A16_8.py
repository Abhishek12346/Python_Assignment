def pattern(num):

    for i in range(num):
        print("*",end=" ")

def main():
    num=int(input("Enter the Number=>"))
    pattern(num)
    
if __name__ == "__main__":
    main()