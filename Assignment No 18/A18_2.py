
def main():
    data = []  

    size = int(input("Enter the Size of List => "))

    for i in range(size):
        num = int(input("Enter element => "))
        data.append(num)

        result=max(data)

    print("Max Element of the List=>",result)

if __name__ == "__main__":
    main()