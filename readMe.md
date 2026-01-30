"""
Restaurant Order System Specification:

Core Features:
1. Menu Management
   - Add/remove dishes with name, price, category (appetizer, main, dessert)
   - Update dish prices

2. Order Management
   - Create new orders with table number
   - Add/remove dishes from order
   - Calculate order total (include 8% tax)
   - Apply discount codes: "STUDENT10" = 10% off, "VIP15" = 15% off

3. Table Management
   - Track table status (available, occupied, reserved)
   - Assign orders to tables
   - Calculate table bill

4. Reporting
   - List all orders for a specific table
   - Calculate total revenue for the day
   - Find most popular dish

Constraints:
- All data should be stored in memory (no database needed)
- Input validation for all user inputs
- Error handling for invalid operations
- Unit tests for each major function
"""

# Expected Interface:
"""
restaurant = RestaurantSystem()

# Menu operations
restaurant.add_dish("Pizza", 12.99, "main")
restaurant.add_dish("Salad", 8.99, "appetizer")

# Order operations
order_id = restaurant.create_order(table_number=5)
restaurant.add_to_order(order_id, "Pizza", 2)
restaurant.add_to_order(order_id, "Salad", 1)
restaurant.apply_discount(order_id, "STUDENT10")

# Table operations
restaurant.assign_table(order_id, 5)
bill = restaurant.get_table_bill(5)

# Reports
revenue = restaurant.get_daily_revenue()
popular = restaurant.get_most_popular_dish()
"""



#FILE SYSTEM
Practice Exercise 1: The "Cloud Store" (Data Management)
This is a very common theme. You are building a key-value store with extra features.

Level 1 (Basic CRUD): Implement a class CloudStore with SET(key, value) and GET(key).

Level 2 (Versioning): Modify SET to store versions. GET(key) should return the latest, but GET_AT(key, version) returns a specific one.

Level 3 (TTL/Expiration): Add SET_WITH_TTL(key, value, ttl). If a key is accessed after ttl seconds, it should return None and be deleted.

Level 4 (Filtering/Analysis): Implement GET_TOP_KEYS(n) which returns the n keys that have been accessed the most, sorted by frequency (descending) and then lexicographically (ascending).



Practice Exercise 2: The "Mini File System" (Nested Data)
This tests your ability to navigate nested dictionaries and handle string paths.

Level 1 (Navigation): Implement mkdir(path) and ls(path). Paths are strings like "/root/users/docs".

Level 2 (Files): Implement create_file(path, content) and read_file(path).

Level 3 (Search): Implement find(name) which returns all paths containing a file or directory with that name.

Level 4 (Permissions): Add a user system. grant(path, user_id, access_level). If a user calls read_file without the correct level, return an error.


Practice Exercise 3: "Transaction Processor" (Logic & State)
This mimics a banking or stock trading system.

Level 1 (Balances): Implement deposit(user, amount) and withdraw(user, amount). Ensure balance never goes below zero.

Level 2 (Transfers): Implement transfer(user_from, user_to, amount). This must be atomic (if one side fails, the whole thing fails).

Level 3 (Scheduled Tasks): Implement schedule_payment(user_from, user_to, amount, timestamp). The payment only executes when the system's "current time" reaches that timestamp.

Level 4 (Cashback/Rewards): Every 10th transaction for a user grants them a 2% cashback. Track transaction counts accurately across all types.