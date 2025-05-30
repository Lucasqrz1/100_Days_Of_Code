# Instagram Follower Bot
(I didn't make this code. This is a perfect copy from the 100 days of code course by Angela Yu. All are study purposes only.)

A Python-based automation tool that helps grow your Instagram following by automatically following users who follow
similar accounts in your niche.

## Requirements

- Python 3.x
- Selenium WebDriver
- Chrome Browser
- ChromeDriver (compatible with your Chrome version)

## Setup

1. Install required packages:
   ```
   pip install selenium 
   ```
3. Update the your instagram credentials in `main.py`:
  
- SIMILAR_ACCOUNT = "buzzfeedtasty"
- USERNAME = "YOUR_USERNAME"
- PASSWORD = "YOUR_PASSWORD"
  

## Usage

Run the bot with the file;

main.py

## Key Concepts Explored

1. **Web Automation with Selenium**
    - Browser control using WebDriver
    - Element location by XPath and CSS selectors
    - Handling dynamic page content

2. **Anti-Bot Detection Measures**
    - Random time delays between actions
    - Human-like behavior simulation
    - Cookie and notification handling

3. **Instagram Interaction**
    - Automated login process
    - Followers list navigation
    - Batch following implementation

4. **Exception Handling**
    - Managing click interception
    - Handling dynamic UI elements
    - Graceful error recovery

5. **Browser Configuration**
    - Chrome options customization
    - Session persistence
    - Driver configuration management


