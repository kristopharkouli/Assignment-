from Assignment10Address_Indian import Assignment10Address_Indian
from Assignment10Student_Indian import Assignment10Student_Indian
from Assignment10ScholarshipStudent_Indian import Assignment10ScholarshipStudent_Indian

def print_header(title):
    """Print header"""
    print("\n▶ " + title)
    print("━" * 70)

def demonstrate_composition():
    """Demonstrate Composition"""
    print_header("1. Composition - Student contains Address")
    
    address = Assignment10Address_Indian("123 Raj Path", "New Delhi", "110001")
    print(f"Address created: {address}")
    
    student = Assignment10Student_Indian("Raj Kumar", 20, address)
    print(f"Student created: {student.name}")
    print(f"Student's address: {student.address}")

def demonstrate_property_validation():
    """Demonstrate Property Validation"""
    print_header("2. Property Validation - Age Validation")
    
    address = Assignment10Address_Indian("456 Gandhi Nagar", "Mumbai", "400001")
    student = Assignment10Student_Indian("Priya Sharma", 20, address)
    
    print(f"✓ Age set: {student.age} years")
    
    # Valid age change
    student.age = 21
    print(f"✓ Age updated: {student.age} years")
    
    # Invalid age - too young
    try:
        print("\n❌ Attempting invalid age: 3 years")
        student.age = 3
    except ValueError as e:
        print(f"✗ Error caught: {e}")
    
    # Invalid age - too old
    try:
        print("\n❌ Attempting invalid age: 150 years")
        student.age = 150
    except ValueError as e:
        print(f"✗ Error caught: {e}")
    
    # Invalid type
    try:
        print("\n❌ Attempting invalid type: 'twenty' (string)")
        student.age = "twenty"
    except TypeError as e:
        print(f"✗ Error caught: {e}")

def demonstrate_add_course():
    """Demonstrate Adding Courses"""
    print_header("3. Course Management")
    
    address = Assignment10Address_Indian("789 Patel Nagar", "Bangalore", "560001")
    student = Assignment10Student_Indian("Amit Patel", 19, address)
    
    print("Adding courses:")
    student.add_course("Mathematics")
    student.add_course("Science")
    student.add_course("English")
    
    student.display()
    
    print("\nRemoving course:")
    student.remove_course("Science")
    
    student.display()

def demonstrate_inheritance():
    """Demonstrate Inheritance"""
    print_header("4. Inheritance - Regular Student vs Scholarship Student")
    
    address1 = Assignment10Address_Indian("321 Shivaji Nagar", "Pune", "411001")
    address2 = Assignment10Address_Indian("654 Raj Nagar", "Chennai", "600001")
    
    # Regular student
    regular_student = Assignment10Student_Indian("Vijay Singh", 20, address1)
    regular_student.add_course("Computer Science")
    regular_student.add_course("Data Analysis")
    
    # Scholarship student
    scholarship_student = Assignment10ScholarshipStudent_Indian(
        "Neeta Verma", 
        21, 
        address2, 
        scholarship_amount=50000
    )
    scholarship_student.add_course("Engineering")
    scholarship_student.add_course("Physics")
    
    print("\n📚 Regular Student:")
    regular_student.display()
    
    print("\n🎓 Scholarship Student:")
    scholarship_student.display()

def demonstrate_polymorphism():
    """Demonstrate Polymorphism"""
    print_header("5. Polymorphism - Different Student Types")
    
    addresses = [
        Assignment10Address_Indian("111 Raj Path", "New Delhi", "110001"),
        Assignment10Address_Indian("222 Gandhi Nagar", "Mumbai", "400001"),
        Assignment10Address_Indian("333 Patel Nagar", "Bangalore", "560001"),
        Assignment10Address_Indian("444 Shivaji Nagar", "Pune", "411001"),
    ]
    
    students = [
        Assignment10Student_Indian("Raj Kumar", 20, addresses[0], ["Mathematics", "Science"]),
        Assignment10ScholarshipStudent_Indian("Priya Sharma", 21, addresses[1], 60000, ["Engineering"]),
        Assignment10Student_Indian("Amit Patel", 19, addresses[2], ["Arts", "Music"]),
        Assignment10ScholarshipStudent_Indian("Neeta Verma", 22, addresses[3], 75000, ["Medicine"]),
    ]
    
    print("\n📋 All Students Information:\n")
    for i, student in enumerate(students, 1):
        print(f"\n{'─'*70}")
        print(f"Student #{i} ({type(student).__name__})")
        print(f"{'─'*70}")
        student.display()

def demonstrate_mutable_behavior():
    """Demonstrate Mutable Behavior"""
    print_header("6. Mutable Behavior - Shared Reference")
    
    address = Assignment10Address_Indian("555 Nehru Nagar", "Hyderabad", "500001")
    student = Assignment10Student_Indian("Sunita Sharma", 20, address)
    
    print("Original student:")
    student.add_course("Economics")
    student.add_course("History")
    student.display()
    
    # Same reference
    same_student = student
    print("\n✓ Same reference created")
    
    print("\nAdding course through same reference:")
    same_student.add_course("Geography")
    
    print("\nOriginal student info - Changes visible:")
    student.display()

def main():
    """Main demonstration"""
    print("\n" + "╔" + "═"*68 + "╗")
    print("║" + " "*68 + "║")
    print("║" + "  Indian Student Management System".center(68) + "║")
    print("║" + "  OOP Concepts Demonstration".center(68) + "║")
    print("║" + " "*68 + "║")
    print("╚" + "═"*68 + "╝")
    
    demonstrate_composition()
    demonstrate_property_validation()
    demonstrate_add_course()
    demonstrate_inheritance()
    demonstrate_polymorphism()
    demonstrate_mutable_behavior()
    
    print("\n" + "╔" + "═"*68 + "╗")
    print("║" + "  Demonstration Complete".center(68) + "║")
    print("╚" + "═"*68 + "╝\n")

if __name__ == "__main__":
    main()
