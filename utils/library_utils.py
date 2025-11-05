"""
library_utils.py
================
Utility functions for the Library Tracker system.

Demonstrates:
- CONCEPT 13: Functions Part 1 - Basics, syntax, definition, calling
- CONCEPT 14: Functions Part 2 - return, map, filter, reduce
- CONCEPT 15: Functions Part 3 - zip, variable scope
"""

from functools import reduce
from datetime import datetime, timedelta


# ============================================================================
# CONCEPT 13: FUNCTIONS PART 1 - Basic Function Definition
# ============================================================================
# Functions are reusable blocks of code that perform specific tasks
# Syntax: def function_name(parameters):

def generate_book_id(last_id):
    """
    Simple function that generates a new book ID.
    
    Components:
    - def: keyword to define a function
    - generate_book_id: function name (should be descriptive)
    - (last_id): parameter - input to the function
    - docstring: describes what the function does
    - return: sends a value back to the caller
    """
    new_id = last_id + 1
    return new_id  # CONCEPT 14: return statement sends value back


def greet_user(name, greeting="Hello"):
    """
    Function with default parameter value.
    If 'greeting' is not provided, it defaults to "Hello".
    """
    message = f"{greeting}, {name}! Welcome to the library."
    return message


def calculate_fine(days_late, rate_per_day=0.50):
    """
    Calculate late return fine.
    
    Parameters:
    - days_late: required parameter
    - rate_per_day: optional parameter with default value
    """
    if days_late <= 0:
        return 0.0
    
    fine = days_late * rate_per_day
    return round(fine, 2)


def format_book_info(book_dict):
    """
    Format book information into a readable string.
    Demonstrates working with dictionary parameters.
    """
    title = book_dict.get('title', 'Unknown')
    author = book_dict.get('author', 'Unknown')
    year = book_dict.get('year', 'N/A')
    
    # Multiple return statements based on conditions
    if not book_dict:
        return "No book information available"
    
    return f"'{title}' by {author} ({year})"


def print_book_details(title, author, year, genre="General"):
    """
    Function that doesn't return a value (implicitly returns None).
    Used for side effects (like printing).
    """
    print(f"Title: {title}")
    print(f"Author: {author}")
    print(f"Year: {year}")
    print(f"Genre: {genre}")
    # No return statement - function returns None


def get_library_stats(total_books, borrowed_books):
    """
    Function returning multiple values (actually returns a tuple).
    """
    available = total_books - borrowed_books
    borrow_rate = (borrowed_books / total_books * 100) if total_books > 0 else 0
    
    # Returning multiple values (packed into a tuple)
    return total_books, borrowed_books, available, borrow_rate


# ============================================================================
# CONCEPT 13: Functions with *args and **kwargs
# ============================================================================

def add_books_to_collection(*book_titles):
    """
    *args allows function to accept any number of positional arguments.
    Arguments are received as a tuple.
    """
    print(f"Adding {len(book_titles)} books to collection:")
    for i, title in enumerate(book_titles, 1):
        print(f"  {i}. {title}")
    return len(book_titles)


def create_book_entry(book_id, title, **additional_info):
    """
    **kwargs allows function to accept any number of keyword arguments.
    Arguments are received as a dictionary.
    """
    book = {
        'id': book_id,
        'title': title
    }
    
    # Add all additional keyword arguments to the book dictionary
    for key, value in additional_info.items():
        book[key] = value
    
    return book


def process_book_order(*books, **options):
    """
    Combining *args and **kwargs in one function.
    """
    print(f"Processing order for {len(books)} books")
    for book in books:
        print(f"  - {book}")
    
    print("Options:")
    for key, value in options.items():
        print(f"  {key}: {value}")


# ============================================================================
# CONCEPT 14: FUNCTIONS PART 2 - map, filter, reduce
# ============================================================================
# These are functional programming tools that work with functions and iterables

