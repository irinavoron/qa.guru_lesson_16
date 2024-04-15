import os

from selene import browser, have
from dotenv import load_dotenv


def test_login():
    load_dotenv()
    login_username = os.getenv('LOGIN_USERNAME')
    login_password = os.getenv('LOGIN_PASSWORD')
    user_name = os.getenv('USER_NAME')

    browser.open('/auth')

    browser.element('[name=login_username]').type(login_username)
    browser.element('[name=login_password]').type(login_password)
    browser.element('[type=submit]').click()
    browser.element('.ts-user-area-avatar').click()

    browser.element('.ts-popup-head').should(have.text(user_name))
