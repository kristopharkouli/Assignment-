from Assignment11Book_Indian import Assignment11Book_Indian
from Assignment11DVD_Indian import Assignment11DVD_Indian
from Assignment11Magazine_Indian import Assignment11Magazine_Indian
from Assignment11Library_Indian import Assignment11Library_Indian
from Assignment11LibraryItem_Indian import Assignment11LibraryItem_Indian

def print_header(title):
    """Print header"""
    print("\n▶ " + title)
    print("━" * 70)

def demonstrate_abstraction():
    """Demonstrate Abstraction"""
    print_header("1. Abstraction - Abstract Base Class")
    
    print("✓ Assignment11LibraryItem_Indian is an abstract class")
    print("✓ Cannot be instantiated directly")
    print("✓ All subclasses must implement displayInfo()")
    
    # Create concrete instances
    book = Assignment11Book_Indian("Gita", 1500, "Vyasa", 700)
    dvd = Assignment11DVD_Indian("Lagaan", 2001, 224, "Drama", "Aamir Khan", "U")
    magazine = Assignment11Magazine_Indian("Rajhans", 2023, "Rajhans Publications", 5, 120)
    
    print("\n✓ Concrete subclass instances created:")
    print(f"  - {type(book).__name__}")
    print(f"  - {type(dvd).__name__}")
    print(f"  - {type(magazine).__name__}")

def demonstrate_constructor_overloading():
    """Demonstrate Constructor Overloading"""
    print_header("2. Constructor Overloading - Default Arguments")
    
    print("Book 1 - All parameters:")
    book1 = Assignment11Book_Indian(
        "Bharat Ki Khoj", 
        1989, 
        "Jawaharlal Nehru", 
        pages=500, 
        isbn="978-81-7525-123-4"
    )
    book1.displayInfo()
    
    print("\nBook 2 - Minimal parameters:")
    book2 = Assignment11Book_Indian("Ramayana", 1500, "Valmiki")
    book2.displayInfo()
    
    print("\nDVD 1 - All parameters:")
    dvd1 = Assignment11DVD_Indian(
        "PK", 
        2014, 
        148, 
        genre="Comedy", 
        director="Rajkumar Hirani", 
        rating="U/A"
    )
    dvd1.displayInfo()
    
    print("\nDVD 2 - Minimal parameters:")
    dvd2 = Assignment11DVD_Indian("Shool", 1999, 160)
    dvd2.displayInfo()

def demonstrate_static_counter():
    """Demonstrate Static Counter"""
    print_header("3. Static Counter - Object Tracking")
    
    print(f"Initial total items: {Assignment11LibraryItem_Indian.get_total_items()}")
    
    print("\nCreating items:")
    book1 = Assignment11Book_Indian("Gita", 1500, "Vyasa", 700)
    print(f"  ✓ Book 1 created - ID: {book1.item_id}, Total: {Assignment11LibraryItem_Indian.get_total_items()}")
    
    dvd1 = Assignment11DVD_Indian("Dilwale Dulhania Le Jayenge", 1995, 189)
    print(f"  ✓ DVD 1 created - ID: {dvd1.item_id}, Total: {Assignment11LibraryItem_Indian.get_total_items()}")
    
    magazine1 = Assignment11Magazine_Indian("National Geographic", 2023, "National Geographic", 3)
    print(f"  ✓ Magazine 1 created - ID: {magazine1.item_id}, Total: {Assignment11LibraryItem_Indian.get_total_items()}")
    
    book2 = Assignment11Book_Indian("Mahabharata", 1500, "Vyasa", 1000)
    print(f"  ✓ Book 2 created - ID: {book2.item_id}, Total: {Assignment11LibraryItem_Indian.get_total_items()}")
    
    print(f"\nFinal total items: {Assignment11LibraryItem_Indian.get_total_items()}")

def demonstrate_method_overriding():
    """Demonstrate Method Overriding"""
    print_header("4. Method Overriding - displayInfo()")
    
    print("Calling displayInfo() for different item types:")
    
    book = Assignment11Book_Indian("Chandrakanta", 1888, "Devkinandan Khatri", 400)
    dvd = Assignment11DVD_Indian("Mother India", 1957, 172, "Drama", "Mehboob Khan")
    magazine = Assignment11Magazine_Indian("India Today", 2023, "India Today Group", 10, 150)
    
    book.displayInfo()
    dvd.displayInfo()
    magazine.displayInfo()

def demonstrate_polymorphism():
    """Demonstrate Polymorphism"""
    print_header("5. Polymorphism - Different Types in Single Collection")
    
    items = [
        Assignment11Book_Indian("Ramcharitmanas", 1574, "Tulsidas", 1200),
        Assignment11DVD_Indian("Bollywood Best Movies", 2020, 180, "Collection"),
        Assignment11Magazine_Indian("Sahitya Akademi", 2023, "Sahitya Akademi", 1, 200),
        Assignment11Book_Indian("Panchatantra", 300, "Vishnu Sharma", 250),
        Assignment11DVD_Indian("RSS", 2016, 156, "Drama", "Raj Kumar Gupta"),
    ]
    
    print(f"\nTotal {len(items)} items:\n")
    for item in items:
        item.displayInfo()

def demonstrate_library_management():
    """Demonstrate Library Management"""
    print_header("6. Library Management")
    
    library = Assignment11Library_Indian("National Library, New Delhi")
    
    print("\nAdding items:")
    book1 = Assignment11Book_Indian("Indian Constitution", 1950, "Dr. B.R. Ambedkar", 1200)
    book2 = Assignment11Book_Indian("Swadeshi", 1910, "Aurobindo Ghosh", 300)
    dvd1 = Assignment11DVD_Indian("Gandhi", 1982, 191, "Biography", "Richard Attenborough")
    magazine1 = Assignment11Magazine_Indian("Yojana", 2023, "Yojana Publications", 5, 100)
    
    library.add_item(book1)
    library.add_item(book2)
    library.add_item(dvd1)
    library.add_item(magazine1)
    
    library.display_all_items()
    library.get_statistics()
    
    print("\n🔍 Search Operations:")
    library.search_by_title("India")
    library.search_by_year(1950)
    
    print("\n📖 Item-Specific Methods:")
    print(f"Book reading time: {book1.get_reading_time()} hours")
    print(f"Film duration: {dvd1.get_duration_hours()} hours")
    print(f"Is it a long movie? {dvd1.is_long_movie()}")
    print(f"Magazine issue: {magazine1.get_issue_label()}")

def main():
    """Main demonstration"""
    print("\n" + "╔" + "═"*68 + "╗")
    print("║" + " "*68 + "║")
    print("║" + "  Indian Library System".center(68) + "║")
    print("║" + "  OOP Concepts Demonstration".center(68) + "║")
    print("║" + " "*68 + "║")
    print("╚" + "═"*68 + "╝")
    
    demonstrate_abstraction()
    demonstrate_constructor_overloading()
    demonstrate_static_counter()
    demonstrate_method_overriding()
    demonstrate_polymorphism()
    demonstrate_library_management()
    
    print("\n" + "╔" + "═"*68 + "╗")
    print("║" + "  Demonstration Complete".center(68) + "║")
    print("╚" + "═"*68 + "╝\n")

if __name__ == "__main__":
    main()
