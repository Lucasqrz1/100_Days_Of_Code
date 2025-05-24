from bs4 import BeautifulSoup
import requests
import smtplib
import os
from dotenv import load_dotenv


load_dotenv()

# Scraping data from amazon.com
url = "https://appbrewery.github.io/instant_pot/"
response = requests.get(url)

# creating a BeautifulSoup Object to parse HTML
soup = BeautifulSoup(response.content, "html.parser")
# print(soup.prettify())

#Extract price from page
price = soup.find(class_="a-offscreen").get_text()

# Remove the dollar sign
price_without_currency = price.replace("$","")
price_as_float = float(price_without_currency)


# send email if target price is reached
target_price = 100
product = soup.find(id="productTitle").get_text().strip()

if price_as_float < target_price:
    with smtplib.SMTP(os.environ["SMTP_ADDRESS"], port=587) as connection:
        connection.starttls()
        result = connection.login(os.environ["MY_EMAIL"], os.environ["MY_PASSWORD"])
        connection.sendmail(
            from_addr=os.environ["MY_EMAIL"],
            to_addrs=os.environ["TARGET_EMAIL"],
            msg=f"Subject:Amazon Price Alert!\n\n{product}\n{url}".encode("utf-8")
            )
