import allure
from selene import browser, have

from config import config


def test_login():
    login_username = config.LOGIN_USERNAME
    login_password = config.LOGIN_PASSWORD
    user_name = config.USER_NAME

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
