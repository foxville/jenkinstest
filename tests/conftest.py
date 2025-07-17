import pytest
import logging
import utilities.logger as cl

import pytest

from base.webdriver import WebdriverClass
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

@pytest.fixture(autouse=True)
def set_up():
    print("Before every a test.")
    yield
    print("After a test.")

@pytest.fixture(scope="class")
def one_time_set_up(request, browser):
    log = cl.custom_logger(logging.DEBUG)
    log.info("Before every a test, once.")
    webdriver_init = WebdriverClass(browser)
    driver = webdriver_init.get_instance()

    if request.cls is not None:
        request.cls.driver = driver

    yield driver
    driver.quit()
    log.info("After a test, once.")

def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")