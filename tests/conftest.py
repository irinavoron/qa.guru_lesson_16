import os
import pytest
from selene import browser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from config import config
from utils import attach


@pytest.fixture(autouse=True, scope='function')
def browser_management():
    options = Options()

    selenoid_capabilities = {
        "browserName": "chrome",
        "browserVersion": "120.0",
        "selenoid:options": {
            "enableVideo": True,
            "enableVNC": True
        }
    }

    options.capabilities.update(selenoid_capabilities)

    selenoid_url = os.getenv('SELENOID_URL')
    selenoid_login = os.getenv('SELENOID_LOGIN')
    selenoid_password = os.getenv('SELENOID_PASSWORD')

    driver = webdriver.Remote(
        command_executor=f'https://{selenoid_login}:{selenoid_password}@{selenoid_url}',
        options=options)

    browser.config.driver = driver

    browser.config.base_url = config.BASE_URL
    browser.config.window_width = config.WINDOW_WIDTH
    browser.config.window_height = config.WINDOW_HEIGHT

    yield

    attach.add_screenshot(browser)
    attach.add_html(browser)
    attach.add_logs(browser)

    browser.quit()
