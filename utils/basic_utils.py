# ============================================================================
# CONCEPT 2: PYTHON OPERATORS
# ============================================================================
def demonstrate_operators():
    """
    Demonstrating arithmetic, comparison, logical, assignment, and membership operators
    in the context of library operations.
    """
    print("\n" + "="*60)
    print("DEMONSTRATING OPERATORS")
    print("="*60)
    
    # Arithmetic operators: +, -, *, /, //, %, **
    total_books = 100
    borrowed_books = 37
    available_books = total_books - borrowed_books  # Subtraction
    print(f"Available books: {total_books} - {borrowed_books} = {available_books}")
    
    # Using modulo to check if book count is even or odd
    if total_books % 2 == 0:  # % is modulo operator
        print(f"Total books ({total_books}) is an even number")
    
    # Floor division for calculating shelf requirements
    books_per_shelf = 15
    shelves_needed = total_books // books_per_shelf  # // is floor division
    print(f"Shelves needed: {total_books} // {books_per_shelf} = {shelves_needed}")
    
    # Comparison operators: ==, !=, >, <, >=, <=
    if borrowed_books > available_books:
        print("More books are borrowed than available!")
    
    # Logical operators: and, or, not
    user_age = 25
    has_membership = True
    can_borrow = (user_age >= 18) and has_membership  # Both conditions must be True
    print(f"Can user borrow? {can_borrow}")
    
    # Identity operators: is, is not
    book1 = None
    if book1 is None:
        print("Book1 is not assigned")
    
    # Membership operators: in, not in
    genres = ["Fiction", "Science", "History", "Biography"]
    if "Fiction" in genres:
        print("Fiction genre is available")
    
    # Assignment operators: =, +=, -=, *=, /=
    late_fee = 0.0
    late_fee += 2.50  # Compound assignment: late_fee = late_fee + 2.50
    late_fee *= 2     # late_fee = late_fee * 2
    print(f"Total late fee after calculations: ${late_fee:.2f}")


# ============================================================================
# CONCEPT 7: STRINGS PART 1 - Representation, Indexing, Slicing
# ============================================================================
def demonstrate_string_operations(book_title="The Python Programming Guide"):
    """
    Demonstrating string indexing, slicing, and memory representation concepts.
    """
    print("\n" + "="*60)
    print("DEMONSTRATING STRING OPERATIONS")
    print("="*60)
    
    # Strings are immutable sequences of characters stored in memory
    # Each character has an index: 0, 1, 2, ... or -1, -2, -3, ... (from end)
    
    print(f"Book title: '{book_title}'")
    
    # Indexing: Access individual characters
    first_char = book_title[0]  # 'T'
    last_char = book_title[-1]   # 'e'
    print(f"First character: '{first_char}', Last character: '{last_char}'")
    
    # Slicing: Extract substrings using [start:end:step]
    # Format: string[start:end] - gets characters from start to end-1
    first_word = book_title[0:3]  # "The"
    print(f"First word (using slice [0:3]): '{first_word}'")
    
    # Negative indices in slicing
    last_five = book_title[-5:]  # "Guide"
    print(f"Last 5 characters: '{last_five}'")
    
    # Step in slicing: every nth character
    every_second = book_title[::2]  # Every 2nd character
    print(f"Every 2nd character: '{every_second}'")
    
    # Reverse a string using slicing
    reversed_title = book_title[::-1]
    print(f"Reversed title: '{reversed_title}'")
    
    # Slicing to get middle portion
    middle_portion = book_title[4:10]  # "Python"
    print(f"Middle portion [4:10]: '{middle_portion}'")


