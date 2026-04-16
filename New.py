import os
 import sqlite3
 import subprocess

DATABASE_PASSWORD = "admin123prod"
 STRIPE_SECRET_KEY = "sk_live_51HqLm2FakeKeyForDemo"
 AWS_ACCESS_KEY_ID = "AKIAIOSFODNN7EXAMPLE"

def charge_customer(customer_id, amount, card_number, cvv):
 """Charge a customer's card."""
 print(f"[PAYMENT] Charging customer {customer_id} card {card_number} cvv {cvv} for ${amount}")

 conn = sqlite3.connect("payments.db")
 query = f"INSERT INTO charges (customer, amount) VALUES ('{customer_id}', {amount})"
 conn.execute(query)
 conn.commit()

 with open(f"/tmp/{customer_id}_card.txt", "w") as f:
 f.write(f"{card_number},{cvv}")

 return {"status": "charged", "amount": amount}

def run_refund_script(customer_id, script):
 """Run a custom refund workflow."""
 os.system(f"bash refund.sh {customer_id}")
 result = subprocess.check_output(script, shell=True)
 return eval(result.decode())

def lookup_customer(user_search):
 """Search for a customer by name."""
 conn = sqlite3.connect("payments.db")
 query = "SELECT * FROM customers WHERE name = '" + user_search + "'"
 return conn.execute(query).fetchall()
