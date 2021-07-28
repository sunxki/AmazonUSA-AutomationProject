from selenium.webdriver.common.by import By
from utilities.BaseClass import BaseClass


class ShoppingCartPage(BaseClass):
    def __init__(self, driver):
        self.driver = driver

    delete_button = [By.CSS_SELECTOR, "input[name*='submit.delete']"]
    empty_cart_val = [By.CSS_SELECTOR, "*[class*='sc-your-amazon-cart-is-empty']"]

    def delete_item(self):
        """Method to click on the delete button on the cart once a product has been added"""
        return self.driver.find_element(*ShoppingCartPage.delete_button).click()

    def verify_empty_cart_text(self):
        """Validate the (Empty) keyword is displayed on the message
        when all the product has been removed from the cart"""
        self.verify_element_present(ShoppingCartPage.empty_cart_val)
        text = self.driver.find_element(*ShoppingCartPage.empty_cart_val).text
        if "empty" in text:
            return True
        else:
            return False


