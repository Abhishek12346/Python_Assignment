def pattern(no):
    for i in range(no):
        for j in range(1, no + 1):
            print(j, end=" ")
        print()

def main():
    n = int(input("Enter number => "))
    pattern(n)

if __name__ == "__main__":
    main()