def demonstrate_map_filter_reduce():
    """
    Comprehensive demonstration of map, filter, and reduce functions.
    """
    print("\n" + "="*60)
    print("DEMONSTRATING map, filter, reduce")
    print("="*60)
    
    # Sample data: list of books with prices
    books = [
        {"title": "Python Basics", "price": 29.99},
        {"title": "Java Guide", "price": 34.50},
        {"title": "Web Development", "price": 25.00},
        {"title": "Data Science", "price": 45.00},
        {"title": "Clean Code", "price": 38.75}
    ]
    
    # ========================================================================
    # MAP: Apply a function to every item in an iterable
    # ========================================================================
    # Syntax: map(function, iterable)
    # Returns an iterator that applies function to every item
    
    print("\n1. MAP EXAMPLES:")
    
    # Example 1: Get all book titles in uppercase
    def uppercase_title(book):
        return book['title'].upper()
    
    uppercase_titles = list(map(uppercase_title, books))
    print(f"Uppercase titles: {uppercase_titles}")
    
    # Example 2: Using lambda with map (lambda is anonymous function)
    # Lambda syntax: lambda parameters: expression
    prices = list(map(lambda book: book['price'], books))
    print(f"All prices: {prices}")
    
    # Example 3: Apply discount to all prices
    def apply_discount(book):
        discounted_book = book.copy()
        discounted_book['price'] = round(book['price'] * 0.9, 2)  # 10% discount
        return discounted_book
    
    discounted_books = list(map(apply_discount, books))
    print("\nBooks with 10% discount:")
    for book in discounted_books:
        print(f"  {book['title']}: ${book['price']}")
    
    # ========================================================================
    # FILTER: Filter items based on a condition
    # ========================================================================
    # Syntax: filter(function, iterable)
    # Returns an iterator with items where function returns True
    
    print("\n2. FILTER EXAMPLES:")
    
    # Example 1: Get books under $30
    def is_affordable(book):
        return book['price'] < 30
    
    affordable_books = list(filter(is_affordable, books))
    print("Affordable books (under $30):")
    for book in affordable_books:
        print(f"  {book['title']}: ${book['price']}")
    
    # Example 2: Using lambda with filter
    expensive_books = list(filter(lambda book: book['price'] >= 35, books))
    print("\nExpensive books ($35+):")
    for book in expensive_books:
        print(f"  {book['title']}: ${book['price']}")
    
    # Example 3: Filter books with 'Python' or 'Java' in title
    programming_books = list(filter(lambda book: 'Python' in book['title'] or 'Java' in book['title'], books))
    print(f"\nProgramming books: {[b['title'] for b in programming_books]}")
    
    # ========================================================================
    # REDUCE: Reduce an iterable to a single value
    # ========================================================================
    # Syntax: reduce(function, iterable, initial_value)
    # Applies function cumulatively to items, from left to right
    # Must import from functools: from functools import reduce
    
    print("\n3. REDUCE EXAMPLES:")
    
    # Example 1: Calculate total price of all books
    def add_prices(total, book):
        """
        Accumulator function for reduce.
        - total: accumulated result so far
        - book: current item being processed
        """
        return total + book['price']
    
    total_price = reduce(add_prices, books, 0)  # 0 is initial value
    print(f"Total price of all books: ${total_price:.2f}")
    
    # Example 2: Using lambda with reduce
    max_price = reduce(lambda max_so_far, book: max(max_so_far, book['price']), books, 0)
    print(f"Most expensive book price: ${max_price:.2f}")
    
    # Example 3: Find book with longest title
    def longer_title(book1, book2):
        return book1 if len(book1['title']) > len(book2['title']) else book2
    
    longest_title_book = reduce(longer_title, books)
    print(f"Book with longest title: '{longest_title_book['title']}'")
    
    # Example 4: Combine map and reduce - get sum of discounted prices
    discounted_prices = map(lambda book: book['price'] * 0.9, books)
    total_discounted = reduce(lambda a, b: a + b, discounted_prices, 0)
    print(f"Total price after 10% discount: ${total_discounted:.2f}")
    
    # ========================================================================
    # Combining map, filter, and reduce
    # ========================================================================
    print("\n4. COMBINING map, filter, reduce:")
    
    # Task: Find total price of books under $35 after applying 10% discount
    
    # Step 1: Filter books under $35
    filtered = filter(lambda book: book['price'] < 35, books)
    
    # Step 2: Apply 10% discount
    discounted = map(lambda book: book['price'] * 0.9, filtered)
    
    # Step 3: Sum up the prices
    total = reduce(lambda a, b: a + b, discounted, 0)
    
    print(f"Total cost of affordable books with discount: ${total:.2f}")


def apply_to_prices(books, operation):
    """
    Higher-order function: accepts a function as parameter.
    Demonstrates functions as first-class objects.
    """
    return list(map(lambda book: {**book, 'price': operation(book['price'])}, books))


# ============================================================================
# CONCEPT 15: FUNCTIONS PART 3 - zip function
# ============================================================================

