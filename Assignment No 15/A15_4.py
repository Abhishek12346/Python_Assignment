from functools import reduce

def main():

    data = [12, 34, 56, 76, 33, 23]
    result = lambda num, total: total + num
    rdata = reduce(result, data)
    print("Sum of All Numbers in the List =>", rdata)

if __name__ == "__main__":
    main()
