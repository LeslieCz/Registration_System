# Registration_System
Prototype for a CI pipeline with automated security testing, built using GitHub Actions and Bandit, demonstrating DevSecOps practices for secure software development.

## Running the Application

This application is a demonstration of common security vulnerabilities in Python code. It is intentionally insecure and should not be used in production.

### Prerequisites
- Python 3.x installed on your system.

### Steps to Run
1. Open a terminal in the project root directory (`Registration_System`).
2. Run the application:
   ```
   python work/app.py
   ```
3. Follow the prompts:
   - **Username:** Enter `admin`
   - **Password:** Enter `admin123`
   - **Enter system command:** Enter a valid system command, e.g., `dir` (on Windows) or `ls` (on Unix).
   - **Enter Python code:** Enter a Python expression, e.g., `print("hello")` or `1+1`.

The application will simulate login, execute the command, run the code, query mock user data, and process a payment.

### Notes
- The app uses a mock database (in-memory list) to avoid real database setup.
- It demonstrates vulnerabilities like hardcoded credentials, command injection, code injection, and SQL injection simulation.
- For security testing, the GitHub Actions workflow in `workflows/security.yml` runs Bandit to detect these issues.
