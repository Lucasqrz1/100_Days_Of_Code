# Library Management System

A simple web-based library management system built with Flask and SQLAlchemy that allows users to manage their book
collection.

## Features

- Add new books with title, author, and rating
- View all books in the library
- Edit book ratings
- Delete books from the library
- SQLite database for data persistence

## Prerequisites

- Python 3.12.10
- virtualenv

## Installation

1. Clone the repository
2. Create a virtual environment:
   ```bash
   virtualenv venv
   ```
3. Activate the virtual environment:
    - Windows:
      ```bash
      venv\Scripts\activate
      ```
    - Unix or MacOS:
      ```bash
      source venv/bin/activate
      ```
4. Install required packages:
   ```bash
   pip install -r requirements.txt
   ```

## Running the Application

1. Make sure your virtual environment is activated
2. Run the application:
   ```bash
   python main.py
   ```
3. Open your web browser and navigate to `http://127.0.0.1:5000`

## Project Structure

- `main.py` - Main application file containing Flask routes and SQLAlchemy models
- `templates/` - Directory containing HTML templates
    - `index.html` - Home page template showing the list of books
    - `add.html` - Template for adding new books
    - `edit_rating.html` - Template for editing book ratings
- `books.db` - SQLite database file (created automatically)
- `requirements.txt` - List of Python package dependencies
- `readme.md` - Project documentation


