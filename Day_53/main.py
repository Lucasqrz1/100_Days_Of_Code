from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
import time

class FormFillingBot:
    def __init__(self):
        # Keep the browser open
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=chrome_options)

    def get_property_data(self):
        URL = "https://appbrewery.github.io/Zillow-Clone/"
        response = requests.get(URL)
        soup = BeautifulSoup(response.text, "html.parser")

        # Get links
        all_link_elements = soup.select(".StyledPropertyCardPhotoBody a")
        links = [link.get('href') for link in all_link_elements]

        # Get prices
        all_price_elements = soup.select(".PropertyCardWrapper span[data-test='property-card-price']")
        prices = [self.clean_price(price.text.strip()) for price in all_price_elements]

        # Get addresses
        all_address_elements = soup.select("address[data-test='property-card-addr']")
        addresses = [self.clean_address(address.text.strip()) for address in all_address_elements]

        return addresses, prices, links

    @staticmethod
    def clean_price(price_str):
        import re
        match = re.search(r'\$([\d,]+)', price_str)
        return f"${match.group(1)}" if match else price_str

    @staticmethod
    def clean_address(address_str):
        import re
        address_str = re.sub(r'\s*\|\s*', '', address_str)
        address_str = re.sub(r'\s+', ' ', address_str)
        return address_str.strip()

    def fill_form(self):
        addresses, prices, links = self.get_property_data()
        form_url = "https://docs.google.com/forms/d/e/1FAIpQLSeQa9n0Y44-thVvftyHmvkyeRN-ppu6DiD4UAmn1al-9kndjQ/viewform?usp=header"

        # XPath selectors
        address_xpath = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input'
        price_xpath = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input'
        link_xpath = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input'
        submit_xpath = '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span'

        for i in range(len(addresses)):
            if i >= len(prices) or i >= len(links):
                break

            self.driver.get(form_url)
            time.sleep(2)

            # Fill form fields
            self.driver.find_element(By.XPATH, address_xpath).send_keys(addresses[i])
            self.driver.find_element(By.XPATH, price_xpath).send_keys(prices[i])
            self.driver.find_element(By.XPATH, link_xpath).send_keys(links[i])

            # Submit
            self.driver.find_element(By.XPATH, submit_xpath).click()
            time.sleep(2)

if __name__ == "__main__":
    bot = FormFillingBot()
    bot.fill_form()