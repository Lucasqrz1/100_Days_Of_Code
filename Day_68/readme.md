# Flask Authentication System

A secure web application built with Flask that implements user authentication with email and password, featuring
registration, login, and protected content access.

## Technology Stack

- Python 3.12.10
- Flask
- SQLAlchemy
- Flask-Login
- SQLite Database
- Jinja2 Templates
- Werkzeug Security

## Installation

1. Clone the repository
2. Create a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```
   pip install flask flask-sqlalchemy flask-login werkzeug
   ```
4. Run the application:
   ```
   python main.py
   ```

## Features

- User registration with email and password
- Secure password hashing
- User login/logout functionality
- Protected routes requiring authentication
- File download capability for authenticated users
- Flash messages for user feedback
- SQLite database for user data storage

## Usage

1. Visit the home page and choose to Register or Login
2. For new users:
    - Click Register
    - Enter your name, email, and password
    - You'll be automatically logged in
3. For existing users:
    - Click Login
    - Enter your email and password
4. Once logged in:
    - Access the secrets page
    - Download protected files
    - Logout when finished
