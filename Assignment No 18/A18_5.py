import MarvellousNum

def ListPrime(data):
    sum_prime = 0

    for no in data:
        if MarvellousNum.ChkPrime(no):
            sum_prime = sum_prime + no

    return sum_prime


def main():
    n = int(input("Enter number of elements: "))
    arr = []

    print("Enter elements:")
    for i in range(n):
        value = int(input())
        arr.append(value)

    result = ListPrime(arr)
    print("Addition of prime numbers:", result)


if __name__ == "__main__":
    main()
