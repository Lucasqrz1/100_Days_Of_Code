# LinkedIn Auto Apply Bot

A Python bot that automatically applies to LinkedIn "Easy Apply" jobs.

## Requirements
- Python 3.x
- Chrome browser
- `selenium` package

## Setup
1. Install requirements:
pip install selenium

2. Update config in script with your details:
CONFIG = {
    'EMAIL': "your_email@example.com", 
    'PASSWORD': "your_password",
    'PHONE': "your_phone_number"
}

3. Run the script:
python linkedin_auto_apply.py

## Features
- Automatic login
- Phone number auto-fill
- Handles multi-step applications
- Error handling and logging

## Disclaimer
For educational purposes only. Use at your own risk.

## License
MIT License