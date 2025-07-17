from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class LoginPageLocators:

    def __init__(self, driver):
        self.driver = driver

    # Locators
    _transfer_to_login_screen_button = "//a[@class='navbar-link fedora-navbar-link']"
    _login_field = "//input[@id='email']"
    _login_button = "//button[@id='otp-login-btn']"
    _login_field = "//input[@id='email']"
    _verify_button = "//span[contains(text(), 'Verify')]"


    def get_transfer_to_login_screen_button(self):
        return self.driver.find_element(By.XPATH,
                                        self._transfer_to_login_screen_button)

    def login_field(self):
        return WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, self._login_field)))

    def login_button(self):
        return WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, self._login_button)))