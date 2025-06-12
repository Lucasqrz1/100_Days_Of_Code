# Flask Blog Application

A dynamic blog application built with Flask framework that allows users to create, read, update, and delete blog posts.

## Installation

1. Clone this repository
2. Create a virtual environment:
   ```
   python -m venv .venv
   ```
3. Activate the virtual environment:
    - Windows: `.venv\Scripts\activate`
    - MacOS/Linux: `source .venv/bin/activate`
4. Install required packages:
   ```
   pip install -r requirements.txt
   ```

## Features

- Create new blog posts with rich text editor (CKEditor)
- Edit existing posts
- Delete posts
- Responsive design using Bootstrap 5
- SQLite database for data persistence
- Form validation
- Clean and modern UI

## Usage

1. Run the application:
   ```
   python main.py
   ```
2. Open your browser and navigate to `http://localhost:5003`
3. Use the navigation menu to:
    - View all posts
    - Create new posts
    - Edit existing posts
    - Delete posts

## Dependencies

- Flask
- Flask-Bootstrap5
- Flask-SQLAlchemy
- Flask-WTF
- Flask-CKEditor
- SQLAlchemy
- WTForms
