class Assignment11Library_Indian:
    """
    Library - Manages a collection of library items
    """
    
    def __init__(self, name):
        self.name = name
        self.items = []
    
    def add_item(self, item):
        """Add an item"""
        if item not in self.items:
            self.items.append(item)
            print(f"✓ '{item.title}' added to library")
        else:
            print(f"✗ '{item.title}' already exists")
    
    def remove_item(self, item_id):
        """Remove an item"""
        for item in self.items:
            if item.item_id == item_id:
                self.items.remove(item)
                print(f"✓ Item ID {item_id} removed")
                return
        print(f"✗ Item ID {item_id} not found")
    
    def display_all_items(self):
        """Display all items"""
        print("\n" + "╔" + "═"*58 + "╗")
        print("║" + f" {self.name} - All Items".ljust(58) + "║")
        print("╚" + "═"*58 + "╝")
        
        if not self.items:
            print("Library is empty")
            return
        
        for item in self.items:
            item.displayInfo()
    
    def search_by_title(self, title):
        """Search by title"""
        print(f"\n🔍 Searching for '{title}':")
        found = False
        for item in self.items:
            if title.lower() in item.title.lower():
                item.displayInfo()
                found = True
        
        if not found:
            print(f"✗ '{title}' not found")
    
    def search_by_year(self, year):
        """Search by year"""
        print(f"\n🔍 Items published in {year}:")
        found = False
        for item in self.items:
            if item.year == year:
                item.displayInfo()
                found = True
        
        if not found:
            print(f"✗ No items found for {year}")
    
    def get_statistics(self):
        """Get library statistics"""
        print("\n" + "="*60)
        print("📊 Library Statistics")
        print("="*60)
        print(f"Library Name: {self.name}")
        print(f"Total Items: {len(self.items)}")
        
        # Count by type
        books = sum(1 for item in self.items if 'Book' in type(item).__name__)
        dvds = sum(1 for item in self.items if 'DVD' in type(item).__name__)
        magazines = sum(1 for item in self.items if 'Magazine' in type(item).__name__)
        
        print(f"Books: {books}")
        print(f"DVDs: {dvds}")
        print(f"Magazines: {magazines}")
        print("="*60)
