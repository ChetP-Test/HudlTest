from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.firefox import GeckoDriverManager
import time




def setup_driver():
    """Sets up the Firefox WebDriver."""
    options = Options()
    options.add_argument("--start-maximized")
    service = Service(GeckoDriverManager().install())
    driver = webdriver.Firefox(service=service, options=options)
    return driver


# Test: Validate Create Account link navigation
def test_create_account_navigation():
    driver = setup_driver()
    driver.get(
        "https://identity.hudl.com/u/login/identifier?state=hKFo2SBHdmlMT1hOWHczUFRrVXNMaWRERjdBMVdlZGZXNWVKbaFur3VuaXZlcnNhbC1sb2dpbqN0aWTZIGo3amhpd1Z0b05GUzdEV1o4QXVnNW9RT1BGVHVDb3cwo2NpZNkgbjEzUmZrSHpLb3phTnhXQzVkWlFvYmVXR2Y0V2pTbjU")

    try:
        # Click Create Account link
        time.sleep(3)
        create_account_link = WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, "//a[contains(text(),'Create Account')]")))
        driver.execute_script("arguments[0].click();", create_account_link)
        time.sleep(5)  # Wait for navigation to complete

        # Validate that the First Name and Last Name input fields are present
        first_name_input = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.ID, "first-name")))
        last_name_input = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.ID, "last-name")))

        assert first_name_input.is_displayed(), "First Name input field is not displayed."
        assert last_name_input.is_displayed(), "Last Name input field is not displayed."
        print("Test Passed: Create Account page loaded with required fields.")

    except Exception as e:
        print(f"Test Failed: {e}")

    time.sleep(10)  # Wait to observe result
    driver.quit()


# Run the test
if __name__ == "__main__":
    test_create_account_navigation()
