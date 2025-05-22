# Hacker News Top Story Scraper

A Python web scraper that fetches and identifies the most upvoted story from Hacker News (news.ycombinator.com).

## Description

This script automatically scrapes the Hacker News homepage to find the story with the highest number of upvotes. It extracts:
- Article titles
- Article links
- Upvote counts

And then outputs the title and link of the most popular story.

## Prerequisites

The following Python packages are required:

python beautifulsoup4==4.12.2 requests==2.31.0


## Installation

1. Clone this repository
2. Install the required packages:
bash pip install beautifulsoup4 requests

## Usage

Run the script:
bash python main.py


The script will output:
- The title of the most upvoted story
- The corresponding link to that story

## How It Works

1. Fetches the HTML content from Hacker News homepage
2. Parses the HTML using BeautifulSoup
3. Extracts article information:
   - Finds all article titles using the 'titleline' class
   - Collects article links from the HTML elements
   - Extracts upvote counts using the 'score' class
4. Identifies the article with the highest upvote count
5. Outputs the most popular article's details

## Limitations

- The script depends on Hacker News' current HTML structure
- Rate limiting may apply when making frequent requests
- Some articles might not have upvote counts

## Contributing

Feel free to fork this repository and submit pull requests for any improvements.

## Acknowledgments

- [Hacker News](https://news.ycombinator.com) for providing the content
- BeautifulSoup4 documentation
- Requests library documentation