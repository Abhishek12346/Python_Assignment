def main():
    data = [10, 20, 34, 53, 24, 45, 65]

    result = lambda num: num % 2 == 0

    rdata=list(filter(result,data))

    count = len(rdata)

    print("Count of even numbers =>", count)

if __name__ == "__main__":
    main()


