import threading

def Small(string):
    count = 0
    for ch in string:
        if ch.islower():
            count += 1

    print("\nSmall Thread")
    print("Lowercase Count:", count)
    print("Thread ID:", threading.get_ident())
    print("Thread Name:", threading.current_thread().name)


def Capital(string):
    count = 0
    for ch in string:
        if ch.isupper():
            count += 1

    print("\nCapital Thread")
    print("Uppercase Count:", count)
    print("Thread ID:", threading.get_ident())
    print("Thread Name:", threading.current_thread().name)


def Digits(string):
    count = 0
    for ch in string:
        if ch.isdigit():
            count += 1

    print("\nDigits Thread")
    print("Digits Count:", count)
    print("Thread ID:", threading.get_ident())
    print("Thread Name:", threading.current_thread().name)


def main():
    text = input("Enter a string: ")

    t1 = threading.Thread(target=Small, args=(text,), name="Small")
    t2 = threading.Thread(target=Capital, args=(text,), name="Capital")
    t3 = threading.Thread(target=Digits, args=(text,), name="Digits")

    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()


if __name__ == "__main__":
    main()
