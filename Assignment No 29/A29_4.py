def main():


    Source_file1=input("Enter the File 1st=>")
    source_file2=input("Enter the File 2nd=> ")

    try:

        f1=open(Source_file1,"r")
        f2=open(source_file2,"r")

        data1=f1.read()
        data2=f2.read()

        if data1==data2:
            print("Success Both are Equal Content")
        else:
            print("Failure Both are NOt equal Content")

        f1.close()
        f2.close()

    except FileNotFoundError:
        print("Unable to open one or both files")

    finally:
        print("End of Application")        


if __name__=="__main__":
    main()
