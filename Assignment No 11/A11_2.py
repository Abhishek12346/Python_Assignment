
def count(no):
    
  
    count = reversed(no)
    print("Number of digits:", count)

def main():
       
    num=int(input("Enter The Number=>"))
    count(num)

if __name__=="__main__":
    main()