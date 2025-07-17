import datetime
import logging
import time
import os
from csv import excel

import utilities.logger as cl

from traceback import print_stack

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import *
from selenium.webdriver.support import expected_conditions as EC




class SeleniumDriver:

    log = cl.custom_logger(logging.DEBUG)

    def __init__(self, driver):
        self.driver = driver

    def take_screenshot(self, result_message):
        """Takes screenshot of the current webpage."""
        file_name = result_message + "." + str(round(time.time() * 1000)) + ".png"
        screenshots_dir = "../screenshots/" #.. go 1 lvl up

        relative_filename = screenshots_dir + file_name
        current_dir = os.path.dirname(__file__)
        destination_file = os.path.join(current_dir, relative_filename)
        destination_dir = os.path.join(current_dir, screenshots_dir)

        try:
            if not os.path.exists(destination_dir):
                os.makedirs(destination_dir)
            self.driver.save_screenshot(destination_file)
            self.log.info("Screenshot saved to: " + destination_file)
        except:
            self.log.error("Error occurred.")
            print_stack()


    def get_title(self):
        return self.driver.title

    def get_by_type(self, locator_type):
        locator_type = locator_type.lower()
        if locator_type == "id":
            return By.ID
        elif locator_type == "xpath":
            return By.XPATH
        elif locator_type == "classname":
            return By.CLASS_NAME
        elif locator_type == "name":
            return By.NAME
        elif locator_type == "css":
            return By.CSS_SELECTOR
        elif locator_type == "linktext":
            return By.LINK_TEXT
        else:
            self.log.info("Locator type is not supported.")
        return False

    def get_element(self, locator, locator_type="id"):
        element = None
        try:
            locator_type = locator_type.lower()
            by_type = self.get_by_type(locator_type)
            element = self.driver.find_element(by_type, locator)
            self.log.info('Element found!')
        except:
            self.log.info('Element not found!')
        return element

    def element_presence(self, locator, by_type):
        try:
            element = self.driver.find_element(by_type, locator)
            if element is not None:
                return True
            else:
                self.log.info('Element not found!')
                return False
        except:
            self.log.info('Element not found!')
            return False

    def elements_presence(self, locator, by_type):
        try:
            elements = self.driver.find_elements(by_type, locator)
            if len(elements) > 0:
                self.log.info('Element Found')
                return True
            else:
                self.log.info('Element not found!')
                return False
        except:
            self.log.info('Element not found!')
            return False

    def element_click(self, locator, locator_type="id"):
        try:
            element = self.get_element(locator, locator_type)
            element.click()
            self.log.info("Clicked on the element, locator: " + locator + ", locator type: " + locator_type + ".")
        except:
            self.log.info("Element can't be clicked. Locator: " + locator + ", locator type: " + locator_type + ".")
            print_stack()

    def element_send_keys(self, locator, locator_type="id", text=""):
        try:
            element = self.get_element(locator, locator_type)
            element.send_keys(text)
            self.log.info(f"Sent text {text} into the element.")
        except:
            self.log.info("Text can't be send.")
            print_stack()

    def wait_for_element(self, locator, locator_type = 'id', timeout=10,
                         poll_frequency=0.5):
        element = None
        try:
            by_type = self.get_by_type(locator_type)
            self.log.info("Waiting for maximum :: " + str(timeout) +
                  " :: seconds for element to be clickable")
            wait = WebDriverWait(self.driver, 10, poll_frequency=1,
                                 ignored_exceptions=[NoSuchElementException,
                                                     ElementNotVisibleException,
                                                     ElementNotSelectableException])
            element = wait.until(EC.element_to_be_clickable(
                (by_type, "stopFilter_stops-0")))
            self.log.info('Element appeared on the page.')
        except:
            self.log.info("Element hasn't appeared on the page.")
            print_stack()
        return element