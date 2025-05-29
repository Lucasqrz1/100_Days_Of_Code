# Internet Speed Twitter Bot

A Python bot that tests your internet speed using Speedtest.net and automatically tweets at your internet service
provider if the speeds are below your promised rates.

## Description

This bot automates the process of:

1. Running a speed test on Speedtest.net
2. Comparing results against promised speeds
3. Tweeting at your internet provider if speeds are below promised rates

## Requirements

- Python 3.x
- Selenium WebDriver
- Chrome Browser
- Python packages:
    - selenium
    - python-dotenv
    - time
  
## Setup

1. Clone this repository
2. Install required packages:
   ```
   pip install selenium python-dotenv
   ```
3. Create a `.env` file with your Twitter credentials:
   ```
   TWITTER_EMAIL=your email here
   TWITTER_PASSWORD=your password here
   ```
4. Update the promised speeds in `main.py`:
   ```python
   PROMISE_DOWN = 120
   PROMISE_UP = 10
   ```

## Usage

Run the bot with the file;

main.py


