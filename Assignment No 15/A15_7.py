def main():

    data = ["Abhi", "Piyush", "Rupesh", "Raj", "Sohan", "om"]
    
    result = lambda string: len(string) > 5
    fdata = list(filter(result, data))

    print("More than 5 Letter =>", fdata)

if __name__ == "__main__":
    main()
