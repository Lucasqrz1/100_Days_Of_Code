from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException, ElementClickInterceptedException
from dotenv import load_dotenv
import os

#TODO: FIGURE OUT WHY PHONE FIELD IS NOT GOING THROUGH

# Load environment variables
load_dotenv()

# Configuration
CONFIG = {
    'LOGIN_URL': "https://www.linkedin.com/login",
    'JOB_SEARCH_URL': "https://www.linkedin.com/jobs/search/?currentJobId=4227541842&f_AL=true&keywords=data%20scientist&origin=JOB_SEARCH_PAGE_JOB_FILTER",
    'EMAIL': os.getenv('LINKEDIN_EMAIL'),
    'PASSWORD': os.getenv('LINKEDIN_PASSWORD'),
    'PHONE': os.getenv('LINKEDIN_PHONE'),
    'TIMEOUT': 10
}


def setup_driver():
    """Configure and return Chrome WebDriver instance."""
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("detach", True)
    return webdriver.Chrome(options=chrome_options)


def login(driver, wait):
    """Handle LinkedIn login process."""
    try:
        driver.get(CONFIG['LOGIN_URL'])

        email_field = driver.find_element(By.ID, "username")
        email_field.send_keys(CONFIG['EMAIL'])

        password_field = driver.find_element(By.ID, "password")
        password_field.send_keys(CONFIG['PASSWORD'])

        sign_in_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
        sign_in_button.click()

        # Wait for login to complete
        wait.until(EC.url_changes(CONFIG['LOGIN_URL']))
        return True
    except (TimeoutException, NoSuchElementException) as e:
        print(f"Login failed: {str(e)}")
        return False


def navigate_to_job_search(driver, wait):
    """Navigate to job search page and select first job."""
    try:
        driver.get(CONFIG['JOB_SEARCH_URL'])
        first_job = wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, ".job-card-container")))
        first_job.click()
        return True
    except TimeoutException as e:
        print(f"Failed to navigate to job search: {str(e)}")
        return False


def apply_to_job(driver, wait):
    """Handle the job application process."""
    try:
        # Click Easy Apply button
        easy_apply_button = wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, ".jobs-apply-button")))
        easy_apply_button.click()

        # Handle phone number input if present
        try:
            phone_input = wait.until(EC.presence_of_element_located(
                (By.CSS_SELECTOR, "input[type='tel']")))
            if not phone_input.get_attribute('value'):
                phone_input.send_keys(CONFIG['PHONE'])
        except TimeoutException:
            print("Phone field not found or already filled")

        # Submit application
        submit_button = wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "button[aria-label='Submit application']")))
        submit_button.click()

        return verify_application_submission(wait)
    except TimeoutException as e:
        print(f"Failed to apply to job: {str(e)}")
        return False


def verify_application_submission(wait):
    # Verify if the application was submitted successfully.
    try:
        success_message = wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, ".artdeco-inline-feedback--success")))
        print("Application submitted successfully!")
        return True
    except TimeoutException:
        print("Could not verify application submission")
        return False


def main():
    """Main execution function."""
    driver = None
    try:
        driver = setup_driver()
        wait = WebDriverWait(driver, CONFIG['TIMEOUT'])

        # Execute the automation flow
        if not login(driver, wait):
            return

        if not navigate_to_job_search(driver, wait):
            return

        if not apply_to_job(driver, wait):
            return

    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")
    finally:
        # Keep browser open (due to detach option), but give user control to close
        input("Press Enter to close the browser...")
        if driver:
            driver.quit()


if __name__ == "__main__":
    main()