from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

import logging
import utilities.logger as cl

class WebdriverClass:


    def __init__(self, browser):
        self.browser = browser

    log = cl.custom_logger(logging.DEBUG)

    def get_instance(self):
        base_url = 'https://letskodeit.teachable.com/'
        if self.browser == "chrome":
            driver = webdriver.Chrome()
            self.log.info('Running tests on Chrome.')
        elif self.browser == "edge":
            driver = webdriver.Edge()
            self.log.info('Running tests on Edge.')
        elif self.browser == "firefox":
            driver = webdriver.Firefox()
            self.log.info('Running tests on Firefox.')
        else:
            driver = webdriver.Chrome()
            self.log.info('No input for the browser, running Chrome.')
        driver.implicitly_wait(10)
        driver.get(base_url)
        return driver