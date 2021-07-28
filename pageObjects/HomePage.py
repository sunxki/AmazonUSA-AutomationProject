from selenium.webdriver.common.by import By

from pageObjects.ResultPage import ResultPage
from pageObjects.SignInPage import SignInPage


class HomePage:
    search_Bar = (By.CSS_SELECTOR, "input[name='field-keywords']")
    search_button = (By.CSS_SELECTOR, "span[id='nav-search-submit-text'] input")
    hello_button = (By.ID,"nav-link-accountList-nav-line-1")
    def __init__(self , driver):
        self.driver = driver

    def perform_a_search(self,search):
        """Create the object of the instance from the Resultpage class once the search bar was used"""
        self.driver.find_element(*HomePage.search_Bar).send_keys(search)
        self.driver.find_element(*HomePage.search_button).click()
        resultpage = ResultPage(self.driver)
        return resultpage

    def find_helllo_button(self):
        """Create the object of the instance from the SignInpage class once the related button has been clicked"""
        self.driver.find_element(*HomePage.hello_button).click()
        signpage = SignInPage(self.driver)
        return signpage
