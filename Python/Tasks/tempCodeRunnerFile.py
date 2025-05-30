class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_available = True
    
class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f"{book.title} by {book.auther} added to the library.")
    
    def display_books(self):
        print("\n Library Collection: ")
        for book in self.books:
            status = "Available " if book.is_available else " Not Available"
            print(f" {book.title} by {book.author} |   ISBN: {book.isbn} | {status}")
        
    def borrow_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower() and book.is_available:
                book.is_available = False
                print(f"You borrowed '{book.title}'")
                return
        print(" Books Not available or not found")

    
    def return_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower() and not book.is_available:
                book.is_available = True
                print(f" You returned '{book.title}'")
                return
        print(" Book found or was not borrowed") 



my_library = Library()

my_library.add_book(Book("Python Basics", "John Doe", "111"))
my_library.add_book(Book("AI For Beginners", "Jan Smith", "222"))
my_library.add_book(Book("Deep Learning", "Andrew Ng", "333"))

while True:
    print("\n Library Menu")
    print("1. Show all books")
    print("2. Borrow a book")
    print("3. Return a book")
    print("4. Exit")

    choice = input("Choose an option: ")
    
    if choice == "1":
        my_library.display_books()
    elif choice == "2":
        title = input("Enter the book title to borrow: ")
        my_library.borrow_book(title)
    elif choice == "3":
        title = input("Enter the book title to return: ")
        my_library.return_book(title)
    elif choice == "4":
        print("Exiting the library system")

    

