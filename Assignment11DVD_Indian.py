from Assignment11LibraryItem_Indian import Assignment11LibraryItem_Indian

class Assignment11DVD_Indian(Assignment11LibraryItem_Indian):
    """
    DVD - Represents a DVD with duration, genre, director, and rating
    """
    
    def __init__(self, title, year, duration, genre=None, director=None, rating=None):
        super().__init__(title, year)
        self.duration = duration  # in minutes
        self.genre = genre if genre is not None else "Unknown"
        self.director = director if director is not None else "Unknown"
        self.rating = rating if rating is not None else "N/A"
    
    def displayInfo(self):
        """Display DVD information"""
        print("\n" + "="*60)
        print("🎬 DVD Details")
        print("="*60)
        print(f"Item ID: {self.item_id}")
        print(f"Title: {self.title}")
        print(f"Director: {self.director}")
        print(f"Year: {self.year}")
        print(f"Duration: {self.duration} minutes")
        print(f"Genre: {self.genre}")
        print(f"Rating: {self.rating}")
        print("="*60)
    
    def get_duration_hours(self):
        """Get duration in hours"""
        return round(self.duration / 60, 2)
    
    def is_long_movie(self, threshold=120):
        """Check if movie is long"""
        return self.duration > threshold
