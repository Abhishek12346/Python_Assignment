import threading

def display_forward():
    print("Thread1: Numbers from 1 to 50")
    for i in range(1, 51):
        print(i, end=" ")
    print()

def display_reverse():
    print("Thread2: Numbers from 50 to 1")
    for i in range(50, 0, -1):
        print(i, end=" ")
    print()

def main():
    t1 = threading.Thread(target=display_forward, name="Thread1")
    t2 = threading.Thread(target=display_reverse, name="Thread2")

    t1.start()
    t1.join()   # Synchronization: wait for Thread1 to finish

    t2.start()
    t2.join()

if __name__ == "__main__":
    main()
