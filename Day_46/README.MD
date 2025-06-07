# Billboard Hot 100 Time Machine

This Python script allows you to travel back in time and get the Billboard Hot 100 songs for any specific date. The script scrapes the Billboard website and can be integrated with Spotify for playlist creation.

## Prerequisites

- Python 3.x
- A Spotify Developer Account

## Installation

1. Clone this repository or download the script
2. Install required dependencies:
```bash
pip install requests python-dotenv beautifulsoup4
```
## Setup
1. Create a Spotify Developer account at [Spotify Developer Dashboard](https://developer.spotify.com/dashboard)
2. Create a new application in the dashboard
3. Get your `Client ID` and `Client Secret`
4. Add a redirect URI in your app settings (e.g., `http://localhost:8888/callback`)
5. Create a `.env` file in the project root with your credentials:

SPOTIFY_CLIENT_ID=your_client_id_here
SPOTIFY_CLIENT_SECRET=your_client_secret_here

## Usage
1. Run the script:
python main.py 
2. Enter a date in YYYY-MM-DD format when prompted 
3. The script will:
    - Scrape the Billboard Hot 100 songs for that date
    - Save the songs to a `travel_date.txt` file
## Features
- Web scraping of Billboard Hot 100 charts
- Date-specific song retrieval
- Local file storage of results
- User input validation
- Environment variable configuration

## Error Handling
The script includes error handling for:
- Missing environment variables
- Web request failures
- Invalid date formats

## Contributing
Feel free to fork this repository and submit pull requests for any improvements.

