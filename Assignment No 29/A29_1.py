def main():
    filename = input("Enter file name: ")

    try:
        fobj = open(filename, "r")
        print(f"{filename} exists in the current directory.")
        fobj.close()

    except FileNotFoundError:
        print(f"{filename} does not exist in the current directory.")


if __name__ == "__main__":
    main()
