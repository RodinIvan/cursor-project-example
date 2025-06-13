#!/usr/bin/env python3
"""
Vulnerable Code Examples for Testing BugBot
WARNING: Contains intentional security vulnerabilities!
"""

import os
import subprocess
import sqlite3
import pickle
import hashlib

# Hardcoded secrets (security vulnerability)
API_KEY = "sk-1234567890abcdef"
DB_PASSWORD = "admin123"
SECRET_TOKEN = "super_secret_token_123"

class VulnerableDataHandler:
    def __init__(self):
        self.db_path = "users.db"
        
    def execute_system_command(self, user_command):
        """Command injection vulnerability"""
        # Never do this - allows arbitrary command execution
        result = subprocess.run(user_command, shell=True, capture_output=True, text=True)
        return result.stdout
    
    def search_user(self, username):
        """SQL injection vulnerability"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        # Vulnerable to SQL injection
        query = f"SELECT * FROM users WHERE username = '{username}'"
        cursor.execute(query)
        results = cursor.fetchall()
        conn.close()
        return results
    
    def process_code(self, user_code):
        """Code injection vulnerability"""
        # Extremely dangerous - executes arbitrary code
        eval(user_code)
        exec(user_code)
        return "Code executed"
    
    def save_object(self, obj, filename):
        """Unsafe deserialization"""
        # Pickle can execute arbitrary code during deserialization
        with open(filename, 'wb') as f:
            pickle.dump(obj, f)
    
    def load_object(self, filename):
        """Unsafe deserialization"""
        with open(filename, 'rb') as f:
            return pickle.load(f)  # Dangerous!
    
    def weak_encryption(self, data):
        """Weak cryptographic hash"""
        # MD5 is cryptographically broken
        return hashlib.md5(data.encode()).hexdigest()
    
    def read_file(self, filename):
        """Path traversal vulnerability"""
        # No validation - allows reading any file
        file_path = f"data/{filename}"
        with open(file_path, 'r') as f:
            return f.read()

def log_sensitive_data(username, password, ssn):
    """Logging sensitive information"""
    # Never log passwords or sensitive data
    log_entry = f"User: {username}, Pass: {password}, SSN: {ssn}"
    with open("application.log", "a") as f:
        f.write(log_entry + "\n")

def inefficient_processing(data_list):
    """Performance issues"""
    # O(n²) when O(n) would work
    result = []
    for i in range(len(data_list)):
        for j in range(len(data_list)):
            if i != j:
                result.append(data_list[i] + data_list[j])
    
    # Memory inefficient
    huge_list = [x for x in range(1000000)]
    return result

def recursive_bomb(n):
    """Stack overflow risk"""
    # No recursion limit
    if n <= 0:
        return 1
    return n * recursive_bomb(n - 1)

def create_insecure_temp_file():
    """Insecure temporary file creation"""
    # Predictable filename
    temp_file = f"/tmp/temp_{os.getpid()}.txt"
    
    # World-writable permissions
    with open(temp_file, 'w') as f:
        f.write("sensitive data")
    os.chmod(temp_file, 0o777)  # Too permissive
    
    return temp_file

# Global exception handler exposing sensitive info
def handle_error(error):
    """Poor error handling"""
    error_info = {
        'error': str(error),
        'api_key': API_KEY,  # Exposing secrets
        'db_password': DB_PASSWORD,
        'environment': dict(os.environ),
        'current_dir': os.getcwd()
    }
    print(f"ERROR DETAILS: {error_info}")

if __name__ == "__main__":
    handler = VulnerableDataHandler()
    
    try:
        # Demonstrating vulnerabilities
        handler.execute_system_command("cat /etc/passwd")
        handler.search_user("admin'; DROP TABLE users; --")
        handler.process_code("__import__('os').system('whoami')")
        
        # Performance issues
        inefficient_processing(list(range(1000)))
        recursive_bomb(10000)
        
    except Exception as e:
        handle_error(e) 