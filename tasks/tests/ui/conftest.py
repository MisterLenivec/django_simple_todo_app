from django.conf import settings
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pytest
import os


@pytest.fixture(scope='session')
def django_db_setup():
    settings.DATABASES['default'] = {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('simple_todo_db_name'),
        'USER': os.environ.get('simple_todo_db_user'),
        'PASSWORD': os.environ.get('simple_todo_db_password'),
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default="chrome",
                     help="Choose browser: chrome or firefox")


def chrome_options():
    options = Options()
    # options.add_argument("--headless")  # No open browser
    options.add_argument("--window-size=1920x1080")
    return options


def firefox_options():
    fp = webdriver.FirefoxProfile()
    return fp


@pytest.fixture(scope="session")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    browser = None

    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        browser = webdriver.Chrome(
            options=chrome_options()
        )
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        browser = webdriver.Firefox(
            firefox_profile=firefox_options()
        )
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")

    yield browser
    print("\nquit browser..")
    browser.quit()
