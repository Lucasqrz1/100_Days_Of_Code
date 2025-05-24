# Amazon Price Tracker

A Python application that tracks the price of a product on Amazon and sends an email notification when the price drops below a specified threshold.

## Features

- Scrapes product information from Amazon using BeautifulSoup
- Monitors product price automatically
- Sends email alerts when price drops below target price
- Configurable via environment variables
- Extracts product title and current price

## Requirements

- Python 3.6+
- Beautiful Soup 4
- Requests
- python-dotenv
- smtplib (part of Python standard library)

## Setup

1. Clone the repository:
   ```
   pip install beautifulsoup4 requests python-dotenv
   ```

2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
   
   Or install individual packages:
   ```
   pip install beautifulsoup4 requests python-dotenv
   ```

3. Create a `.env` file in the project root with the following variables:
   ```
   SMTP_ADDRESS="smtp.gmail.com"
   MY_EMAIL="your-email@gmail.com"
   MY_PASSWORD="your-app-password"
   TARGET_EMAIL="recipient-email@example.com"
   ```
   
   Note: For Gmail, you need to use an App Password:
   - Enable 2-Step Verification in your Google Account
   - Go to Security → App passwords
   - Generate a new app password for this application
   - This is not your regular Gmail password
   - App Passwords remain valid until you manually revoke them

4. Modify the `url` variable in `main.py` to point to your desired Amazon product.
5. Set your desired target price in the `target_price` variable in `main.py`.