def demonstrate_zip_function():
    """
    Demonstrating the zip function which combines multiple iterables.
    """
    print("\n" + "="*60)
    print("DEMONSTRATING zip FUNCTION")
    print("="*60)
    
    # zip() takes multiple iterables and returns an iterator of tuples
    # Each tuple contains elements from all iterables at the same position
    
    # Example 1: Basic zip
    book_ids = [101, 102, 103, 104]
    book_titles = ["Python Basics", "Java Guide", "Web Dev", "Data Science"]
    authors = ["Alice", "Bob", "Charlie", "Diana"]
    
    # Zip combines them into pairs
    books_combined = list(zip(book_ids, book_titles, authors))
    print("\nZipped books (list of tuples):")
    for book in books_combined:
        print(f"  {book}")
    
    # Example 2: Using zip to create a dictionary
    book_dict = dict(zip(book_ids, book_titles))
    print(f"\nBook ID to Title dictionary: {book_dict}")
    
    # Example 3: Unpacking with zip
    print("\nIterating with zip:")
    for book_id, title, author in zip(book_ids, book_titles, authors):
        print(f"  Book #{book_id}: '{title}' by {author}")
    
    # Example 4: Zip with different length iterables (stops at shortest)
    short_list = [1, 2]
    long_list = ['a', 'b', 'c', 'd']
    zipped = list(zip(short_list, long_list))
    print(f"\nZip with different lengths: {zipped}")  # [(1, 'a'), (2, 'b')]
    
    # Example 5: Unzipping - reverse of zip
    pairs = [(1, 'a'), (2, 'b'), (3, 'c')]
    numbers, letters = zip(*pairs)  # * unpacks the list
    print(f"\nUnzipped - Numbers: {numbers}, Letters: {letters}")
    
    # Example 6: Creating book objects from parallel lists
    years = [2020, 2021, 2022, 2023]
    
    def create_book_summary(book_id, title, author, year):
        return f"[{book_id}] {title} by {author} ({year})"
    
    print("\nBook summaries using zip:")
    for book_id, title, author, year in zip(book_ids, book_titles, authors, years):
        summary = create_book_summary(book_id, title, author, year)
        print(f"  {summary}")


# ============================================================================
# CONCEPT 15: VARIABLE SCOPE (Local, Enclosing, Global, Built-in)
# ============================================================================
# Python uses LEGB rule for variable lookup:
# Local -> Enclosing -> Global -> Built-in

# Global variable (accessible throughout the module)
library_name = "Python Learning Library"
total_inventory = 1000
fine_rate = 0.50


def demonstrate_variable_scope():
    """
    Demonstrating different variable scopes in Python.
    """
    print("\n" + "="*60)
    print("DEMONSTRATING VARIABLE SCOPE")
    print("="*60)
    
    # ========================================================================
    # 1. LOCAL SCOPE
    # ========================================================================
    # Variables defined inside a function are local to that function
    
    def calculate_total():
        # local_books is LOCAL - only exists inside this function
        local_books = 50
        local_price = 25.00
        total = local_books * local_price
        print(f"Local calculation: {local_books} books × ${local_price} = ${total}")
        return total
    
    calculate_total()
    # print(local_books)  # This would cause NameError - local_books doesn't exist here
    
    # ========================================================================
    # 2. GLOBAL SCOPE
    # ========================================================================
    # Variables defined at module level are global
    
    def display_library_info():
        # Reading global variable (no problem)
        print(f"Library name (global): {library_name}")
        print(f"Total inventory (global): {total_inventory}")
    
    display_library_info()
    
    # ========================================================================
    # 3. Modifying global variables
    # ========================================================================
    
    def update_inventory_wrong():
        # This creates a NEW local variable, doesn't modify global
        total_inventory = 900
        print(f"Inside function: {total_inventory}")
    
    print(f"\nBefore wrong update: {total_inventory}")
    update_inventory_wrong()
    print(f"After wrong update: {total_inventory}")  # Still 1000!
    
    def update_inventory_correct():
        # Use 'global' keyword to modify global variable
        global total_inventory
        total_inventory = 900
        print(f"Inside function: {total_inventory}")
    
    print(f"\nBefore correct update: {total_inventory}")
    update_inventory_correct()
    print(f"After correct update: {total_inventory}")  # Now 900!
    
    # ========================================================================
    # 4. ENCLOSING SCOPE (Nested Functions)
    # ========================================================================
    
    def outer_function():
        # This variable is in enclosing scope for inner_function
        outer_var = "I'm from outer function"
        multiplier = 2
        
        def inner_function():
            # Can access variables from enclosing (outer) function
            inner_var = "I'm from inner function"
            print(f"  Inner sees outer_var: {outer_var}")
            print(f"  Inner sees inner_var: {inner_var}")
            
            # Can read enclosing variable
            result = 10 * multiplier
            print(f"  Using enclosing multiplier: 10 × {multiplier} = {result}")
        
        print("Calling inner function:")
        inner_function()
        # print(inner_var)  # NameError - inner_var not accessible here
    
    outer_function()
    
    # ========================================================================
    # 5. nonlocal keyword (for nested functions)
    # ========================================================================
    
    def counter_function():
        count = 0  # Enclosing variable
        
        def increment():
            nonlocal count  # Allows modifying enclosing variable
            count += 1
            return count
        
        print(f"\nCounter starts at: {count}")
        print(f"After 1st increment: {increment()}")
        print(f"After 2nd increment: {increment()}")
        print(f"After 3rd increment: {increment()}")
    
    counter_function()
    
    # ========================================================================
    # 6. Built-in scope
    # ========================================================================
    # Python has built-in functions like print, len, max, etc.
    
    def demonstrate_builtin():
        # These are built-in functions - available everywhere
        numbers = [1, 5, 3, 9, 2]
        print(f"Max: {max(numbers)}, Min: {min(numbers)}, Len: {len(numbers)}")
    
    print()
    demonstrate_builtin()
    
    # You can shadow built-in names (not recommended!)
    def shadow_builtin():
        max = 100  # Shadows built-in max() function locally
        print(f"Local max: {max}")
        # Can't use max() function here anymore!
    
    shadow_builtin()
    print(f"Built-in max still works outside: {max([1, 2, 3])}")


