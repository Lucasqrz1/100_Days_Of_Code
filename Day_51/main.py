# import modules
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import os
from dotenv import load_dotenv

# init environment variables
load_dotenv()

# constant variables
PROMISE_DOWN = 120
PROMISE_UP = 10
TWITTER_EMAIL = os.getenv("TWITTER_EMAIL")
TWITTER_PASSWORD = os.getenv("TWITTER_PASSWORD")

# this class defines how the bot will work and interact with the website and twitter(x).
class InternetSpeedTwitterBot:
    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=chrome_options)
        self.down = 0
        self.up = 0

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")

        time.sleep(3)

        go_button = self.driver.find_element(By.CSS_SELECTOR, value=".start-text")
        go_button.click()

        time.sleep(100)

        self.up = self.driver.find_element(By.XPATH,
                                           value='//*[@id="container"]/div[1]/div[3]/div/div/div/div[2]/div[2]/div/div[4]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span').text
        self.down = self.driver.find_element(By.XPATH,
                                             value='//*[@id="container"]/div[1]/div[3]/div/div/div/div[2]/div[2]/div/div[4]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text

    def tweet_at_provider(self):
        self.driver.get("https://x.com/login")
        time.sleep(5)

        # Fill email
        email = self.driver.find_element(By.XPATH, '//input[@autocomplete="username"]')
        email.send_keys(os.getenv("TWITTER_EMAIL"))
        email.send_keys(Keys.ENTER)
        time.sleep(2)

        # Fill password
        password = self.driver.find_element(By.XPATH, '//input[@autocomplete="current-password"]')
        password.send_keys(os.getenv("TWITTER_PASSWORD"))
        password.send_keys(Keys.ENTER)
        time.sleep(2)

        tweet_text = self.driver.find_element(By.CSS_SELECTOR, '[data-text="true"]')
        tweet = f"Hey Internet Provider, why is my internet speed {self.down}down/{self.up}up when I pay for {PROMISE_DOWN}down/{PROMISE_UP}up?"
        tweet_text.send_keys(tweet)
        time.sleep(1)

        tweet_button = self.driver.find_element(By.XPATH, '//div[@data-testid="tweetButtonInline"]')
        tweet_button.click()


bot = InternetSpeedTwitterBot()
bot.get_internet_speed()
bot.tweet_at_provider()