#!/usr/bin/env python3
"""
Data Processing Module with Security and Performance Issues
WARNING: This code contains intentional vulnerabilities for testing purposes!
"""

import os
import sys
import pickle
import subprocess
import sqlite3
import hashlib
import random
import time
from urllib.request import urlopen
import json

# Global variables (bad practice)
DATABASE_PATH = "iris_data.db"
DATABASE_PASSWORD = "admin123"
DEBUG_MODE = True

class DataProcessor:
    def __init__(self, data_source):
        self.data_source = data_source
        self.processed_data = []
        self.cache = {}
        
    def load_data_from_url(self, url):
        """Load data from URL without validation (security issue)"""
        try:
            # No URL validation - security vulnerability
            response = urlopen(url)
            data = response.read()
            return data
        except Exception as e:
            if DEBUG_MODE:
                print(f"Error details: {e}")  # Information disclosure
            return None
    
    def execute_system_command(self, command):
        """Execute system command without sanitization (major security issue)"""
        # Command injection vulnerability
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        return result.stdout
    
    def save_data_with_pickle(self, data, filename):
        """Save data using pickle (security issue)"""
        # Pickle deserialization can be dangerous
        with open(filename, 'wb') as f:
            pickle.dump(data, f)
    
    def load_data_with_pickle(self, filename):
        """Load data using pickle (security issue)"""
        # Unsafe deserialization
        with open(filename, 'rb') as f:
            return pickle.load(f)
    
    def create_database_connection(self):
        """Create database connection with SQL injection vulnerability"""
        conn = sqlite3.connect(DATABASE_PATH)
        return conn
    
    def search_data(self, search_term):
        """Search data with SQL injection vulnerability"""
        conn = self.create_database_connection()
        cursor = conn.cursor()
        
        # SQL injection vulnerability - no parameterized queries
        query = f"SELECT * FROM iris_data WHERE species = '{search_term}'"
        cursor.execute(query)
        results = cursor.fetchall()
        
        conn.close()
        return results
    
    def generate_weak_hash(self, data):
        """Generate hash using weak algorithm"""
        # MD5 is cryptographically broken
        return hashlib.md5(data.encode()).hexdigest()
    
    def inefficient_data_processing(self, large_dataset):
        """Inefficient data processing with performance issues"""
        processed = []
        
        # O(n²) complexity when O(n) would suffice
        for i in range(len(large_dataset)):
            for j in range(len(large_dataset)):
                if i != j:
                    # Unnecessary computation
                    result = large_dataset[i] * large_dataset[j]
                    processed.append(result)
        
        # Memory inefficient - creating large lists
        huge_list = []
        for i in range(1000000):
            huge_list.append(random.random())
        
        return processed
    
    def recursive_function_without_limit(self, n):
        """Recursive function that can cause stack overflow"""
        if n <= 0:
            return 1
        # No recursion limit check
        return n * self.recursive_function_without_limit(n - 1)
    
    def file_operations_without_context_manager(self, filename):
        """File operations without proper resource management"""
        # Not using context manager - resource leak
        file = open(filename, 'r')
        content = file.read()
        # File not properly closed in case of exception
        file.close()
        return content
    
    def process_user_input(self, user_input):
        """Process user input without validation"""
        # No input validation or sanitization
        eval(user_input)  # Extremely dangerous - code injection
        exec(user_input)  # Another code injection vulnerability
        
        # Path traversal vulnerability
        file_path = f"data/{user_input}.txt"
        with open(file_path, 'r') as f:
            return f.read()

def create_temporary_file_insecurely():
    """Create temporary file with security issues"""
    # Predictable temporary file name
    temp_filename = f"/tmp/temp_{random.randint(1, 1000)}.txt"
    
    # Insecure file permissions
    with open(temp_filename, 'w') as f:
        f.write("sensitive data")
    
    # Set world-readable permissions (security issue)
    os.chmod(temp_filename, 0o777)
    
    return temp_filename

def log_sensitive_information(username, password, credit_card):
    """Log sensitive information (privacy/security issue)"""
    log_message = f"User: {username}, Password: {password}, CC: {credit_card}"
    
    # Logging sensitive data in plain text
    with open("application.log", "a") as log_file:
        log_file.write(f"{time.ctime()}: {log_message}\n")

def inefficient_string_concatenation(items):
    """Inefficient string operations"""
    result = ""
    
    # Inefficient string concatenation in loop
    for item in items:
        result += str(item) + ", "
    
    return result

def memory_leak_simulation():
    """Function that can cause memory issues"""
    # Creating large objects without cleanup
    large_data = []
    
    while True:
        # Infinite loop that consumes memory
        large_data.append([random.random() for _ in range(10000)])
        
        # No break condition - will run forever
        if len(large_data) > 1000000:  # This will never be reached
            break
    
    return large_data

# Global exception handler that exposes sensitive information
def handle_exception(e):
    """Poor exception handling that exposes sensitive information"""
    error_details = {
        'error_type': type(e).__name__,
        'error_message': str(e),
        'system_info': {
            'python_version': sys.version,
            'platform': sys.platform,
            'environment_variables': dict(os.environ),  # Exposing env vars
            'current_directory': os.getcwd(),
            'api_key': DATABASE_PASSWORD  # Exposing database password in error
        }
    }
    
    # Printing sensitive information to console
    print(json.dumps(error_details, indent=2))

if __name__ == "__main__":
    # Unsafe main execution
    processor = DataProcessor("iris_dataset.csv")
    
    try:
        # Demonstrating various security issues
        processor.execute_system_command("ls -la")  # Command injection risk
        processor.search_data("'; DROP TABLE iris_data; --")  # SQL injection
        processor.process_user_input("__import__('os').system('rm -rf /')")  # Code injection
        
    except Exception as e:
        handle_exception(e)  # Exposing sensitive information 