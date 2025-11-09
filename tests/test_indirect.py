import pytest
from selene import browser, have

@pytest.mark.parametrize("browser_window_size", ["Desktop"], indirect=True)
def test_click_on_sign_button_desktop(browser_window_size):
    browser.open('https://github.com/')
    browser.element("[class*=HeaderMenu-link--sign-in]").click()
    assert browser.element('.authentication-header').should(have.text('Sign in to GitHub'))

@pytest.mark.parametrize("browser_window_size", ["Mobile"], indirect=True)
def test_click_on_sign_button_mobile(browser_window_size):
    browser.open('https://github.com/')
    browser.element('a[href="/login"]').click()
    assert browser.element('.authentication-header').should(have.text('Sign in to GitHub'))