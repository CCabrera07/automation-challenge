from selenium.webdriver.common.by import By


class InventoryPage:
    BACKPACK_ADD_BUTTON = (By.ID, "add-to-cart-sauce-labs-backpack")
    BIKE_LIGHT_ADD_BUTTON = (By.ID, "add-to-cart-sauce-labs-bike-light")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")

    def __init__(self, driver):
        self.driver = driver

    def add_backpack_to_cart(self):
        self.driver.find_element(*self.BACKPACK_ADD_BUTTON).click()

    def add_bike_light_to_cart(self):
        self.driver.find_element(*self.BIKE_LIGHT_ADD_BUTTON).click()

    def get_cart_badge_text(self):
        return self.driver.find_element(*self.CART_BADGE).text