# ============================================================================
# CONCEPT 8: STRINGS PART 2 - Built-in Functions, Formatting, Conversions
# ============================================================================
def demonstrate_string_functions(isbn="978-0-13-444432-1"):
    """
    Demonstrating string methods, formatting, and type conversions.
    """
    print("\n" + "="*60)
    print("DEMONSTRATING STRING FUNCTIONS & FORMATTING")
    print("="*60)
    
    # String methods
    title = "  python programming  "
    print(f"Original: '{title}'")
    print(f"Upper: '{title.upper()}'")  # Convert to uppercase
    print(f"Title case: '{title.title()}'")  # Capitalize each word
    print(f"Stripped: '{title.strip()}'")  # Remove leading/trailing whitespace
    
    # String checking methods
    print(f"ISBN '{isbn}' is alphanumeric? {isbn.replace('-', '').isalnum()}")
    
    # String formatting - Multiple approaches
    book_id = 101
    book_name = "Python Basics"
    price = 29.99
    
    # Method 1: % formatting (old style)
    formatted1 = "Book #%d: %s costs $%.2f" % (book_id, book_name, price)
    print(f"% formatting: {formatted1}")
    
    # Method 2: .format() method
    formatted2 = "Book #{}: {} costs ${:.2f}".format(book_id, book_name, price)
    print(f".format() method: {formatted2}")
    
    # Method 3: f-strings (modern, preferred)
    formatted3 = f"Book #{book_id}: {book_name} costs ${price:.2f}"
    print(f"f-string: {formatted3}")
    
    # Decimal to Binary conversion (demonstrating type conversion)
    book_id_binary = bin(book_id)  # Converts decimal to binary string
    book_id_hex = hex(book_id)     # Converts decimal to hexadecimal
    book_id_octal = oct(book_id)   # Converts decimal to octal
    
    print(f"\nBook ID {book_id} in different bases:")
    print(f"  Binary: {book_id_binary}")
    print(f"  Hexadecimal: {book_id_hex}")
    print(f"  Octal: {book_id_octal}")
    
    # Converting back from binary string to integer
    binary_str = "1100101"  # This is 101 in decimal
    decimal_value = int(binary_str, 2)  # The '2' specifies binary base
    print(f"\nBinary '{binary_str}' to decimal: {decimal_value}")


# ============================================================================
# CONCEPT 9: BITWISE OPERATORS
# ============================================================================
def demonstrate_bitwise_operations():
    """
    Demonstrating bitwise operators through user permission management.
    Bitwise operators work on binary representations of numbers.
    """
    print("\n" + "="*60)
    print("DEMONSTRATING BITWISE OPERATORS")
    print("="*60)
    
    # Using bitwise flags for user permissions (common in systems programming)
    # Each bit represents a different permission
    CAN_BORROW = 1      # Binary: 0001
    CAN_RESERVE = 2     # Binary: 0010
    CAN_RENEW = 4       # Binary: 0100
    IS_PREMIUM = 8      # Binary: 1000
    
    # Using bitwise OR (|) to combine permissions
    basic_user_permissions = CAN_BORROW | CAN_RESERVE  # 0001 | 0010 = 0011 (3)
    print(f"Basic user permissions: {basic_user_permissions} (binary: {bin(basic_user_permissions)})")
    
    premium_user_permissions = CAN_BORROW | CAN_RESERVE | CAN_RENEW | IS_PREMIUM
    print(f"Premium user permissions: {premium_user_permissions} (binary: {bin(premium_user_permissions)})")
    
    # Using bitwise AND (&) to check if a specific permission exists
    user_perms = basic_user_permissions
    can_user_borrow = (user_perms & CAN_BORROW) != 0
    can_user_renew = (user_perms & CAN_RENEW) != 0
    print(f"\nChecking basic user: Can borrow? {can_user_borrow}, Can renew? {can_user_renew}")
    
    # Bitwise XOR (^) - toggles bits
    toggled = basic_user_permissions ^ CAN_RESERVE  # Removes CAN_RESERVE
    print(f"After toggling RESERVE permission: {toggled}")
    
    # Bitwise NOT (~) - inverts all bits
    inverted = ~CAN_BORROW  # This will give negative number in Python due to two's complement
    print(f"Bitwise NOT of CAN_BORROW: {inverted}")
    
    # Left shift (<<) and Right shift (>>)
    # Left shift by n is equivalent to multiplying by 2^n
    shifted_left = CAN_BORROW << 2  # 0001 << 2 = 0100 (multiply by 4)
    print(f"CAN_BORROW << 2 = {shifted_left} (equivalent to {CAN_BORROW} * 4)")
    
    # Right shift by n is equivalent to integer division by 2^n
    shifted_right = IS_PREMIUM >> 2  # 1000 >> 2 = 0010 (divide by 4)
    print(f"IS_PREMIUM >> 2 = {shifted_right} (equivalent to {IS_PREMIUM} // 4)")


