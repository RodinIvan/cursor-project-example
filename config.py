# Configuration file with security issues

# Hardcoded credentials (major security issue)
DATABASE_CONFIG = {
    'host': 'localhost',
    'port': 5432,
    'username': 'admin',
    'password': 'password123',  # Weak password
    'database': 'production_db'
}

# API keys in plain text
API_KEYS = {
    'openai': 'sk-1234567890abcdefghijklmnopqrstuvwxyz',
    'stripe': 'sk_live_1234567890abcdef',
    'aws_access_key': 'AKIAIOSFODNN7EXAMPLE',
    'aws_secret_key': 'wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY'
}

# JWT secret key
JWT_SECRET = "super_secret_key_123"

# Debug mode enabled in production
DEBUG = True
TESTING = True

# Insecure SSL settings
SSL_VERIFY = False
SSL_CERT_CHECK = False

# Default admin credentials
DEFAULT_ADMIN = {
    'username': 'admin',
    'password': 'admin',
    'email': 'admin@example.com'
}

# Logging configuration that logs sensitive data
LOGGING_CONFIG = {
    'level': 'DEBUG',
    'log_passwords': True,  # Bad practice
    'log_api_keys': True,   # Bad practice
    'log_file': '/var/log/app.log'
}

# Weak encryption settings
ENCRYPTION_CONFIG = {
    'algorithm': 'MD5',  # Weak algorithm
    'key_length': 8,     # Too short
    'salt': 'fixed_salt' # Fixed salt is bad
}

# File upload settings with security issues
UPLOAD_CONFIG = {
    'allowed_extensions': ['*'],  # Allows any file type
    'max_file_size': 999999999,   # No reasonable limit
    'upload_path': '/tmp/',       # Insecure location
    'execute_uploaded': True      # Extremely dangerous
}

# Database connection string with embedded credentials
DATABASE_URL = "postgresql://admin:password123@localhost:5432/production_db"

# CORS settings - too permissive
CORS_CONFIG = {
    'allow_origins': ['*'],
    'allow_methods': ['*'],
    'allow_headers': ['*'],
    'allow_credentials': True
}

# Session configuration
SESSION_CONFIG = {
    'secret_key': 'easy_to_guess',
    'secure': False,      # Not secure over HTTP
    'httponly': False,    # Accessible via JavaScript
    'samesite': 'None'    # No CSRF protection
}

# Email configuration with credentials
EMAIL_CONFIG = {
    'smtp_server': 'smtp.gmail.com',
    'smtp_port': 587,
    'username': 'myapp@gmail.com',
    'password': 'mypassword123',  # Hardcoded email password
    'use_tls': False              # Insecure connection
}

# Redis configuration
REDIS_CONFIG = {
    'host': 'localhost',
    'port': 6379,
    'password': None,     # No authentication
    'ssl': False          # Unencrypted connection
}

# Feature flags
FEATURES = {
    'enable_debug_endpoints': True,    # Debug endpoints in production
    'bypass_authentication': True,    # Authentication bypass
    'allow_sql_queries': True,        # Direct SQL execution
    'enable_file_browser': True       # File system access
} 