def pattern(no):
    for i in range(1, no + 1):
        for j in range(i):
            print("*", end="   ")
        print()

def main():
    n = int(input("Enter number => "))
    pattern(n)

if __name__ == "__main__":
    main()
