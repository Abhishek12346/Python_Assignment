from functools import reduce

# Function to check prime number
def is_prime(no):
    if no <= 1:
        return False
    for i in range(2, no):
        if no % i == 0:
            return False
    return True

def multiply(no):
    return no * 2

def find_max(a, b):
    if a > b:
        return a
    else:
        return b

def main():
    data = []  

    size = int(input("Enter the Size of List => "))

    for i in range(size):
        num = int(input("Enter element => "))
        data.append(num) 

    print("Element of the List=>",data)

    print("**********************************************************")

    fdata = list(filter(is_prime, data))
    print("List after filter =", fdata)


    mdata = list(map(multiply, fdata))
    print("List after map =", mdata)

    rdata = reduce(find_max, mdata)
    print("Output of reduce =", rdata)

if __name__ == "__main__":
    main()
