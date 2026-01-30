import threading
def Min(data):
    result_Min=min(data)
    return result_Min   
 
def Max(data):
    result_Max=max(data)
    return result_Max

def Thread_Min(data):
    print("Min  Numbers =>", Min(data))
    

def Thread_Max(data):
    print("Max Number=>",Max(data))    

def main():

    data = []  
    size = int(input("Enter the Size of List => "))
    print("************************************************")
    for i in range(size):
        
        num = int(input("Enter element => "))
        data.append(num)
    print("************************************************")
        

    t1=threading.Thread(target=Thread_Min,args=(data,))
    t2=threading.Thread(target=Thread_Max,args=(data,))

    t1.start()
    t2.start()


    t1.join()
    t2.join()

if __name__ == "__main__":
    main()
