def main():
    try:
        fobj=open("Demo.txt","w")
        print("File Gets Succefully Opened")


        fobj.write("Ajeenkya dy Patil School of Engineering Lohegaon ")
        fobj.write("Shivnagaer Vidya Prasarak Mandal Malegaon Baramati \n")
        fobj.write("Cummnies Engineering Collage of Women Kothrud \n")
        fobj.write("Collage of Enginnering Pune \n")
        fobj.write("Pimpari Chicwad Institute of Collage of Engineerign pune \n")
        fobj.close()

    except FileNotFoundError:
        print("Unable to open the fileas there is no such file")   

    finally:
        print("End of Applications")     

if __name__=="__main__":
    main()
