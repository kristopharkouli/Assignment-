from abc import ABC, abstractmethod

class Assignment11LibraryItem_Indian(ABC):
    """
    Library Item - Abstract base class for all library items with static counter
    """
    
    item_count = 0
    
    def __init__(self, title, year):
        Assignment11LibraryItem_Indian.item_count += 1
        self.item_id = Assignment11LibraryItem_Indian.item_count
        self.title = title
        self.year = year
    
    @abstractmethod
    def displayInfo(self):
        """Display item information"""
        pass
    
    @classmethod
    def get_total_items(cls):
        """Get total items count"""
        return cls.item_count
    
    @classmethod
    def reset_counter(cls):
        """Reset counter"""
        cls.item_count = 0
