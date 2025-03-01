from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_basket_page_empty(self):
        self.should_be_basket_url()
        self.should_not_be_product()
        self.should_be_text_basket_empty()

    def should_be_basket_url(self):
        current_url = self.browser.current_url
        substring = "basket"
        assert substring in current_url, "Basket page. Invalid URL"

    def should_not_be_product(self):
        assert self.is_not_element_present(
            *BasketPageLocators.PRODUCT_IN_BASKET
        ), "Basket page. Product is presented, but should not be"

    def should_be_text_basket_empty(self):
        text = self.browser.find_element(*BasketPageLocators.CONTENT_INNER).text
        assert (
            text == "Your basket is empty. Continue shopping"
        ), f"Basket page. {text} not equal 'Your basket is empty. Continue shopping'"
