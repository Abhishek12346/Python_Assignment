def CheckVowel(Ch):
    Ch=Ch.lower()
    vowel=['a','e','i','o','u']
    if Ch in vowel:
        print("This is Vowel")
    else:
        print("Not a Vowel")
        
def main():
    
    Ch=input("Enter the Character=>")
    Ret=CheckVowel(Ch)
    
 
if __name__ =="__main__":
    main()