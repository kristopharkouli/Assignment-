from Assignment11LibraryItem_Indian import Assignment11LibraryItem_Indian

class Assignment11Book_Indian(Assignment11LibraryItem_Indian):
    """
    Book - Represents a book with author, pages, and ISBN
    """
    
    def __init__(self, title, year, author, pages=None, isbn=None):
        super().__init__(title, year)
        self.author = author
        self.pages = pages if pages is not None else 0
        self.isbn = isbn if isbn is not None else "N/A"
    
    def displayInfo(self):
        """Display book information"""
        print("\n" + "="*60)
        print("📚 Book Details")
        print("="*60)
        print(f"Item ID: {self.item_id}")
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Year: {self.year}")
        print(f"Pages: {self.pages}")
        print(f"ISBN: {self.isbn}")
        print("="*60)
    
    def get_reading_time(self, pages_per_hour=30):
        """Get estimated reading time"""
        if self.pages == 0:
            return 0
        hours = self.pages / pages_per_hour
        return round(hours, 2)
