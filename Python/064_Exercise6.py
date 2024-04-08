# Write a library class with no of books and books as two instance variables. WAP to create a library from this Library class and show how you can print
# all boks, add a book and get the number of books using different methods. Show that your program dosent persist the books after the program is stopped.

class Library:
    def __init__(self):
        self.noBooks = 0
        self.books=[]

    def addBook(self, book):
        self.books.append(book)
        self.noBooks = len(self.books)

    def showInfo(self):
        print(f"The library has {self.noBooks} books")
        
l1 = Library()
l1.addBook("Bunny1")
l1.addBook("Bunny2")
l1.addBook("Bunny3")
l1.showInfo()