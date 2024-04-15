import os

import allure
from selene import browser, have
from dotenv import load_dotenv


def test_login():
    load_dotenv()
    login_username = os.getenv('LOGIN_USERNAME')
    login_password = os.getenv('LOGIN_PASSWORD')
    user_name = os.getenv('USER_NAME')

    with allure.step('Open login page'):
        browser.open('/auth')

    with allure.step('Fill login form'):
        browser.element('[name=login_username]').type(login_username)
        browser.element('[name=login_password]').type(login_password)

    with allure.step('Submit login form'):
        browser.element('[type=submit]').click()

    with allure.step('Check user name after login'):
        browser.element('.ts-user-area-avatar').click()
        browser.element('.ts-popup-head').should(have.text(user_name))
