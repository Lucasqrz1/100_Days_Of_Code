import os
import requests
from dotenv import load_dotenv
from typing import Dict, List

# Load environment variables
load_dotenv()

def get_stock_data(stock_name: str) -> Dict:
    """Fetch stock data from Alpha Vantage API."""
    try:
        response = requests.get(
            "https://www.alphavantage.co/query",
            params={
                "function": "TIME_SERIES_DAILY",
                "symbol": stock_name,
                "apikey": os.getenv("STOCK_API_KEY")
            }
        )
        response.raise_for_status()
        return response.json()["Time Series (Daily)"]
    except requests.RequestException as e:
        print(f"Error fetching stock data: {e}")
        return None

def calculate_price_change(yesterday_price: float, day_before_price: float) -> tuple:
    """Calculate price change percentage and direction."""
    difference = float(yesterday_price) - float(day_before_price)
    percentage = round((abs(difference) / float(yesterday_price)) * 100)
    direction = "🔺" if difference > 0 else "🔻"
    return percentage, direction

def get_news(company_name: str) -> List[Dict]:
    """Fetch news articles from News API."""
    try:
        response = requests.get(
            "https://newsapi.org/v2/everything",
            params={
                "apiKey": os.getenv("NEWS_API_KEY"),
                "qInTitle": company_name,
            }
        )
        response.raise_for_status()
        return response.json()["articles"][:3]
    except requests.RequestException as e:
        print(f"Error fetching news: {e}")
        return []

def main():
    STOCK_NAME = "TSLA"
    COMPANY_NAME = "Tesla Inc"

    # Get stock data
    data = get_stock_data(STOCK_NAME)
    if not data:
        return

    # Process stock prices
    data_list = list(data.values())
    yesterday_close = float(data_list[0]["4. close"])
    day_before_close = float(data_list[1]["4. close"])
    
    # Calculate changes
    change_percent, direction = calculate_price_change(yesterday_close, day_before_close)
    
    # Get news if significant change
    if change_percent > 1:
        articles = get_news(COMPANY_NAME)
        for article in articles:
            message = (
                f"{STOCK_NAME}: {direction}{change_percent}%\n"
                f"Headline: {article['title']}\n"
                f"Brief: {article['description']}"
            )
            print(message)  # Replace with your notification logic

if __name__ == "__main__":
    main()