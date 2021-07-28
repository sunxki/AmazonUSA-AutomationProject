from selenium.webdriver.common.by import By

from pageObjects.ConditionOfUsePage import ConditionsOfUsePage

class CreateAccount:

    def __init__(self,driver):
        self.driver = driver

    name_field = (By.ID, "ap_customer_name")
    email_field = (By.ID, "ap_email")
    condition_of_use_link = (By.LINK_TEXT, "Conditions of Use")

    def find_name(self):
        """Return the name field on the page"""
        return self.driver.find_element(*CreateAccount.name_field)

    def find_email(self):
        """Return the name email on the page"""
        return self.driver.find_element(*CreateAccount.email_field)

    def navigate_conditions_of_use(self):
        """Create the object of the instance from the ConditionofusePage class once the related button has
        been clicked"""
        self.driver.find_element(*CreateAccount.condition_of_use_link).click()
        conditionpage = ConditionsOfUsePage(self.driver)
        return conditionpage

