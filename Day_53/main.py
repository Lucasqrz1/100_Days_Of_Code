from bs4 import BeautifulSoup
from selenium import webdriver
import requests
import time


URL = "https://appbrewery.github.io/Zillow-Clone/"

response = requests.get(URL)
website_html = response.text
soup = BeautifulSoup(website_html, "html.parser")

# Create a list of links for all the listings scraped
all_link_elements = soup.select(".StyledPropertyCardPhotoBody a")
all_links = [link.get('href') for link in all_link_elements]

# Save links to a file
with open("all_links.txt", mode="w", encoding="utf-8") as file:
    for link in all_links:
        file.write(f"{link}\n")

# Create a list of prices
all_price_elements = soup.select(".PropertyCardWrapper span[data-test='property-card-price']")

# Function to clean price strings
def clean_price(price_str):
    import re
    # Extract just the dollar amount
    # This will match the dollar sign and digits with commas
    match = re.search(r'\$([\d,]+)', price_str)
    if match:
        return f"${match.group(1)}"
    return price_str

all_prices = [clean_price(price.text.strip()) for price in all_price_elements]

# Save prices to a file
with open("all_prices.txt", mode="w", encoding="utf-8") as file:
    for price in all_prices:
        file.write(f"{price}\n")

# Create a list of addresses
all_address_elements = soup.select("address[data-test='property-card-addr']")

# Function to clean address strings
def clean_address(address_str):
    import re
    # Remove the pipe character and any leading/trailing whitespace
    address_str = re.sub(r'\s*\|\s*', '', address_str)
    # Replace multiple spaces with a single space
    address_str = re.sub(r'\s+', ' ', address_str)
    # Remove any other special characters if needed
    address_str = address_str.strip()
    return address_str

all_addresses = [clean_address(address.text.strip()) for address in all_address_elements]

# Save addresses to a file
with open("all_addresses.txt", mode="w", encoding="utf-8") as file:
    for address in all_addresses:
        file.write(f"{address}\n")


# form filling automation with selenium webdriver
class FormFillingBot:
    def __init__(self):
        # Keep browser open so you can manually log out
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=chrome_options)

    def fill(self):
        url = "https://docs.google.com/forms/d/e/1FAIpQLSeQa9n0Y44-thVvftyHmvkyeRN-ppu6DiD4UAmn1al-9kndjQ/viewform?usp=header"
        self.driver.get(url)
        time.sleep(2)
        property_price_box = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input'
        price_per_month_box = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input'
        link = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input'
        submit = '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span'