# ============================================================================
# CONCEPT 10: LOOPS - while loop, break, continue
# ============================================================================
def demonstrate_while_loop():
    """
    Demonstrating while loops with break and continue statements.
    Used for processing user actions until they choose to exit.
    """
    print("\n" + "="*60)
    print("DEMONSTRATING WHILE LOOP")
    print("="*60)
    
    # Simulating a book search where user keeps searching until they type 'quit'
    search_count = 0
    search_queries = ["Python", "", "Java", "quit", "C++"]  # Simulated inputs
    
    query_index = 0
    while query_index < len(search_queries):  # while condition is True, loop continues
        search_query = search_queries[query_index]
        query_index += 1
        search_count += 1
        
        # 'break' exits the loop immediately
        if search_query.lower() == "quit":
            print("User chose to quit. Exiting search...")
            break  # Exit the while loop
        
        # 'continue' skips the rest of the current iteration and goes to next iteration
        if search_query == "":
            print("Empty search query. Please try again.")
            continue  # Skip to next iteration
        
        print(f"Searching for books about '{search_query}'...")
    
    print(f"Total search attempts: {search_count}")
    
    # Another example: Processing book returns with validation
    print("\nProcessing book returns:")
    books_to_return = [101, 0, 102, -5, 103]  # Some invalid IDs
    index = 0
    
    while index < len(books_to_return):
        book_id = books_to_return[index]
        index += 1
        
        # Skip invalid book IDs
        if book_id <= 0:
            print(f"  Invalid book ID: {book_id} - Skipping...")
            continue
        
        print(f"  Processing return for book ID: {book_id}")
        
        # Could add a break condition, e.g., if system error occurs
        if book_id == 999:  # Simulated error condition
            print("  System error! Stopping processing.")
            break


# ============================================================================
# CONCEPT 11: LOOPS - for loop
# ============================================================================
def demonstrate_for_loop(books_list):
    """
    Demonstrating for loops for iterating over sequences.
    For loops are used when you know the number of iterations or have a sequence to iterate over.
    """
    print("\n" + "="*60)
    print("DEMONSTRATING FOR LOOP")
    print("="*60)
    
    # Iterating over a list of book titles
    print("Book titles in our collection:")
    for book in books_list:  # 'for' iterates over each element in the sequence
        print(f"  - {book}")
    
    # Using range() with for loop
    print("\nDisplaying first 5 book IDs:")
    for book_id in range(1, 6):  # range(start, stop) generates numbers from start to stop-1
        print(f"  Book ID: {book_id}")
    
    # Iterating with index using enumerate()
    print("\nBooks with their positions:")
    for index, book in enumerate(books_list, start=1):  # enumerate adds counter to iteration
        print(f"  {index}. {book}")
    
    # Nested for loops - useful for multi-dimensional data
    print("\nLibrary sections and their book counts:")
    sections = {
        "Fiction": 45,
        "Science": 32,
        "History": 28
    }
    
    for section, count in sections.items():  # .items() gives key-value pairs
        print(f"  {section} section:")
        # Inner loop to display shelf distribution (just as example)
        books_per_shelf = 10
        shelves = count // books_per_shelf
        for shelf_num in range(1, shelves + 1):
            print(f"    Shelf {shelf_num}: ~{books_per_shelf} books")


