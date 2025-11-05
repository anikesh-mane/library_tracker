"""
LIBRARY TRACKER - EDUCATIONAL MINI-PROJECT
===========================================
Purpose: Demonstrate all foundational Python concepts through a real-world library management system.

Learning Objectives:
- Apply data types, operators, and control flow in context
- Use collections (lists, tuples, sets, dictionaries) effectively
- Implement Object-Oriented Programming principles
- Handle files and exceptions gracefully
- Work with modules and packages
- Use comprehensions and functional programming tools

This is the main entry point of the application.
"""

# ============================================================================
# CONCEPT 21: MODULES & PACKAGES
# ============================================================================
# Demonstrating importing from custom modules
# We organize code into separate files for maintainability


# Import our custom modules (these will be in separate files)
from library import Library
from books.book import Book
from books.ebook import EBook
from user import User, PremiumUser

from utils.basic_utils import *
from utils.library_utils import (
    generate_book_id, 
    format_book_info, 
    calculate_fine,
    binary_permission_check,
    validate_isbn
)
from files.ops import save_library_data, load_library_data

# ============================================================================
# CONCEPT 1: PYTHON DATA TYPES
# ============================================================================
# Demonstrating various Python data types through library configuration

# Integer: Maximum books a user can borrow
MAX_BOOKS_PER_USER = 3

# Float: Fine per day for late returns
FINE_PER_DAY = 0.50

# String: Library name
LIBRARY_NAME = "Python Learning Library"

# Boolean: Is the library currently open?
is_library_open = True

# Complex number (less common, but showing it exists): Used for advanced calculations
# In real scenarios, might be used for electrical engineering or signal processing
library_complexity_rating = 5 + 3j  # Just demonstrating the data type

# None type: Placeholder for optional values
current_borrowed_book = None


