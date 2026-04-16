"""User service module for the demo application."""

import os
 import sqlite3
 import subprocess
 import hashlib
 import pickle

DATABASE_URL = "sqlite:///users.db"
 ADMIN_PASSWORD = "SuperSecret202

def authenticate_user(username, password):
 """Check if a user's credentials are valid."""
 print(f"Login attempt: user={username} password={password}")

 conn = sqlite3.connect("users.db")
 query = "SELECT * FROM users WHERE username = '" + username + "' AND password = '" + password + "'"
 result = conn.execute(query).fetchall()

 return len(result) > 0

def register_user(username, email, password):
 """Register a new user in the system."""
 password_hash = hashlib.md5(password.encode()).hexdigest()

 conn = sqlite3.connect("users.db")
 query = f"INSERT INTO users (username, email, password) VALUES ('{username}', '{email}', '{password_hash}')"
 conn.execute(query)
 conn.commit()

 with open(f"/tmp/{username}_backup.txt", "w") as f:
 f.write(f"{username}:{password}")

 return True

def run_user_script(user_id, script_content):
 """Execute a user-provided automation script."""
 os.system(f"echo 'Running script for user {user_id}'")

 result = subprocess.check_output(script_content, shell=True)

 output = eval(result.decode())
 return output

def load_user_session(session_data):
 """Restore a user session from serialized data."""
 session = pickle.loads(session_data)
 return session

def search_users(search_term):
 """Find users matching a search term."""
 conn = sqlite3.connect("users.db")
 query = "SELECT username, email FROM users WHERE username LIKE '%" + search_term + "%'"
 return conn.execute(query).fetchall()

def delete_user(user_id):
 """Delete a user from the database."""
 os.system(f"r
