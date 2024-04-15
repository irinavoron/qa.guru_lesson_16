import allure
from selene import browser, have

from config import config


def test_login():
    with allure.step('Open login page'):
        browser.open('/auth')

    with allure.step('Fill login form'):
        browser.element('[name=login_username]').type(config.LOGIN_USERNAME)
        browser.element('[name=login_password]').type(config.LOGIN_PASSWORD)

    with allure.step('Submit login form'):
        browser.element('[type=submit]').click()

    with allure.step('Check user name after login'):
        browser.element('.ts-user-area-avatar').click()
        browser.element('.ts-popup-head').should(have.text(config.USER_NAME))
