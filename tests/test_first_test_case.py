import pytest

from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass
from testData.HomePageData import HomePageData

class TestCaseOne(BaseClass):
    def test_shop_flow(self,get_data):
        log = self.getLogger()
        homepage = HomePage(self.driver)
        resultpage = homepage.perform_a_search(get_data["Search"])
        log.info(f'The keywords use on the search was {get_data["Search"]}')
        assert get_data["Search"] in resultpage.search_validation() , "The result are not the expected"
        log.warning(f'{resultpage.search_validation()} are displayed on the page')
        detailpage = resultpage.select_item_with_price()
        precartpage = detailpage.add_to_cart(resultpage.price_displayed_validator)
        shoppingcartpage = precartpage.view_cart()
        log.warning(f'Prices on the pages were {resultpage.price_displayed_validator}')
        assert resultpage.verify_prices_match(), "Prices don't match"
        log.info("Prices match")
        shoppingcartpage.delete_item()
        assert shoppingcartpage.verify_empty_cart_text(), "The message should contain Empty"
        log.info("The item was removed for the cart successfully")

    @pytest.fixture(params=HomePageData.expected_data)
    def get_data(self,request):
        return request.param










