
def main():
    data = []  

    size = int(input("Enter the Size of List => "))

    for i in range(size):
        num = int(input("Enter element => "))
        data.append(num)

        result=min(data)

    print("Min Element of the List =>",result)

if __name__ == "__main__":
    main()
