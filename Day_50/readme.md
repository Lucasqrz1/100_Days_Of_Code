# Tinder Auto Swiper Bot

A Python-based automated bot that interacts with Tinder web application using Selenium WebDriver. This bot automatically handles the login process through Facebook and performs right swipes (likes) on Tinder.

## Description

This bot automates the following actions on Tinder:
- Logs into Tinder using Facebook credentials
- Handles location and notification permissions
- Accepts cookies
- Automatically likes (right swipes) profiles
- Handles matching popups

## Requirements

- Python 3.x
- Selenium WebDriver
- Chrome Browser
- ChromeDriver (compatible with your Chrome browser version)

### Required Python Packages

- selenium
- time


## Setup

1. Install the required package:
   ```bash
   pip install selenium
   ```

2. Configure your credentials:
   - Replace `FB_EMAIL` with your Facebook email
   - Replace `FB_PASSWORD` with your Facebook password

## Usage

1. Make sure you have ChromeDriver installed and in your system PATH
2. Run the script:
   ```bash
   python main.py
   ```

## Features

- **Automated Login**: Handles Facebook authentication process
- **Permission Management**: Automatically accepts location access and notifications
- **Error Handling**: 
  - Manages "It's a Match!" popups
  - Handles loading delays
  - Deals with common exceptions
- **Rate Limiting**: Limited to 100 likes (free tier limit)
  - Can be modified for premium accounts by changing the loop condition

## Limitations

- Works with free tier Tinder (100 likes per day limit)
- Requires Facebook login credentials
- Depends on XPath and CSS selectors which may need updates if Tinder's website structure changes

## Safety Notes

- Keep your credentials secure
- Use at your own risk as automated actions might violate Tinder's terms of service
- Consider adding delays between actions to avoid being flagged as a bot

## Disclaimer

This bot is for educational purposes only. Using automated scripts might violate Tinder's terms of service. Use at your own risk.
I didn't make this code. It is a perfect copy from the 100 days of code course, only for code review.