# ============================================================================
# Additional utility functions for the library system
# ============================================================================

def validate_isbn(isbn):
    """
    Validate ISBN-10 or ISBN-13 format.
    Demonstrates complex string processing.
    """
    # Remove hyphens and spaces
    isbn_clean = isbn.replace('-', '').replace(' ', '')
    
    # Check if it's ISBN-10 or ISBN-13
    if len(isbn_clean) == 10:
        # ISBN-10 validation
        if not (isbn_clean[:-1].isdigit() and (isbn_clean[-1].isdigit() or isbn_clean[-1].upper() == 'X')):
            return False
        return True
    elif len(isbn_clean) == 13:
        # ISBN-13 validation (basic check)
        return isbn_clean.isdigit()
    
    return False


def binary_permission_check(permissions, flag):
    """
    Check if a specific permission bit is set using bitwise operations.
    Used with CONCEPT 9: Bitwise Operators
    """
    return (permissions & flag) != 0


def format_date(date_obj):
    """
    Format a datetime object into readable string.
    """
    return date_obj.strftime("%Y-%m-%d %H:%M:%S")


def parse_book_csv_line(csv_line):
    """
    Parse a CSV line into a book dictionary.
    Example: "101,Python Guide,John Doe,2023,Programming"
    """
    parts = csv_line.strip().split(',')
    if len(parts) >= 5:
        return {
            'id': int(parts[0]),
            'title': parts[1],
            'author': parts[2],
            'year': int(parts[3]),
            'genre': parts[4]
        }
    return None


def search_books(books, query):
    """
    Search books by title or author using filter and lambda.
    """
    query_lower = query.lower()
    return list(filter(
        lambda book: query_lower in book.title.lower() or query_lower in book.author.lower(),
        books
    ))


def sort_books_by_title(books):
    """
    Sort books alphabetically by title.
    Returns a new sorted list.
    """
    return sorted(books, key=lambda book: book.title.lower())


def sort_books_by_year(books, reverse=False):
    """
    Sort books by publication year.
    """
    return sorted(books, key=lambda book: book.year, reverse=reverse)


def group_books_by_genre(books):
    """
    Group books by genre using reduce and dictionaries.
    """
    def group_reducer(grouped, book):
        genre = book.get_genre() if hasattr(book, 'get_genre') else 'Unknown'
        if genre not in grouped:
            grouped[genre] = []
        grouped[genre].append(book)
        return grouped
    
    return reduce(group_reducer, books, {})


# Lambda functions stored as variables (demonstrating functions as first-class objects)
get_book_title = lambda book: book.title
is_book_available = lambda book: book.is_available()
calculate_discount_price = lambda price, discount: round(price * (1 - discount), 2)