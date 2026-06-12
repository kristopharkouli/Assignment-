class Assignment10Address_Indian:
    """
    Address Class - Represents an address with street, city, and postal code
    """
    
    def __init__(self, street, city, postal_code):
        self.street = street
        self.city = city
        self.postal_code = postal_code
    
    def __str__(self):
        return f"{self.street}, {self.city} - {self.postal_code}"
    
    def __repr__(self):
        return f"Assignment10Address_Indian('{self.street}', '{self.city}', '{self.postal_code}')"
