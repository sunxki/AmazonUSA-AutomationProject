from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from testData.CreateAccountPageData import CreateAccountData


class ConditionsOfUsePage(CreateAccountData):

    def __init__(self, driver):
        self.driver = driver
        self.link_validator = []

    help_bar = (By.ID,"helpsearch")
    results_on_page = (By.CSS_SELECTOR, "div[class*='cs-help-search-results'] h2 a")
    displayed_links = (By.XPATH, "//div[@id='links-contain']//h3")

    def perform_a_search(self,option):
        """Method to performed a search, option is a string string to send the value to the field"""
        self.driver.find_element(*ConditionsOfUsePage.help_bar).send_keys(option)
        self.driver.find_element(*ConditionsOfUsePage.help_bar).send_keys(Keys.ENTER)

    def navigate_result(self,option):
        """Logic to find the desire option to navigate from the result fron the search on the page"""
        title_links = self.driver.find_elements(*ConditionsOfUsePage.results_on_page)
        for title in title_links:
            if title.text == option:
                title.click()
            break

    def get_links(self):
        """Method to validate the expected option on the page are displayed"""
        links = self.driver.find_elements(*ConditionsOfUsePage.displayed_links)
        for link in links:
            self.link_validator.append(link.text)
        self.link_validator.remove("Learn More")
        return self.link_validator













