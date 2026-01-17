def palindrome(s):
    
    if s == s[::-1]:
        print("Palindrome string")
    else:
        print("Not a palindrome string")




def main():
    text = input("Enter a string: ")
    palindrome(text)
if __name__=="__main__":
    main()

