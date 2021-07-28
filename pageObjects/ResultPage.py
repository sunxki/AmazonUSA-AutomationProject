from selenium.webdriver.common.by import By
from pageObjects.DetailPage import DetailPage
from utilities.BaseClass import BaseClass


class ResultPage(BaseClass):

    def __init__(self, driver):
        self.driver = driver
        self.price_displayed_validator = []

    result_info_text = (By.CSS_SELECTOR, "div[class='a-section a-spacing-small a-spacing-top-small']")
    products_displayed = (By.CSS_SELECTOR, "div[class ='a-section a-spacing-medium']")

    item_link = (By.TAG_NAME, "a")
    item_price_tag = (By.CSS_SELECTOR, "span.a-price")
    item_title = (By.CSS_SELECTOR, "span.a-size-medium")
    price_whole = (By.CSS_SELECTOR, "span.a-price-whole")
    price_fraction = (By.CSS_SELECTOR, "span.a-price-fraction")

    def search_validation(self):
        return self.driver.find_element(*ResultPage.result_info_text).text

    def find_products_displayed(self):
        self.verify_elements_present(ResultPage.products_displayed)
        return self.driver.find_elements(*ResultPage.products_displayed)

    def select_item_with_price(self):
        products = self.find_products_displayed()
        for product in products:
            if product.find_element(*ResultPage.item_price_tag).is_displayed:
                self.get_price_formatted(product)
                product.find_element(*ResultPage.item_link).click()
                break
        detailpage = DetailPage(self.driver)
        return detailpage

    def get_price_formatted(self,product):
        whole = float(product.find_element(*ResultPage.price_whole).text)
        fraction = float(product.find_element(*ResultPage.price_fraction).text)/100
        price_formatted = whole + fraction
        self.price_displayed_validator.append(price_formatted)


    def verify_prices_match(self):
        if len(set(self.price_displayed_validator)) == 1:
            return True
        else:
            return False