# ============================================================================
# CONCEPT 12: COMPREHENSIONS (List, Dictionary, Set)
# ============================================================================
def demonstrate_comprehensions(sample_books):
    """
    Demonstrating list, dictionary, and set comprehensions.
    Comprehensions provide concise syntax for creating collections from iterables.
    """
    print("\n" + "="*60)
    print("DEMONSTRATING COMPREHENSIONS")
    print("="*60)
    
    # List Comprehension: [expression for item in iterable if condition]
    # Creates a new list by applying an expression to each item
    
    # Example: Get all book titles in uppercase
    uppercase_titles = [book['title'].upper() for book in sample_books]
    print("Book titles in uppercase (list comprehension):")
    print(f"  {uppercase_titles}")
    
    # List comprehension with condition
    # Get only available books (not borrowed)
    available_books = [book['title'] for book in sample_books if book['available']]
    print(f"\nAvailable books: {available_books}")
    
    # Dictionary Comprehension: {key_expr: value_expr for item in iterable}
    # Creates a dictionary from an iterable
    
    # Example: Create a dictionary mapping book ID to title
    book_id_to_title = {book['id']: book['title'] for book in sample_books}
    print("\nBook ID to Title mapping (dict comprehension):")
    for book_id, title in book_id_to_title.items():
        print(f"  ID {book_id}: {title}")
    
    # Dictionary comprehension with condition
    # Get only borrowed books with their IDs
    borrowed_books = {book['id']: book['title'] for book in sample_books if not book['available']}
    print(f"\nBorrowed books: {borrowed_books}")
    
    # Set Comprehension: {expression for item in iterable}
    # Creates a set (unique values) from an iterable
    
    # Example: Get unique genres from all books
    all_genres = {book['genre'] for book in sample_books}
    print(f"\nUnique genres in library (set comprehension): {all_genres}")
    
    # Nested comprehension example
    # Flatten a list of lists (e.g., books organized by shelves)
    shelves = [
        ["Book A", "Book B"],
        ["Book C", "Book D", "Book E"],
        ["Book F"]
    ]
    all_books_flat = [book for shelf in shelves for book in shelf]
    print(f"\nFlattened book list: {all_books_flat}")


# ============================================================================
# CONCEPT 3: input() and Type Casting
# ============================================================================
def get_user_input_demo():
    """
    Demonstrating user input and type casting.
    input() always returns a string, so we need to cast it to appropriate types.
    """
    print("\n" + "="*60)
    print("DEMONSTRATING input() AND TYPE CASTING")
    print("="*60)
    
    # For demonstration purposes, we'll use predefined values
    # In a real scenario, you would use input() to get user input
    
    # Simulating user inputs (in real use, these would be input() calls)
    print("Simulating user registration...")
    
    # String input (no casting needed)
    user_name = "Alice Johnson"  # Would be: input("Enter your name: ")
    print(f"Name entered: {user_name}")
    
    # Integer casting: Converting string to int
    age_input = "25"  # Would be: input("Enter your age: ")
    user_age = int(age_input)  # Type casting string to integer
    print(f"Age entered: {user_age} (type: {type(user_age).__name__})")
    
    # Float casting: Converting string to float
    fine_input = "15.50"  # Would be: input("Enter fine amount: $")
    fine_amount = float(fine_input)  # Type casting string to float
    print(f"Fine amount: ${fine_amount:.2f} (type: {type(fine_amount).__name__})")
    
    # Boolean casting: Converting to boolean
    membership_input = "yes"  # Would be: input("Do you have membership? (yes/no): ")
    has_membership = membership_input.lower() in ['yes', 'y', 'true', '1']
    print(f"Has membership: {has_membership} (type: {type(has_membership).__name__})")
    
    # Handling conversion errors with try-except (preview of exception handling)
    invalid_input = "abc123"
    try:
        invalid_number = int(invalid_input)  # This will fail
    except ValueError:
        print(f"Cannot convert '{invalid_input}' to integer - using default value 0")
        invalid_number = 0
    
    # Multiple type conversions
    print("\nDemonstrating various type conversions:")
    print(f"  str(123) = '{str(123)}' (int to string)")
    print(f"  int('456') = {int('456')} (string to int)")
    print(f"  float('78.9') = {float('78.9')} (string to float)")
    print(f"  int(78.9) = {int(78.9)} (float to int - truncates decimal)")
    print(f"  bool(1) = {bool(1)} (int to bool - non-zero is True)")
    print(f"  bool(0) = {bool(0)} (int to bool - zero is False)")