# ============================================================================
# MAIN PROGRAM - Integrating all concepts
# ============================================================================
def main():
    """
    Main function that runs the Library Tracker application.
    This integrates all the demonstrated concepts into a cohesive program.
    """
    print("="*60)
    print(f"WELCOME TO {LIBRARY_NAME}")
    print("="*60)
    
    # # Run all demonstration functions
    # demonstrate_operators()
    
    # # Sample data for demonstrations
    # sample_book_titles = [
    #     "Python Crash Course",
    #     "Clean Code",
    #     "The Pragmatic Programmer",
    #     "Design Patterns"
    # ]
    
    # demonstrate_string_operations()
    # demonstrate_string_functions()
    # demonstrate_bitwise_operations()
    # demonstrate_while_loop()
    # demonstrate_for_loop(sample_book_titles)
    
    # # Sample books for comprehensions
    # sample_books = [
    #     {"id": 101, "title": "Python Basics", "genre": "Programming", "available": True},
    #     {"id": 102, "title": "Java Guide", "genre": "Programming", "available": False},
    #     {"id": 103, "title": "Web Design", "genre": "Design", "available": True},
    #     {"id": 104, "title": "Data Science", "genre": "Programming", "available": True},
    # ]
    
    # demonstrate_comprehensions(sample_books)
    # get_user_input_demo()
    # demonstrate_lists_and_tuples()
    # demonstrate_sets_and_dictionaries()
    # demonstrate_conditionals(user_age=25, book_available=True, fine_amount=2.50)
    
    # # ========================================================================
    # # CONCEPT 13, 14, 15: Functions (will be in library_utils.py)
    # # ========================================================================
    # print("\n" + "="*60)
    # print("DEMONSTRATING FUNCTIONS FROM UTILITY MODULE")
    # print("="*60)
    
    # # Using functions from library_utils module
    # new_book_id = generate_book_id(101)
    # print(f"Generated book ID: {new_book_id}")
    
    # book_details = {"title": "Python Guide", "author": "John Smith", "year": 2023}
    # formatted = format_book_info(book_details)
    # print(f"Formatted book info: {formatted}")
    
    # days_late = 5
    # fine = calculate_fine(days_late)
    # print(f"Fine for {days_late} days late: ${fine:.2f}")
    
    # # Demonstrating bitwise permission function
    # permissions = 7  # CAN_BORROW | CAN_RESERVE | CAN_RENEW
    # can_borrow = binary_permission_check(permissions, 1)
    # print(f"User has borrow permission: {can_borrow}")
    
    # ========================================================================
    # CONCEPT 16, 17, 18, 19: OOP
    # ========================================================================
    print("\n" + "="*60)
    print("DEMONSTRATING OBJECT-ORIENTED PROGRAMMING")
    print("="*60)
    
    # Creating Book objects (demonstrates Constructor)
    book1 = Book(101, "Python Programming", "John Doe", 2023)
    book2 = EBook(102, "Web Development", "Jane Smith", 2024, 5.2, "PDF")
    
    print(f"Total books created: {Book.get_total_books()}")  # Class method
    print(f"\nBook 1: {book1.get_info()}")
    print(f"Book 2: {book2.get_info()}")  # Polymorphism - different implementation
    
    # Creating User objects
    user1 = User("Alice", "alice@email.com", 1001)
    user2 = PremiumUser("Bob", "bob@email.com", 1002, premium_level="Gold")

    print(f"Total users created: {User.total_users}")  # Class method
    print(f"\nUser 1: {user1.get_user_info()}")
    print(f"User 2: {user2.get_user_info()}")  # Inheritance - PremiumUser extends User
    
    # Creating Library object
    library = Library("Python Learning Library")
    
    # Adding books to library
    library.add_book(book1)
    library.add_book(book2)
    
    # Registering users
    library.register_user(user1)
    library.register_user(user2)
    
    # Performing library operations
    print("\n--- Library Operations ---")
    library.display_books()
    
    # Borrow a book (demonstrates encapsulation and method interaction)
    library.borrow_book(1001, 101)
    
    # Try to borrow unavailable book
    library.borrow_book(1002, 101)
    
    # Return a book
    library.return_book(1001, 101)
    
    # # ========================================================================
    # # CONCEPT 20: FILE HANDLING & EXCEPTION HANDLING
    # # ========================================================================
    # print("\n" + "="*60)
    # print("DEMONSTRATING FILE HANDLING & EXCEPTION HANDLING")
    # print("="*60)
    
    # # Save library data to file
    # try:
    #     save_library_data(library, "data/library_data.txt")
    #     print("[SUCCESS] Library data saved successfully")
    # except Exception as e:
    #     print(f"[ERROR] Error saving data: {e}")
    
    # # Load library data from file
    # try:
    #     loaded_library = load_library_data("data/library_data.txt")
    #     print("[SUCCESS] Library data loaded successfully")
    #     print(f"Loaded library: {loaded_library.name}")
    # except FileNotFoundError:
    #     print("[ERROR] Library data file not found")
    # except Exception as e:
    #     print(f"[ERROR] Error loading data: {e}")
    
    # # ========================================================================
    # # Interactive Menu (Simulated)
    # # ========================================================================
    # print("\n" + "="*60)
    # print("LIBRARY MANAGEMENT SYSTEM - INTERACTIVE DEMO")
    # print("="*60)
    
    # # In a real application, this would be a while loop with input()
    # # For demonstration, we'll simulate a few interactions
    
    # print("\nSimulated User Interactions:")
    # print("1. User searches for 'Python'")
    # search_results = [book for book in library.books if 'Python' in book.title]
    # print(f"   Found {len(search_results)} books matching 'Python'")
    
    # print("\n2. User views their borrowed books")
    # user1_books = library.get_user_borrowed_books(1001)
    # print(f"   {user1.name} has {len(user1_books)} books borrowed")
    
    # print("\n3. Display library statistics")
    # total_books = len(library.books)
    # available_books = len([b for b in library.books if b.is_available()])
    # print(f"   Total books: {total_books}")
    # print(f"   Available: {available_books}")
    # print(f"   Borrowed: {total_books - available_books}")
    
    print("\n" + "="*60)
    print("DEMONSTRATION COMPLETE!")
    print("="*60)


# Entry point of the program
if __name__ == "__main__":
    # This block only runs when this file is executed directly
    # Not when it's imported as a module
    main()