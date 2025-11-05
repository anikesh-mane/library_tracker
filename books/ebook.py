from books.book import Book

# ============================================================================
# CONCEPT 18: INHERITANCE - Creating a Subclass
# ============================================================================

class EBook(Book):
    """
    EBook inherits from Book.
    Demonstrates inheritance - reusing code from parent class and extending it.
    
    Inheritance Benefits:
    - Code reuse: EBook gets all Book methods and attributes
    - Extensibility: Can add EBook-specific features
    - Polymorphism: Can use EBook anywhere Book is expected
    """
    
    def __init__(self, book_id, title, author, year, file_size_mb=0, file_format="PDF", genre="General"):
        """
        Constructor that extends parent constructor.
        Uses super() to call parent class's __init__.
        """
        # Call parent class constructor to initialize inherited attributes
        super().__init__(book_id, title, author, year, genre)
        
        # Add EBook-specific attributes
        self.file_size_mb = file_size_mb
        self.file_format = file_format
        self.download_count = 0
    
    # ========================================================================
    # CONCEPT 19: POLYMORPHISM - Method Overriding
    # ========================================================================
    
    def get_info(self):
        """
        Override parent method with EBook-specific implementation.
        This is polymorphism - same method name, different behavior.
        """
        # Call parent method and extend it
        basic_info = super().get_info()
        return f"{basic_info} | Format: {self.file_format} | Size: {self.file_size_mb}MB | Downloads: {self.download_count}"
    
    def calculate_late_fee(self, days_late):
        """
        EBooks have lower late fees since they're digital.
        Overriding parent method with different logic.
        """
        return days_late * 0.25  # Half the cost of physical books
    
    # EBook-specific methods
    def download(self):
        """Method specific to EBook - not available in parent class"""
        self.download_count += 1
        return f"Downloading {self.title} ({self.file_size_mb}MB)..."
    
    def get_file_format(self):
        """Another EBook-specific method"""
        return self.file_format