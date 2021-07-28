from selenium.webdriver.common.by import By

from pageObjects.PreCartPage import PreCartPage


class DetailPage:
    def __init__(self , driver):
        self.driver = driver

    add_cart_button = (By.ID, "add-to-cart-button")
    price_on_page = (By.ID, "priceblock_ourprice")
    price_on_box = (By.ID, "price_inside_buybox")

    def add_to_cart (self,price_stored):
        price_stored.extend(self.get_prices())
        self.driver.find_element(*DetailPage.add_cart_button).click()
        precartpage = PreCartPage(self.driver)
        return precartpage

    def get_prices(self):
        price_1 = float((self.driver.find_element(*DetailPage.price_on_page).text).replace("$", ""))
        price_2 = float((self.driver.find_element(*DetailPage.price_on_box).text).replace("$", ""))
        return [price_1, price_2]







