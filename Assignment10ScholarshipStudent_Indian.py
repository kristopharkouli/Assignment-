from Assignment10Student_Indian import Assignment10Student_Indian

class Assignment10ScholarshipStudent_Indian(Assignment10Student_Indian):
    """
    Scholarship Student Class - Extends Student with scholarship amount
    """
    
    def __init__(self, name, age, address, scholarship_amount, courses=None):
        super().__init__(name, age, address, courses)
        
        if not isinstance(scholarship_amount, (int, float)) or scholarship_amount < 0:
            raise ValueError("Scholarship amount must be a non-negative number")
        
        self.scholarship_amount = scholarship_amount
    
    def display(self):
        """Display scholarship student information"""
        super().display()
        print(f"Scholarship Amount: ₹{self.scholarship_amount:,.2f}")
        print("="*50)
    
    def update_scholarship(self, new_amount):
        """Update scholarship amount"""
        if not isinstance(new_amount, (int, float)) or new_amount < 0:
            raise ValueError("New scholarship amount must be a non-negative number")
        
        old_amount = self.scholarship_amount
        self.scholarship_amount = new_amount
        print(f"\n✓ Scholarship updated:")
        print(f"  Old Amount: ₹{old_amount:,.2f}")
        print(f"  New Amount: ₹{new_amount:,.2f}")
        print(f"  Difference: ₹{new_amount - old_amount:,.2f}")
