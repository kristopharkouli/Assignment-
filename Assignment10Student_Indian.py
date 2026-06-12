from Assignment10Address_Indian import Assignment10Address_Indian

class Assignment10Student_Indian:
    """
    Student Class - Represents a student with name, age, address, and courses
    """
    
    def __init__(self, name, age, address, courses=None):
        if not isinstance(address, Assignment10Address_Indian):
            raise TypeError("address must be an Assignment10Address_Indian object")
        
        self.name = name
        self._age = None
        self.age = age  # Use property setter for validation
        self.address = address
        self.courses = courses if courses is not None else []
    
    @property
    def age(self):
        """Get age"""
        return self._age
    
    @age.setter
    def age(self, value):
        """Set and validate age"""
        if not isinstance(value, int):
            raise TypeError("Age must be an integer")
        if value < 5 or value > 100:
            raise ValueError("Age must be between 5 and 100")
        self._age = value
    
    def add_course(self, course):
        """Add a course"""
        if not isinstance(course, str) or not course.strip():
            raise ValueError("Course must be a non-empty string")
        self.courses.append(course)
        print(f"✓ '{course}' course added")
    
    def remove_course(self, course):
        """Remove a course"""
        if course in self.courses:
            self.courses.remove(course)
            print(f"✓ '{course}' course removed")
        else:
            print(f"✗ '{course}' course not found")
    
    def display(self):
        """Display student information"""
        print("\n" + "="*50)
        print("Student Details")
        print("="*50)
        print(f"Name: {self.name}")
        print(f"Age: {self.age} years")
        print(f"Address: {self.address}")
        print(f"Courses: {', '.join(self.courses) if self.courses else 'None'}")
        print("="*50)
