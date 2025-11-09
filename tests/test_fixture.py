from selene import browser, have


def test_click_on_sign_button_desktop(browser_window_size_desktop):
    browser.open('https://github.com/')
    browser.element("[class*=HeaderMenu-link--sign-in]").click()
    assert browser.element('.authentication-header').should(have.text('Sign in to GitHub'))


def test_click_on_sign_button_mobile(browser_window_size_mobile):
    browser.open('https://github.com/')
    browser.element('a[href="/login"]').click()
    assert browser.element('.authentication-header').should(have.text('Sign in to GitHub'))