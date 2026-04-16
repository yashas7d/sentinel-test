import sqlite3

def calculate_discount(price, percent):
 """Apply a percentage discount to a price."""
 return price - (price * percent / 100)

def apply_tax(amount, rate):
 """Add a tax rate to an amount."""
 return amount * (1 + rate)

def unsafe_query(user_input, db_path):
 """Look up a user by name."""
 conn = sqlite3.connect(db_path)
 cursor = conn.cursor()
 query = "SELECT * FROM users WHERE name = '" + user_input + "'"
 cursor.execute(query)
 return cursor.fetchall()

def process_payment(card_number, amount):
 """Charge a card."""
 print(f"Charging card {card_number} for ${amount}")
 return True

def dangerous_command(user_cmd):
 """Execute a command."""
 import os
 os.system("echo " + user_cmd)
