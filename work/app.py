import subprocess
import hashlib

# Week 3: Information Security Fundamentals
# Hardcoded credentials violate basic security principles (confidentiality, authentication)
username = "admin"
password = "admin123"

# Week 8: Security Design and Development (CWE Top 25)
# Weak hashing algorithm (MD5) is insecure and vulnerable to attacks
def hash_password(pwd):
    return hashlib.md5(pwd.encode()).hexdigest()

# Week 8: Security Design and Development (CWE Top 25)
# Weak hashing algorithm (MD5) is insecure and vulnerable to attacks
def login():
    user = input("Username: ")
    pwd = input("Password: ")
    
    if user == username and pwd == password:
        print("Login successful")
    else:
        print("Login failed")

# Mock database: in-memory list of users
mock_users = [
    ("1", "admin"),
    ("2", "user1"),
    ("3", "user2")
]

# Week 8: Security Design and Development (CWE Top 25)
# Weak hashing algorithm (MD5) is insecure and vulnerable to attacks
def get_user_data(user_id):
    # Simulate injectionwith mock data
    if "OR" in user_id.upper() or "1=1" in user_id:
        return mock_users
    else:
        # Return matching user
        return [user for user in mock_users if user[0] == user_id]

# Week 4: Top Web Application Attacks (OWASP Top 10 - Command Injection)
# Command injection via direct OS command execution

def run_command():
    user_input = input("Enter system command: ")
    subprocess.run(user_input, shell=True)

# Week 4: Top Web Application Attacks (OWASP Top 10 - Code Injection)
# Dangerous use of eval() allowing arbitrary code execution
def execute_code():
    code = input("Enter Python code: ")
    eval(code)

# Week 10: Security Monitoring
# No logging or monitoring implemented (violates SSDF monitoring practices)
def process_payment(amount):
    print(f"Processing payment of ${amount}")
    # No validation nor logging

# Week 9: Security Testing
# This entire script is designed to be scanned by  SAST tools (Bandit)
# to automatically detect vulnerabilities in CI pipeline

def main():
    login()
    run_command()
    execute_code()
    result = get_user_data("1 OR 1=1")
    print(f"User data: {result}")
    process_payment(100)

main()