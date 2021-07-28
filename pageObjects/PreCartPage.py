from selenium.webdriver.common.by import By
from pageObjects.ShoppingCartPage import ShoppingCartPage


class PreCartPage:
    def __init__(self, driver):
        self.driver = driver

    view_cart_button = (By.ID, "hlb-view-cart-announce")

    def view_cart(self):
        self.driver.find_element(*PreCartPage.view_cart_button).click()
        shoppingpage = ShoppingCartPage(self.driver)
        return shoppingpage




