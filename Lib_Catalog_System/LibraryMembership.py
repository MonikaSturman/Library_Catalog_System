from LibraryItem import LibraryItem

class LibraryMembership(LibraryItem):
    def __init__(self, name, member_id, contact_info):
        self.name = name
        self.member_id = member_id
        self.contact_info = contact_info
        self.borrowed_items = []
        self.membership_status = "Active"
        
    def borrow_item(self, item):
        if item.is_available():
            item.borrow_item()
            self.borrowed_items.append(item)
            return True
        else:
            return False
        
    def return_item(self, item):
        if item in self.borrowed_items:
            item.return_item()
            self.borrowed_items.remove(item)
            return True
        else:
            return False
        
    def get_borrowed_items(self):
        return self.borrowed_items
    
    def renew_membership(self):
        # The meaning of here for example extend membership duration
        self.membership_status = "Renewed"
        return True      
    
    def update_contact_info(self, new_contact_info):
        self.new_contact_info = new_contact_info
        return True
    
    def check_membership_status(self):
        return self.membership_status  
        
        
        
        
    
    