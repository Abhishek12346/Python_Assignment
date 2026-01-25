def count_digits(no):
    count = 0
    while no > 0:
        count += 1
        no //= 10
    return count

def main():
    num = int(input("Enter number => "))
    print("Output =", count_digits(num))

if __name__ == "__main__":
    main()
