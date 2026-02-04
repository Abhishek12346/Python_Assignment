def main():

    File_Name = input("Enter the File Name => ")
    count = 0

    try:
        fobj = open(File_Name, "r")

        for line in fobj:          # through file
            count = count + 1

        print("Number of Lines =>", count)
        fobj.close()

    except FileNotFoundError:
        print("Unable to open the File")

    finally:
        print("End of Application")


if __name__ == "__main__":
    main()
