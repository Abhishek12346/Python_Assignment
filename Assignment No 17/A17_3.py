def factorial(no):
    fact = 1
    for i in range(1, no + 1):
        fact = fact * i
    return fact

def main():
    num = int(input("Enter the number => "))
    result = factorial(num)
    print("Factorial =>", result)

if __name__ == "__main__":
    main()
