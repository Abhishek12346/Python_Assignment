import threading

def EvenList(data):
    even_list = []
    sum_even = 0

    for num in data:
        if num % 2 == 0:
            even_list.append(num)
            sum_even += num
            

    print("Even Elements = >", even_list)
    print("Sum of Even Elements =>", sum_even)


def OddList(data):
    odd_list = []
    sum_odd = 0

    for num in data:
        if num % 2 != 0:
            odd_list.append(num)
            sum_odd += num

    print("Odd Elements =>", odd_list)
    print("Sum of Odd Elements =>", sum_odd)


def main():
    data = []

    size = int(input("Enter the size of list: "))
    for i in range(size):
        value = int(input("Enter element: "))
        data.append(value)

    print("Input List =>", data)

    t1 = threading.Thread(target=EvenList, args=(data,), name="EvenList")
    t2 = threading.Thread(target=OddList, args=(data,), name="OddList")

    t1.start()
    t2.start()

    t1.join()
    t2.join()


if __name__ == "__main__":
    main()
