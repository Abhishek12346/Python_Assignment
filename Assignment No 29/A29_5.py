def main():

    File_Name=input("Enter the File Name=>")

    String=input("Enter the Sting=>")

    try:

        fobj=open(File_Name,"r")
        data=fobj.read()

        Count=data.count(String)
        print("Number of String is =>",Count)

        fobj.close()

    except FileNotFoundError:
        print("Unbale to open the File as String")

    finally:
        print("end of Applications")       


if __name__=="__main__":
    main()
