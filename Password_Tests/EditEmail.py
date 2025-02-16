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


# Test: Validate editing the email address
def test_edit_email():
    driver = setup_driver()
    driver.get(
        "https://identity.hudl.com/u/login/identifier?state=hKFo2SBHdmlMT1hOWHczUFRrVXNMaWRERjdBMVdlZGZXNWVKbaFur3VuaXZlcnNhbC1sb2dpbqN0aWTZIGo3amhpd1Z0b05GUzdEV1o4QXVnNW9RT1BGVHVDb3cwo2NpZNkgbjEzUmZrSHpLb3phTnhXQzVkWlFvYmVXR2Y0V2pTbjU")

    try:
        # Enter email
        time.sleep(3)
        email_input = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.ID, "username")))
        email_input.clear()
        email_input.send_keys("chetpatel26@googlemail.com")
        time.sleep(3)

        # Click continue button
        continue_button = WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@data-action-button-primary='true']")))
        driver.execute_script("arguments[0].click();", continue_button)
        time.sleep(5)

        # Click Edit email button
        edit_button = WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, "//a[@data-link-name='edit-username']")))
        driver.execute_script("arguments[0].click();", edit_button)
        time.sleep(5)

        # Validate email input box is present
        email_input = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.ID, "username")))
        assert email_input.is_displayed(), "Email input box is not displayed after clicking Edit."
        assert email_input.get_attribute("value") == "chetpatel26@googlemail.com", "Email value did not persist."
        print("Test Passed: Email input box is present and contains the previous email.")

        # Enter new email
        email_input.clear()
        email_input.send_keys("testuser@hotmail.com")
        time.sleep(3)  # Allow time to visually confirm input
        print("Test Passed: New email entered successfully.")

    except Exception as e:
        print(f"Test Failed: {e}")

    time.sleep(10)  # Wait to observe result
    driver.quit()


# Run the test
if __name__ == "__main__":
    test_edit_email()
