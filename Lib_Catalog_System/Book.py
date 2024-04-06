class Book:
    
# Book Class Methods:
# is_available(): Check if the book is available for borrowing.
# borrow_book(): Mark the book as borrowed and update its availability status.
# return_book(): Mark the book as returned and update its availability status.
    
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.availability = True # assume the book is available initially
        
    def is_available(self):
        return self.availability
    
    def borrow_book(self):
        if self.availability: # checking if the book available
            self.availability = False # mark the book as borrowed
            return True  # now the book is borrowed
        else:
            return False # book is already borrowed
        
    def return_book(self):
        self.availability = True 
        return True # book returned
            