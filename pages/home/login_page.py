from base.basepage import BasePage

import logging
import utilities.logger as cl

class LoginPage(BasePage):

    log = cl.custom_logger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    _transfer_to_login_screen_button = "//a[@class='navbar-link fedora-navbar-link']"
    _login_field = "//input[@id='email']"
    _log_in_button = "//span[contains(text(), 'Log In')]"
    _error_blank = "//span[@id='my-error-id']"
    _verify_button = "//span[contains(text(), 'Verify')]"
    _invalid_code_error = "//div[contains(text(), 'Invalid code. Please try again.')]"


    def error_blank(self):
        return self.get_element(self._error_blank, "XPATH")

    def invalid_code_error(self):
        return self.get_element(self._invalid_code_error, "XPATH")


    def click_login_screen_button(self):
        self.element_click(self._transfer_to_login_screen_button, "XPATH" )

    def click_login_button(self):
        self.element_click(self._log_in_button, "XPATH")

    def enter_email(self, email):
        self.element_send_keys(self._login_field, "XPATH", email)

    def verify_code(self):
        self.element_click(self._verify_button, "XPATH")

    def verify_error_blank(self):
        return self.element_presence(self.error_blank())

    def verify_title_name(self):
        return self.verify_page_title("123")