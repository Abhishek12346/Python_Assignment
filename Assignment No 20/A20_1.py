import threading
import time

def even(size):

    print("Even numbers:")
    for i in range(1, size + 1):
        if i % 2 == 0:
            print(i, end=" ")

def odd(size):
    print("\nOdd numbers:")
    for i in range(1, size + 1):
        if i % 2 != 0:
            print(i, end=" ")


def main():

    start_Time=time.time()
    t1=threading.Thread(target=even,name=even)
    t2=threading.Thread(target=odd,name=odd)

    t1.start()
    t2.start()

    t1.join()
    t2.join()

   
    size = int(input("Enter the size: "))
    even(size)
    odd(size)

    end_Time=time.time()

    print("\nTime Required=>",end_Time-start_Time)

if __name__ == "__main__":
    main()
