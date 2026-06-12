from Assignment11LibraryItem_Indian import Assignment11LibraryItem_Indian

class Assignment11Magazine_Indian(Assignment11LibraryItem_Indian):
    """
    Magazine - Represents a magazine with publisher, issue number, and pages
    """
    
    def __init__(self, title, year, publisher, issue_number=None, pages=None):
        super().__init__(title, year)
        self.publisher = publisher
        self.issue_number = issue_number if issue_number is not None else 1
        self.pages = pages if pages is not None else 0
    
    def displayInfo(self):
        """Display magazine information"""
        print("\n" + "="*60)
        print("📰 Magazine Details")
        print("="*60)
        print(f"Item ID: {self.item_id}")
        print(f"Title: {self.title}")
        print(f"Publisher: {self.publisher}")
        print(f"Year: {self.year}")
        print(f"Issue Number: {self.issue_number}")
        print(f"Pages: {self.pages}")
        print("="*60)
    
    def get_issue_label(self):
        """Get formatted issue label"""
        return f"Issue #{self.issue_number} - {self.year}"
