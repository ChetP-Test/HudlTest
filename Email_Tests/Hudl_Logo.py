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


# Test: Validate Hudl logo presence on login page
def test_hudl_logo_presence():
    driver = setup_driver()
    driver.get(
        "https://identity.hudl.com/u/login/identifier?state=hKFo2SBHdmlMT1hOWHczUFRrVXNMaWRERjdBMVdlZGZXNWVKbaFur3VuaXZlcnNhbC1sb2dpbqN0aWTZIGo3amhpd1Z0b05GUzdEV1o4QXVnNW9RT1BGVHVDb3cwo2NpZNkgbjEzUmZrSHpLb3phTnhXQzVkWlFvYmVXR2Y0V2pTbjU")

    try:
        # Wait for the Hudl logo to be visible
        time.sleep(3)  # Slow down execution for observation
        hudl_logo = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.ID, "custom-prompt-logo")))
        assert hudl_logo.is_displayed(), "Hudl logo is not displayed on the login page"
        print("Test Passed: Hudl logo is present on login page.")

    except Exception as e:
        print(f"Test Failed: {e}")

    time.sleep(10)  # Wait to observe result
    driver.quit()


# Run the test
if __name__ == "__main__":
    test_hudl_logo_presence()
