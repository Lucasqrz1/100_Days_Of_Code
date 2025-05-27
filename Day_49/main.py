from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException, ElementClickInterceptedException
from dotenv import load_dotenv
import os

class LinkedInBot:
    def __init__(self):
        load_dotenv()
        self.config = {
            'LOGIN_URL': "https://www.linkedin.com/login",
            'JOB_SEARCH_URL': "https://www.linkedin.com/jobs/search/?f_AL=true",
            'EMAIL': os.getenv('LINKEDIN_EMAIL'),
            'PASSWORD': os.getenv('LINKEDIN_PASSWORD'),
            'PHONE': os.getenv('LINKEDIN_PHONE'),
            'TIMEOUT': 10
        }
        self.driver = None
        self.wait = None
        
    def setup_driver(self):
        """Initialize the Chrome WebDriver"""
        self.driver = webdriver.Chrome()
        self.wait = WebDriverWait(self.driver, self.config['TIMEOUT'])
        
    def login(self):
        """Handle LinkedIn login process"""
        try:
            self.driver.get(self.config['LOGIN_URL'])
            
            # Fill email
            email_field = self.wait.until(
                EC.presence_of_element_located((By.ID, "username"))
            )
            email_field.send_keys(self.config['EMAIL'])
            
            # Fill password
            password_field = self.driver.find_element(By.ID, "password")
            password_field.send_keys(self.config['PASSWORD'])
            
            # Click sign in
            sign_in_button = self.driver.find_element(By.CSS_SELECTOR, "[type='submit']")
            sign_in_button.click()
            
            return True
        except Exception as e:
            print(f"Login failed: {str(e)}")
            return False

    def navigate_to_jobs(self):
        """Navigate to jobs search page"""
        try:
            self.driver.get(self.config['JOB_SEARCH_URL'])
            return True
        except Exception as e:
            print(f"Navigation failed: {str(e)}")
            return False

    def fill_phone_number(self):
        """Fill phone number if field exists and is empty"""
        try:
            phone_input = self.wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "input[type='tel']"))
            )
            if phone_input.get_attribute("value") == "":
                phone_input.send_keys(self.config['PHONE'])
            return True
        except TimeoutException:
            return False  # Phone field not found, which is okay

    def apply_to_job(self):
        """Handle the job application process"""
        try:
            # Click Easy Apply button
            easy_apply_button = self.wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, ".jobs-apply-button"))
            )
            easy_apply_button.click()
            
            # Fill phone number if needed
            self.fill_phone_number()
            
            # Submit application
            submit_button = self.wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))
            )
            submit_button.click()
            
            return True
        except Exception as e:
            print(f"Application failed: {str(e)}")
            return False

    def close(self):
        """Clean up resources"""
        if self.driver:
            self.driver.quit()

    def run(self):
        """Main execution method"""
        try:
            self.setup_driver()
            if not self.login():
                return False
            
            if not self.navigate_to_jobs():
                return False
            
            return self.apply_to_job()
            
        except Exception as e:
            print(f"An error occurred: {str(e)}")
            return False
        finally:
            self.close()


def main():
    bot = LinkedInBot()
    success = bot.run()
    print("Application successful!" if success else "Application failed!")

if __name__ == "__main__":
    main()