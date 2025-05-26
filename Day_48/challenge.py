#TODO input basic data for sign up to a website automatically through this code

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Keep Chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# Create and configure the Chrome webdriver
driver = webdriver.Chrome(options=chrome_options)

# Navigate to Website
driver.get("https://secure-retreat-92358.herokuapp.com/")

# Hone in on absolute path using XPATH
first_name = driver.find_element(By.XPATH, value="/html/body/form/input[1]")
last_name = driver.find_element(By.XPATH, value="/html/body/form/input[2]")
email = driver.find_element(By.XPATH, value="/html/body/form/input[3]")

# Fill the form
first_name.send_keys("Gary")
last_name.send_keys("Holt")
email.send_keys("example@email.com")

# Sign up
sign_up_button = driver.find_element(By.XPATH, value="/html/body/form/button")
sign_up_button.click()