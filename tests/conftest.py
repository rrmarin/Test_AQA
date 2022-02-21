from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import pytest
import os


@pytest.fixture(scope="class")
def browser(request):
    browser_type = request.config.getoption("browser")
    browsers = {
        "firefox": webdriver.Firefox,
        "chrome": webdriver.Chrome
    }
    browser = browsers[browser_type]()
    browser.maximize_window()
    yield browser
    browser.close()


@pytest.fixture(scope="class")
def wait(browser):
    wait = WebDriverWait(browser, 10)
    return wait


def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        default=os.getenv("BROWSER", "firefox"),
        choices= ["firefox", "chrome"],
        help="Select from FF, Chrome",
    )

    parser.addoption(
        "--base-url",
        metavar="url",
        default=os.getenv("BASE_URL", None),
        help="Base url for the application under test.",
    )


@pytest.fixture(scope="session")
def base_url(request):
    base_url = request.config.getoption("base_url")
    if base_url is not None:
        return base_url
    pytest.exit("Please provide base url.")



