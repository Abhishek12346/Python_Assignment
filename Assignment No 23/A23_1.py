class BookStore:
    # Class variable
    NoOfBooks = 0

    def __init__(self, Name, Author):
        # Instance variables
        self.Name = Name
        self.Author = Author

        # Increment class variable
        BookStore.NoOfBooks += 1

    def Display(self):
        print(self.Name, "by", self.Author, ". No of books:", BookStore.NoOfBooks)


# Example usage
Obj1 = BookStore("Linux System Programming", "Robert Love")
Obj1.Display()

Obj2 = BookStore("C Programming", "Dennis Ritchie")
Obj2.Display()
