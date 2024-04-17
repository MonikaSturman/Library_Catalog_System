from LibraryItem import LibraryItem

class Book(LibraryItem):
    
# Book Class Methods:
# borrow_book(): Mark the book as borrowed and update its availability status.
# return_book(): Mark the book as returned and update its availability status.
    
    def __init__(self, title, author, isbn):
        super().__init__(title, isbn) # Call parent class constructor
        self.author = author
        self.isbn = isbn
       
    def borrow_book(self):
        if self.availability: # checking if the book available
            self.availability = False # mark the book as borrowed
            return True  # now the book is borrowed
        else:
            return False # book is already borrowed
        
    def return_book(self):
        self.availability = True 
        return True # book returned
            
            
my_book = Book("Python Introduction", "Peterson A.W.", 657889001)     
print(my_book.isbn)
print(my_book.availability) 

my_book.borrow_book()
print(my_book.availability)

print(my_book.isbn)
print(my_book.item_id)

my_book.return_book()

print(my_book.availability)