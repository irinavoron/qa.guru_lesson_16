from selene import browser, have


def test_login():
    browser.open('/auth')

    browser.element('[name=login_username]').type('yarutich.irina@gmail.com')
    browser.element('[name=login_password]').type('150424mg')
    browser.element('[type=submit]').click()
    browser.element('.ts-user-area-avatar').click()

    browser.element('.ts-popup-head').should(have.text('yarutich.irina'))
