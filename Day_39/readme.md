# Flight Deal Finder

An automated flight search system that helps you find the best flight deals by tracking prices to your favorite destinations.

## Overview

This application:
- Tracks flight prices from a specified origin city
- Manages destination data through a spreadsheet
- Automatically finds and compares flight prices
- Searches for flights within a 6-month window
- Handles IATA airport codes lookup

## Features

- 🔄 Automated flight price checking
- 📊 Google Sheets integration for destination management
- ✈️ IATA code automatic lookup
- 💰 Cheapest flight finder
- 🕒 Rate limit handling for API requests

## Prerequisites

- Python 3.x
- Google Sheets API access
- Flight search API credentials (specific API details should be added here)

## Installation

1. Clone the repository:

bash git clone [repository-url] cd flight-deal-finder

2. Install required packages:
```bash
pip install -r requirements.txt
```
# Create a .env file with your credentials
SHEET_API_KEY=your_google_sheets_api_key
FLIGHT_SEARCH_API_KEY=your_flight_search_api_key
python main.py
flight-deal-finder/
│
├── main.py              # Main application script
├── data_manager.py      # Google Sheet data management
├── flight_search.py     # Flight search functionality
├── flight_data.py       # Flight data processing
├── .env                 # Environment variables (not in git)
└── requirements.txt     # Project dependencies