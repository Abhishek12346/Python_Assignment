
import threading
def sum_element(data):
    sum=0
    for i in data:
        sum=sum+i
    print("Sum of All element in The List=>",sum)

def Product(data):
    Fact=1
    for i in data:
        Fact=Fact*i
    print("Product Of the List Elemwnt=>",Fact)        

def main():

    data=[]
    Size=int(input("Enter the Size of the List=>"))

    for i in range(Size):
        Num=int(input("Enter the Element of the List=>"))
        data.append(Num)
    print("Data of the List =>",data) 

    t1=threading.Thread(target=sum_element,args=(data,))
    t2=threading.Thread(target=Product,args=(data,))

    t1.start()
    t2.start()
    t1.join()
    t2.join()
if __name__=="__main__":
    main()