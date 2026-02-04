def main():

    Source_File = input("Enter source file name => ")
    Destination_File = input("Enter destination file name => ")

    try:
        fsrc = open(Source_File, "r")
        fdest = open(Destination_File, "w")

        Data = fsrc.read()
        fdest.write(Data)

        print("File copied successfully.")

        fsrc.close()
        fdest.close()

    except FileNotFoundError:
        print("Source file does not exist.")

    finally:
        print("End of Application")


if __name__ == "__main__":
    main()