# ============================================================================
# CONCEPT 4: LISTS AND TUPLES
# ============================================================================
def demonstrate_lists_and_tuples():
    """
    Demonstrating lists (mutable) and tuples (immutable) collections.
    """
    print("\n" + "="*60)
    print("DEMONSTRATING LISTS AND TUPLES")
    print("="*60)
    
    # LISTS - Mutable (can be modified), ordered collections
    # Created using square brackets []
    book_titles = ["1984", "Brave New World", "Fahrenheit 451"]
    print(f"Original book list: {book_titles}")
    
    # List operations
    book_titles.append("The Handmaid's Tale")  # Add to end
    print(f"After append: {book_titles}")
    
    book_titles.insert(1, "Animal Farm")  # Insert at specific position
    print(f"After insert at index 1: {book_titles}")
    
    removed_book = book_titles.pop()  # Remove and return last item
    print(f"Removed book: {removed_book}")
    print(f"After pop: {book_titles}")
    
    book_titles.remove("1984")  # Remove specific item
    print(f"After removing '1984': {book_titles}")
    
    # List indexing and slicing
    print(f"First book: {book_titles[0]}")
    print(f"Last book: {book_titles[-1]}")
    print(f"First two books: {book_titles[0:2]}")
    
    # List methods
    book_titles.sort()  # Sort in place
    print(f"After sorting: {book_titles}")
    
    print(f"Number of books: {len(book_titles)}")
    
    # TUPLES - Immutable (cannot be modified), ordered collections
    # Created using parentheses ()
    # Often used for data that shouldn't change (like coordinates, RGB colors, or database records)
    
    book_info = ("Python Crash Course", "Eric Matthes", 2019, "9781593279288")
    print(f"\nBook information tuple: {book_info}")
    
    # Tuple unpacking
    title, author, year, isbn = book_info
    print(f"Title: {title}, Author: {author}, Year: {year}, ISBN: {isbn}")
    
    # Tuples are immutable - this would cause an error:
    # book_info[0] = "New Title"  # TypeError: 'tuple' object does not support item assignment
    
    # But you can access elements
    print(f"Book title from tuple: {book_info[0]}")
    
    # Tuple with single element (note the comma)
    single_item_tuple = ("Only Book",)  # The comma makes it a tuple
    print(f"Single item tuple: {single_item_tuple}, type: {type(single_item_tuple)}")
    
    # Without comma, it's just a string
    not_a_tuple = ("Only Book")
    print(f"Not a tuple: {not_a_tuple}, type: {type(not_a_tuple)}")
    
    # Use case: Returning multiple values from a function returns a tuple
    def get_library_stats():
        return 150, 98, 52  # Returns a tuple
    
    total, borrowed, available = get_library_stats()
    print(f"\nLibrary stats: Total={total}, Borrowed={borrowed}, Available={available}")


