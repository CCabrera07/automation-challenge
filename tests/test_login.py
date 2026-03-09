from pages.login_page import LoginPage
import pytest

@pytest.mark.ui
def test_login_success(driver):
    login_page = LoginPage(driver)
    login_page.open()

    from data.test_data import STANDARD_USER, PASSWORD

    login_page.login(STANDARD_USER, PASSWORD)

    assert "inventory" in driver.current_url


def test_login_invalid_password(driver):
    login_page = LoginPage(driver)
    login_page.open()

    from data.test_data import STANDARD_USER, INVALID_PASSWORD

    login_page.login(STANDARD_USER, INVALID_PASSWORD)

    error_message = login_page.get_error_message()

    assert "Epic sadface: Username and password do not match any user in this service" in error_message, \
        f"Se esperaba mensaje de error de credenciales inválidas, recibido: {error_message}"