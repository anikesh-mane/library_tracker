from datetime import datetime
from library import LibraryItem

# ============================================================================
# CONCEPT 16: OOP PART 1 - Classes, Objects, Constructor
# ============================================================================

class Book(LibraryItem):
    """
    Represents a physical book in the library.
    This is a concrete class that inherits from LibraryItem.
    
    Class Definition Components:
    - Constructor (__init__): Initializes object state
    - Instance variables: Data unique to each object
    - Methods: Functions that operate on the object
    """
    
    # CONCEPT 17: Class Variable (shared by all instances of Book)
    # Class variables belong to the class itself, not to individual objects
    total_books_created = 0
    default_borrow_period = 14  # days
    
    def __init__(self, book_id, title, author, year, genre="General"):
        """
        Constructor method - called when creating a new Book object.
        
        Parameters:
        - self: Reference to the current instance
        - book_id, title, author, year: Instance-specific data
        - genre: Optional parameter with default value
        """
        # Call parent class constructor
        super().__init__(book_id, title, author, year)
        
        # CONCEPT 17: Instance Variables (unique to each object)
        # These are created using self and are different for each Book object
        self.__book_id = book_id  # Private variable (name mangling with __)
        self.__title = title      # Private variable
        self.__author = author    # Private variable
        self.__year = year        # Private variable
        self._genre = genre       # Protected variable (convention: single _)
        self._available = True    # Protected variable
        self._borrowed_by = None  # Protected variable
        self._borrowed_date = None
        
        # Increment class variable
        Book.total_books_created += 1
    
    # ========================================================================
    # CONCEPT 17: ENCAPSULATION - Getters and Setters (Access Control)
    # ========================================================================
    # Encapsulation hides internal state and requires interaction through methods
    # This protects data integrity
    
    # Getter methods (read-only access to private variables)
    @property # this decorator make the method accessible like an attribute !
    def book_id(self):
        """Property decorator makes this method accessible like an attribute"""
        return self.__book_id
    
    @book_id.setter
    def book_id(self, value):
        """Setter for book_id with validation"""
        if isinstance(value, int) and value > 0:
            self.__book_id = value
        else:
            print("Invalid book ID. Must be a positive integer.")
    
    @property
    def title(self):
        """Getter for title"""
        return self.__title
    
    @property
    def author(self):
        """Getter for author"""
        return self.__author
    
    @property
    def year(self):
        """Getter for year"""
        return self.__year
    
    def get_genre(self):
        """Regular getter method"""
        return self._genre
    
    # Setter method with validation
    def set_genre(self, genre):
        """
        Setter with validation logic.
        This is encapsulation in action - controlling how data is modified.
        """
        valid_genres = ["Fiction", "Non-Fiction", "Science", "History", "Programming", "General"]
        if genre in valid_genres:
            self._genre = genre
            print(f"Genre updated to: {genre}")
        else:
            print(f"Invalid genre. Must be one of: {valid_genres}")
    
    # ========================================================================
    # CONCEPT 16: Instance Methods (operate on instance data)
    # ========================================================================
    
    def is_available(self):
        """Check if book is available for borrowing"""
        return self._available
    
    def borrow(self, user_id):
        """
        Mark book as borrowed.
        Returns True if successful, False if already borrowed.
        """
        if self._available:
            self._available = False
            self._borrowed_by = user_id
            self._borrowed_date = datetime.now()
            return True
        return False
    
    def return_book(self):
        """
        Mark book as returned.
        Returns the number of days it was borrowed.
        """
        if not self._available and self._borrowed_date:
            days_borrowed = (datetime.now() - self._borrowed_date).days
            self._available = True
            self._borrowed_by = None
            self._borrowed_date = None
            return days_borrowed
        return 0
    
    # ========================================================================
    # CONCEPT 19: POLYMORPHISM - Method Overriding
    # ========================================================================
    # Implementing abstract methods from parent class
    
    def get_info(self):
        """
        Implementation of abstract method from LibraryItem.
        This is polymorphism - same method name, different implementation.
        """
        status = "Available" if self._available else f"Borrowed by User {self._borrowed_by}"
        return f"[Book #{self.__book_id}] '{self.__title}' by {self.__author} ({self.__year}) - {status}"
    
    def calculate_late_fee(self, days_late):
        """Calculate late fee for books - $0.50 per day"""
        return days_late * 0.50
    
    # ========================================================================
    # CONCEPT 17: Class Methods (operate on class data, not instance data)
    # ========================================================================
    
    @classmethod
    def get_total_books(cls):
        """
        Class method - uses @classmethod decorator.
        Works with class variables, receives 'cls' instead of 'self'.
        Called on the class itself: Book.get_total_books()
        """
        return cls.total_books_created
    
    @classmethod
    def create_from_string(cls, book_string):
        """
        Factory method - alternative constructor.
        Creates a Book object from a formatted string.
        """
        # Example: "101|Python Guide|John Doe|2023|Programming"
        parts = book_string.split('|')
        return cls(int(parts[0]), parts[1], parts[2], int(parts[3]), parts[4])
    
    # ========================================================================
    # CONCEPT 17: Static Methods (don't need class or instance data)
    # ========================================================================
    
    @staticmethod
    def is_valid_isbn(isbn):
        """
        Static method - uses @staticmethod decorator.
        Doesn't need access to class or instance data.
        Utility function logically related to the class.
        """
        # Simple ISBN-10 validation (just checking format)
        isbn = isbn.replace('-', '').replace(' ', '')
        if len(isbn) == 10:
            return isbn[:-1].isdigit() and (isbn[-1].isdigit() or isbn[-1].upper() == 'X')
        return False
    
    # ========================================================================
    # Special Methods (Magic Methods / Dunder Methods)
    # ========================================================================
    
    def __str__(self):
        """
        String representation for print() and str().
        Makes the object human-readable.
        """
        return f"'{self.__title}' by {self.__author}"
    
    def __repr__(self):
        """
        Official string representation for debugging.
        Should ideally be valid Python code to recreate the object.
        """
        return f"Book({self.__book_id}, '{self.__title}', '{self.__author}', {self.__year}, '{self._genre}')"
    
    def __eq__(self, other):
        """
        Equality comparison (==).
        Two books are equal if they have the same ID.
        """
        if isinstance(other, Book):
            return self.__book_id == other.book_id
        return False
    
    def __lt__(self, other):
        """
        Less than comparison (<) for sorting.
        Books are compared by title alphabetically.
        """
        if isinstance(other, Book):
            return self.__title < other.title
        return NotImplemented