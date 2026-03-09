import os
from datetime import datetime
import pytest
from selenium import webdriver
from pytest_html import extras
import base64

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")


def pytest_configure(config):
    browser = config.getoption("--browser")
    if hasattr(config, "_metadata"):
        config._metadata["Browser"] = browser

@pytest.fixture
def driver(request):
    browser = request.config.getoption("--browser")

    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "firefox":
        driver = webdriver.Firefox()

    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture
def logged_in_driver(driver):
    from pages.login_page import LoginPage

    login_page = LoginPage(driver)
    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    return driver


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        driver = item.funcargs.get("driver")

        if driver:
            os.makedirs("screenshots", exist_ok=True)

            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            file_name = f"{item.name}_{timestamp}.png"
            file_path = os.path.join("screenshots", file_name)

            driver.save_screenshot(file_path)

            with open(file_path, "rb") as image_file:
                encoded = base64.b64encode(image_file.read()).decode()

            extra = getattr(report, "extra", [])
            extra.append(extras.image(encoded, mime_type="image/png"))
            report.extra = extra