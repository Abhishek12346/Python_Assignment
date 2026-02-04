def main():

    try:

        fobj=open("Hello.txt","w")

        data=fobj.write(" ")

        fobj.close()

    except FileNotFoundError:
        print(" file does not exist.")

    finally:
        print("End of Application")


if __name__ == "__main__":
    main()
