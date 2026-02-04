def main():

    File_Name=input("Enter the File Name =>")

    try:

        fobj=open(File_Name,"r")

        Data=fobj.read()
        print(Data)
        
        fobj.close()
    except FileNotFoundError:

        print("Unable to open the fileas there is no such file")   

    finally:
        print("End of Applications")   
if __name__=="__main__":
    main()
