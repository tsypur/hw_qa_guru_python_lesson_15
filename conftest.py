import os

import pytest
from selene import browser

@pytest.fixture(scope='function')
def browser_window_size_desktop():
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    yield
    browser.quit()


@pytest.fixture(scope='function')
def browser_window_size_mobile():
    browser.config.window_width = 380
    browser.config.window_height = 700
    yield
    browser.quit()


@pytest.fixture(params=['Desktop', 'Mobile'])
def browser_window_size(request):
    if request.param == 'Desktop':
        browser.config.window_width = 1920
        browser.config.window_height = 1080
    elif request.param == 'Mobile':
        browser.config.window_width = 380
        browser.config.window_height = 700
    yield
    browser.quit()

@pytest.fixture(params=[
    (1920, 1080),
    (1366, 768),
    (899, 667),
    (380, 700),
])
def browser_window_size_params(request):
    width, height = request.param
    browser.config.window_width = width
    browser.config.window_height = height

    if width > 900:
        device_type = "Desktop"
    else:
        device_type = "Mobile"

    yield device_type

    browser.quit()