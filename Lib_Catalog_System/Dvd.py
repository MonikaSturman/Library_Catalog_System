from LibraryItem import LibraryItem

class Dvd(LibraryItem):
    
    def __init__(self, title, director, release_year, item_id):
        super().__init__(title, item_id)
        self.director = director
        self.release_year = release_year
        
    def borrow_dvd(self):
        if self.availability: # Check if the DVD is available
            self.availability= False # Mark the DVD as successfully borrowed
            return True # DVD successfully borrowed
        else:
            return False # DVD is already borrowed
        
    def return_dvd(self):
        self.availability = True
        return True 
    
dvd1 = Dvd("Heroes", "BlaBla", 2000, 98700012)

print(dvd1.availability)  
dvd1.borrow_dvd()

print(dvd1.availability)
dvd1.return_dvd()

print(dvd1.availability)         
            