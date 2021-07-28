from selenium.webdriver.common.by import By

from pageObjects.CreateAccountPage import CreateAccount

class SignInPage:

    create_account_button = (By.ID, "createAccountSubmit")

    def __init__(self , driver):
        self.driver = driver

    def get_create_button(self):
        self.driver.find_element(*SignInPage.create_account_button).click()
        createpage = CreateAccount(self.driver)
        return createpage