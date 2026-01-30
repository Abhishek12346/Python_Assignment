import threading

def Prime(data):
    prime_list = []
    for num in data:
        if num > 1:
            for i in range(2, num):
                if num % i == 0:
                    break
            else:
                prime_list.append(num)
    return prime_list

def NonPrime(data):
    non_prime_list = []
    for num in data:
        if num <= 1:
            non_prime_list.append(num)
        else:
            for i in range(2, num):
                if num % i == 0:
                    non_prime_list.append(num)
                    break
    return non_prime_list

def PrimeThread(data):
    print("Prime Numbers =>", Prime(data))

def NonPrimeThread(data):
    print("Non-Prime Numbers =>", NonPrime(data))

def main():
    data = []
    size = int(input("Enter the Size of the List => "))

    for i in range(size):
        num = int(input("Enter the Element => "))
        data.append(num)

    print("Input List =>", data)

    t1 = threading.Thread(target=PrimeThread, args=(data,))
    t2 = threading.Thread(target=NonPrimeThread, args=(data,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

if __name__ == "__main__":
    main()
