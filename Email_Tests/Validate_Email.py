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


# Test: Validate password field appears after entering email and clicking Continue
def test_password_field_appears():
    driver = setup_driver()
    driver.get(
        "https://identity.hudl.com/u/login/identifier?state=hKFo2SBHdmlMT1hOWHczUFRrVXNMaWRERjdBMVdlZGZXNWVKbaFur3VuaXZlcnNhbC1sb2dpbqN0aWTZIGo3amhpd1Z0b05GUzdEV1o4QXVnNW9RT1BGVHVDb3cwo2NpZNkgbjEzUmZrSHpLb3phTnhXQzVkWlFvYmVXR2Y0V2pTbjU")

    try:
        # Enter email
        time.sleep(3)
        email_input = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.ID, "username")))
        email_input.clear()
        email_input.send_keys("chetpatel26@googlemail.com")
        time.sleep(3)  # Slow down execution for observation

        # Click continue button
        continue_button = WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@data-action-button-primary='true']")))
        driver.execute_script("arguments[0].click();", continue_button)
        time.sleep(5)  # Wait for password field to appear

        # Validate that the password input box appears
        password_input = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.ID, "password")))
        assert password_input.is_displayed(), "Password field did not appear after clicking Continue."
        print("Test Passed: Password field appeared successfully.")

    except Exception as e:
        print(f"Test Failed: {e}")

    time.sleep(10)  # Wait to observe result
    driver.quit()


# Run the test
if __name__ == "__main__":
    test_password_field_appears()