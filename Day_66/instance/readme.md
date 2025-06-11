# Flask Cafe API

A RESTful API built with Flask for managing cafe information. This API allows users to search, add, update, and delete
cafe records in a database.

## Installation

1. Clone the repository
2. Create a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install required packages:
   ```
   pip install flask flask-sqlalchemy
   ```

## API Endpoints

### GET Endpoints

- `/` - Home page
- `/random` - Get a random cafe
- `/all` - Get all cafes
- `/search?loc=<location>` - Search cafes by location

### POST Endpoints

- `/add` - Add a new cafe (requires form data)

### PATCH Endpoints

- `/patch_new_price/<cafe_id>?new_price=<price>` - Update cafe price

### DELETE Endpoints

- `/report-closed/<cafe_id>?api-key=<key>` - Delete a cafe (requires API key)

## Usage Examples

### Get Random Cafe
