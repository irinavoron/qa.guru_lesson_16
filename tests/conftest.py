import pytest
from selene import browser


@pytest.fixture(autouse=True, scope='function')
def browser_management():
    browser.config.base_url = 'https://mamago.by'
    browser.config.window_width = 1896
    browser.config.window_height = 1096

    yield

    browser.quit()