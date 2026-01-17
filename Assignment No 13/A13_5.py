

def Grade(marks):

    if marks >= 75:
            print("Out Standing Brillant == Distinction")
    elif marks >= 60:
            print("First Class Obtain")
    elif marks >= 50:
            print("Second Class Obtain")
    else:
          print(" Fail Next Year Try")



def main():
    marks = int(input("Enter the marks=>"))
    Grade(marks)



if __name__=="__main__":
    main()