# ============================================================================
# CONCEPT 5: SETS AND DICTIONARIES
# ============================================================================
def demonstrate_sets_and_dictionaries():
    """
    Demonstrating sets (unique, unordered) and dictionaries (key-value pairs).
    """
    print("\n" + "="*60)
    print("DEMONSTRATING SETS AND DICTIONARIES")
    print("="*60)
    
    # SETS - Unordered collections of unique elements
    # Created using curly braces {} or set()
    # Great for membership testing and eliminating duplicates
    
    print("SETS:")
    borrowed_by_user1 = {"Python Basics", "Java Fundamentals", "Web Development"}
    borrowed_by_user2 = {"Java Fundamentals", "Database Design", "Python Basics"}
    
    print(f"User 1 borrowed: {borrowed_by_user1}")
    print(f"User 2 borrowed: {borrowed_by_user2}")
    
    # Set operations
    # Union: All unique books borrowed by either user
    all_borrowed = borrowed_by_user1 | borrowed_by_user2  # or .union()
    print(f"All books borrowed (union): {all_borrowed}")
    
    # Intersection: Books borrowed by both users
    common_books = borrowed_by_user1 & borrowed_by_user2  # or .intersection()
    print(f"Books borrowed by both (intersection): {common_books}")
    
    # Difference: Books borrowed by user1 but not user2
    only_user1 = borrowed_by_user1 - borrowed_by_user2  # or .difference()
    print(f"Only user1 borrowed (difference): {only_user1}")
    
    # Symmetric difference: Books borrowed by one user but not both
    exclusive_books = borrowed_by_user1 ^ borrowed_by_user2  # or .symmetric_difference()
    print(f"Exclusively borrowed (symmetric difference): {exclusive_books}")
    
    # Set methods
    genres = set()  # Empty set
    genres.add("Fiction")
    genres.add("Science")
    genres.add("Fiction")  # Duplicate, won't be added
    print(f"\nGenres: {genres}")
    
    # Membership testing (very fast with sets)
    print(f"Is 'Fiction' in genres? {'Fiction' in genres}")
    
    # DICTIONARIES - Collections of key-value pairs
    # Created using curly braces {} with key:value pairs
    # Keys must be unique and immutable (strings, numbers, tuples)
    
    print("\n\nDICTIONARIES:")
    # Dictionary representing a book
    book = {
        "id": 101,
        "title": "Python Programming",
        "author": "John Doe",
        "year": 2023,
        "available": True,
        "copies": 3
    }
    
    print(f"Book dictionary: {book}")
    
    # Accessing values
    print(f"Book title: {book['title']}")  # Using bracket notation
    print(f"Book author: {book.get('author')}")  # Using .get() method (safer)
    
    # .get() with default value (won't raise error if key doesn't exist)
    publisher = book.get('publisher', 'Unknown')
    print(f"Publisher: {publisher}")
    
    # Adding/modifying entries
    book['genre'] = 'Programming'  # Add new key-value pair
    book['copies'] = 5  # Modify existing value
    print(f"After modifications: {book}")
    
    # Dictionary methods
    print(f"\nAll keys: {list(book.keys())}")
    print(f"All values: {list(book.values())}")
    print(f"All items: {list(book.items())}")
    
    # Iterating through dictionary
    print("\nBook details:")
    for key, value in book.items():
        print(f"  {key}: {value}")
    
    # Nested dictionary (dictionary of dictionaries)
    library_catalog = {
        101: {"title": "Book A", "author": "Author 1"},
        102: {"title": "Book B", "author": "Author 2"},
        103: {"title": "Book C", "author": "Author 3"}
    }
    
    print(f"\nLibrary catalog: {library_catalog}")
    print(f"Book 102 details: {library_catalog[102]}")
    
    # Dictionary comprehension (covered in detail in CONCEPT 12)
    squared_ids = {book_id: book_id**2 for book_id in [101, 102, 103]}
    print(f"Squared IDs: {squared_ids}")


# ============================================================================
# CONCEPT 6: CONDITIONAL STATEMENTS (if/else)
# ============================================================================
def demonstrate_conditionals(user_age, book_available, fine_amount):
    """
    Demonstrating if, elif, else statements for decision making.
    """
    print("\n" + "="*60)
    print("DEMONSTRATING CONDITIONAL STATEMENTS")
    print("="*60)
    
    # Simple if statement
    if user_age >= 18:
        print(f"User age {user_age}: Eligible for adult membership")
    
    # if-else statement
    if book_available:
        print("Book status: Available for borrowing")
    else:
        print("Book status: Currently borrowed")
    
    # if-elif-else statement (multiple conditions)
    print(f"\nChecking fine amount: ${fine_amount}")
    if fine_amount == 0:
        print("No outstanding fines - Good standing!")
    elif fine_amount < 5:
        print("Small fine - Please pay at counter")
    elif fine_amount < 20:
        print("Moderate fine - Borrowing restricted until paid")
    else:
        print("Large fine - Membership suspended until paid")
    
    # Nested if statements
    print("\nChecking borrowing eligibility:")
    if user_age >= 13:
        if fine_amount == 0:
            if book_available:
                print("✓ Eligible to borrow this book")
            else:
                print("✗ Book not available")
        else:
            print("✗ Must clear fines first")
    else:
        print("✗ Must be 13 or older")
    
    # Conditional expressions (ternary operator)
    # Format: value_if_true if condition else value_if_false
    status = "Available" if book_available else "Borrowed"
    print(f"\nBook status (using ternary): {status}")
    
    # Multiple conditions with logical operators
    has_membership = True
    is_book_reserved = False
    
    if has_membership and book_available and not is_book_reserved:
        print("✓ Can borrow this book now")
    elif not has_membership:
        print("✗ Need membership to borrow")
    elif is_book_reserved:
        print("✗ Book is reserved by another user")
    else:
        print("✗ Book not currently available")