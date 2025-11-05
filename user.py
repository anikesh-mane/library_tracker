from datetime import datetime


# ============================================================================
# CONCEPT 16 & 17: User Class with Encapsulation
# ============================================================================

class User:
    """
    Represents a library user with encapsulated data and behavior.
    """
    
    # Class variable
    total_users = 0
    
    def __init__(self, name, email, user_id):
        """Constructor for User"""
        # Private attributes (name mangling)
        self.__name = name
        self.__email = email
        self.__user_id = user_id
        
        # Protected attributes
        self._borrowed_books = []  # List of book IDs
        self._registration_date = datetime.now()
        self._fine_amount = 0.0
        
        User.total_users += 1
    
    # Getters
    @property
    def name(self):
        return self.__name
    
    @property
    def email(self):
        return self.__email
    
    @property
    def user_id(self):
        return self.__user_id
    
    def get_borrowed_books(self):
        """Returns copy of borrowed books list (maintaining encapsulation)"""
        return self._borrowed_books.copy()
    
    def get_fine_amount(self):
        """Getter for fine amount"""
        return self._fine_amount
    
    # Setters with validation
    def update_email(self, new_email):
        """Update email with validation"""
        if '@' in new_email and '.' in new_email:
            self.__email = new_email
            return True
        return False
    
    def add_fine(self, amount):
        """Add to fine amount"""
        if amount > 0:
            self._fine_amount += amount
    
    def pay_fine(self, amount):
        """Reduce fine amount when payment is made"""
        if amount > 0 and amount <= self._fine_amount:
            self._fine_amount -= amount
            return True
        return False
    
    # Instance methods
    def borrow_book(self, book_id):
        """Add book to borrowed list"""
        if book_id not in self._borrowed_books:
            self._borrowed_books.append(book_id)
            return True
        return False
    
    def return_book(self, book_id):
        """Remove book from borrowed list"""
        if book_id in self._borrowed_books:
            self._borrowed_books.remove(book_id)
            return True
        return False
    
    def can_borrow(self, max_books=3):
        """Check if user can borrow more books"""
        return len(self._borrowed_books) < max_books and self._fine_amount == 0
    
    def get_user_info(self):
        """Get formatted user information"""
        return f"User #{self.__user_id}: {self.__name} ({self.__email}) - Books: {len(self._borrowed_books)}, Fine: ${self._fine_amount:.2f}"
    
    def __str__(self):
        return f"{self.__name} (ID: {self.__user_id})"


# ============================================================================
# CONCEPT 18: INHERITANCE - PremiumUser subclass
# ============================================================================

class PremiumUser(User):
    """
    Premium user with additional privileges.
    Demonstrates inheritance and extending parent functionality.
    """
    
    def __init__(self, name, email, user_id, premium_level="Silver"):
        """Constructor that extends User constructor"""
        super().__init__(name, email, user_id)
        
        # Premium-specific attributes
        self.premium_level = premium_level  # Silver, Gold, Platinum
        self.priority_reservations = []
        self.bonus_borrow_days = self._calculate_bonus_days()
    
    def _calculate_bonus_days(self):
        """Private helper method to calculate bonus days based on level"""
        bonus_days = {
            "Silver": 7,
            "Gold": 14,
            "Platinum": 21
        }
        return bonus_days.get(self.premium_level, 0)
    
    # ========================================================================
    # CONCEPT 19: POLYMORPHISM - Overriding parent methods
    # ========================================================================
    
    def can_borrow(self, max_books=3):
        """
        Override parent method - premium users can borrow more books
        and can borrow even with small fines.
        """
        premium_max_books = {
            "Silver": 5,
            "Gold": 7,
            "Platinum": 10
        }
        max_allowed = premium_max_books.get(self.premium_level, max_books)
        
        # Premium users can borrow with fines up to $5
        fine_threshold = 5.0
        return len(self._borrowed_books) < max_allowed and self._fine_amount < fine_threshold
    
    def get_user_info(self):
        """Extend parent method with premium information"""
        basic_info = super().get_user_info()
        return f"{basic_info} | Premium: {self.premium_level} (+{self.bonus_borrow_days} days)"
    
    # Premium-specific methods
    def reserve_book(self, book_id):
        """Premium users can reserve books"""
        if book_id not in self.priority_reservations:
            self.priority_reservations.append(book_id)
            return True
        return False
    
    def upgrade_level(self):
        """Upgrade premium level"""
        upgrades = {"Silver": "Gold", "Gold": "Platinum", "Platinum": "Platinum"}
        old_level = self.premium_level
        self.premium_level = upgrades.get(old_level, old_level)
        self.bonus_borrow_days = self._calculate_bonus_days()
        return self.premium_level != old_level