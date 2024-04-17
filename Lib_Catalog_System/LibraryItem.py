class LibraryItem:
    def __init__(self, title, item_id):
        self.title = title
        self.item_id = item_id
        self.availability = True
        
    def is_available(self):
        return self.availability
    
    def borrow_item(self): 
        if self.availability:
            self.availability = False
            return True # Item successfully borrowed
        else:
            return False # Item is already borrowed
        
        
    def return_item(self):
        self.availability = True  
        return True # Item returned successfully      
            