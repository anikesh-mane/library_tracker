"""
library_classes.py
==================
This module contains all the Object-Oriented Programming concepts for the Library Tracker.

Demonstrates:
- CONCEPT 16: OOP Part 1 - Classes, Objects, Constructors
- CONCEPT 17: OOP Part 2 - Types of Variables & Methods, Encapsulation
- CONCEPT 18: OOP Part 3 - Inheritance
- CONCEPT 19: OOP Part 4 - Polymorphism & Abstract Classes
"""

from abc import ABC, abstractmethod  # For abstract classes
from datetime import datetime, timedelta

from user import User

# ============================================================================
# CONCEPT 19: ABSTRACT BASE CLASS
# ============================================================================
# Abstract classes define a template that other classes must follow
# They cannot be instantiated directly - only their subclasses can be instantiated

class LibraryItem(ABC):
    """
    Abstract base class representing any item in the library.
    This demonstrates the concept of abstraction - defining a common interface.
    """
    
    def __init__(self, item_id, title, creator, year):
        """Constructor for LibraryItem"""
        self._item_id = item_id
        self._title = title
        self._creator = creator
        self._year = year
    
    @abstractmethod
    def get_info(self):
        """
        Abstract method - must be implemented by all subclasses.
        This enforces a contract: all library items must provide info.
        """
        pass
    
    @abstractmethod
    def calculate_late_fee(self, days_late):
        """Calculate late fee - different items may have different fee structures"""
        pass


# ============================================================================
# CONCEPT 16, 17, 18, 19: Library Class (Aggregation and Composition)
# ============================================================================

class Library:
    """
    Main library class that manages books and users.
    Demonstrates composition (has-a relationship) and encapsulation.
    """
    
    def __init__(self, name):
        """Constructor for Library"""
        self.name = name
        self.__books = []  # Private list of Book objects (composition)
        self.__users = []  # Private list of User objects (composition)
        self.__borrowed_records = {}  # {user_id: [book_ids]}
        self._creation_date = datetime.now()
    
    # ========================================================================
    # CONCEPT 17: Public Interface Methods (Encapsulation)
    # ========================================================================
    
    @property
    def books(self):
        """Getter for books - returns copy to maintain encapsulation"""
        return self.__books.copy()
    
    @property
    def users(self):
        """Getter for users"""
        return self.__users.copy()
    
    def add_book(self, book):
        """
        Add a book to the library.
        Demonstrates polymorphism - accepts any LibraryItem subclass.
        """
        if isinstance(book, LibraryItem):
            self.__books.append(book)
            print(f"✓ Added: {book.get_info()}")
            return True
        print("✗ Invalid book object")
        return False
    
    def register_user(self, user):
        """Register a new user"""
        if isinstance(user, User):
            self.__users.append(user)
            self.__borrowed_records[user.user_id] = []
            print(f"✓ Registered: {user.get_user_info()}")
            return True
        return False
    
    def find_book_by_id(self, book_id):
        """Find a book by its ID"""
        for book in self.__books:
            if book.book_id == book_id:
                return book
        return None
    
    def find_user_by_id(self, user_id):
        """Find a user by their ID"""
        for user in self.__users:
            if user.user_id == user_id:
                return user
        return None
    
    def borrow_book(self, user_id, book_id):
        """
        Process book borrowing.
        Demonstrates interaction between multiple objects.
        """
        user = self.find_user_by_id(user_id)
        book = self.find_book_by_id(book_id)
        
        if not user:
            print(f"✗ User {user_id} not found")
            return False
        
        if not book:
            print(f"✗ Book {book_id} not found")
            return False
        
        # Check if user can borrow (polymorphic behavior)
        if not user.can_borrow():
            print(f"✗ {user.name} cannot borrow (reached limit or has fines)")
            return False
        
        # Try to borrow the book
        if book.borrow(user_id):
            user.borrow_book(book_id)
            self.__borrowed_records[user_id].append(book_id)
            print(f"✓ {user.name} borrowed '{book.title}'")
            return True
        else:
            print(f"✗ '{book.title}' is not available")
            return False
    
    def return_book(self, user_id, book_id):
        """Process book return and calculate late fees"""
        user = self.find_user_by_id(user_id)
        book = self.find_book_by_id(book_id)
        
        if not user or not book:
            return False
        
        days_borrowed = book.return_book()
        user.return_book(book_id)
        
        if book_id in self.__borrowed_records.get(user_id, []):
            self.__borrowed_records[user_id].remove(book_id)
        
        # Calculate late fee (polymorphic - different for Book vs EBook)
        borrow_period = 14
        if hasattr(user, 'bonus_borrow_days'):  # Premium user
            borrow_period += user.bonus_borrow_days
        
        if days_borrowed > borrow_period:
            days_late = days_borrowed - borrow_period
            late_fee = book.calculate_late_fee(days_late)
            user.add_fine(late_fee)
            print(f"✓ {user.name} returned '{book.title}' - Late fee: ${late_fee:.2f}")
        else:
            print(f"✓ {user.name} returned '{book.title}' - On time!")
        
        return True
    
    def display_books(self):
        """Display all books - demonstrates polymorphism"""
        print("\n--- Library Books ---")
        if not self.__books:
            print("No books in library")
            return
        
        for book in self.__books:
            # Polymorphic call - different output for Book vs EBook
            print(f"  {book.get_info()}")
    
    def get_user_borrowed_books(self, user_id):
        """Get list of books borrowed by a user"""
        return self.__borrowed_records.get(user_id, [])
    
    def __str__(self):
        return f"Library: {self.name} ({len(self.__books)} books, {len(self.__users)} users)"