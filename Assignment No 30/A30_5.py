def main():

    File_Name = input("Enter the File Name => ")
    Search_Word = input("Enter word to search => ")
    found = False

    try:
        fobj = open(File_Name, "r")

        for line in fobj:
            if Search_Word in line:
                found = True
                break

        if found:
            print("Word found in the file")
        else:
            print("Word not found in the file")

        fobj.close()

    except FileNotFoundError:
        print("Unable to open the file")

    finally:
        print("End of Application")


if __name__ == "__main__":
    main()
