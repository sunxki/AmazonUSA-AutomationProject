import pytest
from pageObjects.HomePage import HomePage
from testData.CreateAccountPageData import CreateAccountData
from utilities.BaseClass import BaseClass

class TestCaseTwo(BaseClass):
    def test_support_flow(self, get_api, get_data):
        log = self.getLogger()
        homepage = HomePage(self.driver)
        signpage = homepage.find_helllo_button()
        log.info("The Hello, Sign In Account & lists was button was found")
        createpage = signpage.get_create_button()
        log.info("Create account page was displayed")
        createpage.find_name().send_keys(get_api["employee_name"])
        log.info(f'The name provided was {get_api["employee_name"]}')
        createpage.find_email().send_keys(self.generate_email(get_api["employee_name"]))
        log.info(f'The email provided was {self.generate_email(get_api["employee_name"])}')
        conditionpage = createpage.navigate_conditions_of_use()
        conditionpage.perform_a_search(get_data["pre_search"])
        log.info(f'The input on the search {get_data["pre_search"]}')
        self.verify_link_present(get_data["desired"])
        conditionpage.navigate_result(get_data["desired"])
        assert get_data["Expected_Links"] == conditionpage.get_links()
        log.info("The options expected are displayed")

    @pytest.fixture(params=CreateAccountData.data)
    def get_api(self,request):
        return request.param

    @pytest.fixture(params=CreateAccountData.expected_data)
    def get_data(self, request):
        return request.param
