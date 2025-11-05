"""
file_operations.py
==================
File handling and exception handling for the Library Tracker system.

Demonstrates:
- CONCEPT 20: File Handling & Exception Handling
"""

import json
import csv
from datetime import datetime


# ============================================================================
# CONCEPT 20: EXCEPTION HANDLING
# ============================================================================
# Exception handling allows graceful error management
# Syntax: try-except-else-finally blocks

class LibraryFileError(Exception):
    """
    Custom exception class for library file operations.
    Demonstrates creating custom exceptions by inheriting from Exception.
    """
    def __init__(self, message, filename=None):
        self.message = message
        self.filename = filename
        super().__init__(self.message)
    
    def __str__(self):
        if self.filename:
            return f"LibraryFileError [{self.filename}]: {self.message}"
        return f"LibraryFileError: {self.message}"


# ============================================================================
# CONCEPT 20: FILE HANDLING - Text Files
# ============================================================================

def save_library_data(library, filename):
    """
    Save library data to a text file.
    
    Demonstrates:
    - Opening files with 'with' statement (context manager)
    - Writing to files
    - Exception handling
    - File modes: 'w' (write), 'r' (read), 'a' (append)
    """
    
    try:
        # 'with' statement ensures file is properly closed even if error occurs
        # 'w' mode opens file for writing (creates if doesn't exist, overwrites if exists)
        with open(filename, 'w', encoding='utf-8') as file:
            # Write library header
            file.write(f"=== {library.name} Data ===\n")
            file.write(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            file.write("="*50 + "\n\n")
            
            # Write books section
            file.write("BOOKS:\n")
            file.write("-"*50 + "\n")
            for book in library.books:
                # Write each book's information
                file.write(f"ID: {book.book_id}\n")
                file.write(f"Title: {book.title}\n")
                file.write(f"Author: {book.author}\n")
                file.write(f"Year: {book.year}\n")
                file.write(f"Available: {book.is_available()}\n")
                file.write("-"*50 + "\n")
            
            # Write users section
            file.write("\nUSERS:\n")
            file.write("-"*50 + "\n")
            for user in library.users:
                file.write(f"ID: {user.user_id}\n")
                file.write(f"Name: {user.name}\n")
                file.write(f"Email: {user.email}\n")
                file.write(f"Borrowed Books: {len(user.get_borrowed_books())}\n")
                file.write(f"Fine: ${user.get_fine_amount():.2f}\n")
                file.write("-"*50 + "\n")
        
        print(f"✓ Successfully saved library data to '{filename}'")
        return True
    
    except PermissionError:
        # Specific exception for permission-related errors
        print(f"✗ Permission denied: Cannot write to '{filename}'")
        return False
    
    except IOError as e:
        # IO errors (Input/Output errors)
        print(f"✗ IO Error while saving: {e}")
        return False
    
    except Exception as e:
        # Catch-all for any other exceptions
        print(f"✗ Unexpected error while saving: {e}")
        return False


def load_library_data(filename):
    """
    Load library data from a text file.
    
    Demonstrates:
    - Reading from files
    - Exception handling with multiple except blocks
    - else clause (executes if no exception occurred)
    - finally clause (always executes)
    """
    
    file_handle = None
    
    try:
        # 'r' mode opens file for reading
        file_handle = open(filename, 'r', encoding='utf-8')
        
        # Read entire file content
        content = file_handle.read()
        
        # Parse the content (simplified parsing for demonstration)
        lines = content.split('\n')
        
        # Extract library name from first line
        library_name = "Loaded Library"
        if lines and '===' in lines[0]:
            library_name = lines[0].replace('===', '').strip().replace(' Data', '')
        
        print(f"✓ Successfully loaded data from '{filename}'")
        
        # For demonstration, we'll return a simple object
        # In a real application, you'd reconstruct the full library
        class SimpleLibrary:
            def __init__(self, name):
                self.name = name
        
        return SimpleLibrary(library_name)
    
    except FileNotFoundError:
        # Raised when file doesn't exist
        print(f"✗ File not found: '{filename}'")
        raise  # Re-raise the exception to caller
    
    except PermissionError:
        # Raised when lacking permission to read file
        print(f"✗ Permission denied: Cannot read '{filename}'")
        raise
    
    except UnicodeDecodeError:
        # Raised when file encoding is incorrect
        print(f"✗ Encoding error: Cannot decode '{filename}'")
        raise
    
    except Exception as e:
        # Catch-all for other exceptions
        print(f"✗ Error loading file: {e}")
        raise
    
    else:
        # This block executes ONLY if no exception occurred
        print("File loaded successfully (else block)")
    
    finally:
        # This block ALWAYS executes, whether exception occurred or not
        # Used for cleanup (closing files, releasing resources)
        if file_handle and not file_handle.closed:
            file_handle.close()
            print("File closed (finally block)")


# ============================================================================
# CONCEPT 20: FILE HANDLING - CSV Files
# ============================================================================

def save_books_to_csv(books, filename):
    """
    Save books to a CSV (Comma-Separated Values) file.
    
    CSV format is common for spreadsheet data.
    Demonstrates using the csv module.
    """
    
    try:
        with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
            # Create CSV writer object
            # fieldnames defines the column headers
            fieldnames = ['id', 'title', 'author', 'year', 'genre', 'available']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            
            # Write header row
            writer.writeheader()
            
            # Write each book as a row
            for book in books:
                writer.writerow({
                    'id': book.book_id,
                    'title': book.title,
                    'author': book.author,
                    'year': book.year,
                    'genre': book.get_genre(),
                    'available': book.is_available()
                })
        
        print(f"✓ Saved {len(books)} books to CSV: '{filename}'")
        return True
    
    except IOError as e:
        print(f"✗ Error saving CSV: {e}")
        return False


def load_books_from_csv(filename):
    """
    Load books from a CSV file.
    
    Demonstrates:
    - Reading CSV files
    - Exception handling
    - Data validation
    """
    
    books_data = []
    
    try:
        with open(filename, 'r', encoding='utf-8') as csvfile:
            # Create CSV reader that returns dictionaries
            reader = csv.DictReader(csvfile)
            
            # Read each row
            for row_num, row in enumerate(reader, start=2):  # Start at 2 (after header)
                try:
                    # Validate and convert data types
                    book_data = {
                        'id': int(row['id']),
                        'title': row['title'].strip(),
                        'author': row['author'].strip(),
                        'year': int(row['year']),
                        'genre': row['genre'].strip(),
                        'available': row['available'].lower() == 'true'
                    }
                    
                    # Validate data
                    if not book_data['title']:
                        raise ValueError("Title cannot be empty")
                    
                    if book_data['year'] < 1000 or book_data['year'] > 2100:
                        raise ValueError(f"Invalid year: {book_data['year']}")
                    
                    books_data.append(book_data)
                
                except ValueError as e:
                    # Handle conversion errors for specific rows
                    print(f"✗ Error in row {row_num}: {e}")
                    continue  # Skip this row and continue with next
                
                except KeyError as e:
                    # Handle missing columns
                    print(f"✗ Missing column in row {row_num}: {e}")
                    continue
        
        print(f"✓ Loaded {len(books_data)} books from CSV: '{filename}'")
        return books_data
    
    except FileNotFoundError:
        print(f"✗ CSV file not found: '{filename}'")
        return []
    
    except Exception as e:
        print(f"✗ Error reading CSV: {e}")
        return []


# ============================================================================
# CONCEPT 20: FILE HANDLING - JSON Files
# ============================================================================

def save_books_to_json(books, filename):
    """
    Save books to a JSON (JavaScript Object Notation) file.
    
    JSON is a popular format for structured data.
    Demonstrates using the json module.
    """
    
    try:
        # Convert book objects to dictionaries
        books_list = []
        for book in books:
            book_dict = {
                'id': book.book_id,
                'title': book.title,
                'author': book.author,
                'year': book.year,
                'genre': book.get_genre(),
                'available': book.is_available()
            }
            books_list.append(book_dict)
        
        # Write to JSON file
        with open(filename, 'w', encoding='utf-8') as jsonfile:
            # indent=2 makes the JSON pretty-printed (readable)
            # ensure_ascii=False allows unicode characters
            json.dump(books_list, jsonfile, indent=2, ensure_ascii=False)
        
        print(f"✓ Saved {len(books)} books to JSON: '{filename}'")
        return True
    
    except TypeError as e:
        # JSON can't serialize certain Python objects
        print(f"✗ JSON serialization error: {e}")
        return False
    
    except IOError as e:
        print(f"✗ Error saving JSON: {e}")
        return False


def load_books_from_json(filename):
    """
    Load books from a JSON file.
    """
    
    try:
        with open(filename, 'r', encoding='utf-8') as jsonfile:
            # Load JSON data into Python objects (list of dicts)
            books_data = json.load(jsonfile)
        
        print(f"✓ Loaded {len(books_data)} books from JSON: '{filename}'")
        return books_data
    
    except FileNotFoundError:
        print(f"✗ JSON file not found: '{filename}'")
        return []
    
    except json.JSONDecodeError as e:
        # Raised when JSON is malformed
        print(f"✗ Invalid JSON format: {e}")
        return []
    
    except Exception as e:
        print(f"✗ Error reading JSON: {e}")
        return []


# ============================================================================
# CONCEPT 20: FILE OPERATIONS - Appending to Files
# ============================================================================

def log_transaction(transaction_type, details, logfile="library_log.txt"):
    """
    Append transaction logs to a file.
    
    Demonstrates:
    - Appending to files (mode 'a')
    - Logging system events
    """
    
    try:
        # 'a' mode opens file for appending (creates if doesn't exist)
        with open(logfile, 'a', encoding='utf-8') as file:
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            log_entry = f"[{timestamp}] {transaction_type}: {details}\n"
            file.write(log_entry)
        
        return True
    
    except IOError as e:
        print(f"✗ Error writing to log: {e}")
        return False


def read_log_file(logfile="library_log.txt", num_lines=10):
    """
    Read the last N lines from log file.
    
    Demonstrates reading files line by line.
    """
    
    try:
        with open(logfile, 'r', encoding='utf-8') as file:
            # Read all lines into a list
            lines = file.readlines()
            
            # Return last num_lines
            return lines[-num_lines:] if len(lines) > num_lines else lines
    
    except FileNotFoundError:
        print(f"✗ Log file not found: '{logfile}'")
        return []
    
    except Exception as e:
        print(f"✗ Error reading log: {e}")
        return []


# ============================================================================
# CONCEPT 20: Binary File Operations
# ============================================================================

def save_binary_data(data, filename):
    """
    Save data to a binary file.
    
    Demonstrates working with binary files (mode 'wb').
    Useful for images, executables, etc.
    """
    
    try:
        # 'wb' mode: write binary
        with open(filename, 'wb') as file:
            # Convert string to bytes
            if isinstance(data, str):
                data = data.encode('utf-8')
            file.write(data)
        
        print(f"✓ Saved binary data to '{filename}'")
        return True
    
    except Exception as e:
        print(f"✗ Error saving binary data: {e}")
        return False


def load_binary_data(filename):
    """
    Load data from a binary file.
    """
    
    try:
        # 'rb' mode: read binary
        with open(filename, 'rb') as file:
            data = file.read()
        
        print(f"✓ Loaded {len(data)} bytes from '{filename}'")
        return data
    
    except FileNotFoundError:
        print(f"✗ Binary file not found: '{filename}'")
        return None
    
    except Exception as e:
        print(f"✗ Error loading binary data: {e}")
        return None


# ============================================================================
# CONCEPT 20: Context Managers and File Safety
# ============================================================================

def safe_file_operation(filename, operation="read"):
    """
    Demonstrates comprehensive file safety with try-except-else-finally.
    """
    
    file_handle = None
    success = False
    
    try:
        print(f"Attempting to {operation} file: '{filename}'")
        
        if operation == "read":
            file_handle = open(filename, 'r', encoding='utf-8')
            content = file_handle.read()
            print(f"Read {len(content)} characters")
            success = True
            return content
        
        elif operation == "write":
            file_handle = open(filename, 'w', encoding='utf-8')
            file_handle.write("Test content\n")
            print("Write successful")
            success = True
            return True
    
    except FileNotFoundError:
        print(f"✗ FileNotFoundError: '{filename}' does not exist")
        raise LibraryFileError("File not found", filename)
    
    except PermissionError:
        print(f"✗ PermissionError: No permission to access '{filename}'")
        raise LibraryFileError("Permission denied", filename)
    
    except IOError as e:
        print(f"✗ IOError: {e}")
        raise LibraryFileError(f"IO operation failed: {e}", filename)
    
    else:
        # Executes only if no exception occurred
        print("✓ File operation completed successfully (else block)")
    
    finally:
        # Always executes - cleanup code
        if file_handle:
            if not file_handle.closed:
                file_handle.close()
                print("✓ File closed in finally block")
        
        if success:
            print("✓ Operation status: SUCCESS")
        else:
            print("✗ Operation status: FAILED")


# ============================================================================
# Advanced Exception Handling Examples
# ============================================================================

def validate_and_process_book_data(book_data):
    """
    Demonstrates raising exceptions and custom validation.
    """
    
    # Raising exceptions manually with 'raise' keyword
    if not isinstance(book_data, dict):
        raise TypeError("Book data must be a dictionary")
    
    if 'title' not in book_data:
        raise KeyError("Book data must contain 'title' field")
    
    if not book_data['title']:
        raise ValueError("Book title cannot be empty")
    
    # Additional validations
    if 'year' in book_data:
        year = book_data['year']
        if not isinstance(year, int):
            raise TypeError(f"Year must be an integer, got {type(year).__name__}")
        
        if year < 1000 or year > 2100:
            raise ValueError(f"Year {year} is out of valid range (1000-2100)")
    
    # If all validations pass
    print("✓ Book data is valid")
    return True


def robust_file_backup(source_file, backup_file):
    """
    Create a backup of a file with comprehensive error handling.
    """
    
    try:
        # Try to read source file
        try:
            with open(source_file, 'r', encoding='utf-8') as source:
                content = source.read()
        except FileNotFoundError:
            raise LibraryFileError(f"Source file '{source_file}' not found")
        
        # Try to write backup file
        try:
            with open(backup_file, 'w', encoding='utf-8') as backup:
                backup.write(content)
        except PermissionError:
            raise LibraryFileError(f"Cannot write to '{backup_file}'")
        
        print(f"✓ Successfully backed up '{source_file}' to '{backup_file}'")
        return True
    
    except LibraryFileError as e:
        print(f"✗ Backup failed: {e}")
        return False
    
    except Exception as e:
        print(f"✗ Unexpected error during backup: {e}")
        return False


# ============================================================================
# Exception Handling Best Practices Demonstration
# ============================================================================

def demonstrate_exception_handling():
    """
    Comprehensive demonstration of exception handling concepts.
    """
    
    print("\n" + "="*60)
    print("DEMONSTRATING EXCEPTION HANDLING")
    print("="*60)
    
    # Example 1: Basic try-except
    print("\n1. Basic try-except:")
    try:
        result = 10 / 0  # This will raise ZeroDivisionError
    except ZeroDivisionError:
        print("  ✗ Cannot divide by zero!")
    
    # Example 2: Multiple except blocks
    print("\n2. Multiple except blocks:")
    try:
        number = int("not_a_number")  # ValueError
    except ValueError:
        print("  ✗ ValueError: Invalid number format")
    except TypeError:
        print("  ✗ TypeError: Wrong type")
    
    # Example 3: Catching exception object
    print("\n3. Catching exception details:")
    try:
        numbers = [1, 2, 3]
        print(numbers[10])  # IndexError
    except IndexError as e:
        print(f"  ✗ IndexError: {e}")
    
    # Example 4: try-except-else
    print("\n4. try-except-else:")
    try:
        result = 10 / 2
    except ZeroDivisionError:
        print("  ✗ Division error")
    else:
        print(f"  ✓ Division successful: {result}")
    
    # Example 5: try-except-finally
    print("\n5. try-except-finally:")
    try:
        file = open("test.txt", "r")
    except FileNotFoundError:
        print("  ✗ File not found")
    finally:
        print("  ✓ Cleanup code executed (finally block)")
    
    # Example 6: Raising exceptions
    print("\n6. Raising exceptions:")
    try:
        age = -5
        if age < 0:
            raise ValueError("Age cannot be negative")
    except ValueError as e:
        print(f"  ✗ {e}")
    
    # Example 7: Custom exceptions
    print("\n7. Custom exceptions:")
    try:
        raise LibraryFileError("Custom error occurred", "test.txt")
    except LibraryFileError as e:
        print(f"  ✗ {e}")