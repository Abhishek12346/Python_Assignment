    
def main():
    data = [12, 43, 24, 45, 33, 54, 56]
    a=lambda num : num %2==0
    Fdata = list(filter(a, data))

    print("Even Numbers =>", Fdata)

if __name__ == "__main__":
    main()
