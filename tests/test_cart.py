from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
import pytest

@pytest.mark.ui
def test_add_one_product_to_cart(logged_in_driver):
    """
    logged_in_driver
    1. abre navegador
    2. hace login
    3. entrega el navegador ya logueado al test
El test ya empieza logueado.
    """

    inventory_page = InventoryPage(logged_in_driver)

    inventory_page.add_backpack_to_cart()

    badge = inventory_page.get_cart_badge_text()
    assert badge == "1", f"Resultado esperado: 1 producto en el carrito, actualmente se agrego: {badge}"

def test_add_one_product_fail_intentionally(logged_in_driver):
    inventory_page = InventoryPage(logged_in_driver)

    inventory_page.add_backpack_to_cart()

    # Este test falla a propósito para validar screenshots
    badge = inventory_page.get_cart_badge_text()
    assert badge == "2", f"Resultado esperado: 2 productos en el carrito, actualmente se agrego: {badge}"