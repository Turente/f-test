from .base_page import BasePage
from .locators import ProductPageLocators
import time


class ProductPage(BasePage):
    def should_be_product_page(self):
        self.should_be_product_url()
        self.should_be_write_review_button()
        self.should_be_add_to_basket_button()
        self.should_be_product_name()
        self.should_be_product_price()

    def should_be_product_url(self):
        current_url = self.browser.current_url
        # substring = "?promo=newYear" активирую при выборе отдельной ссылки в тесте
        substring = "?promo=offer"
        assert substring in current_url, "Product page. Invalid URL"

    def should_be_write_review_button(self):
        assert self.is_element_present(
            *ProductPageLocators.WRITE_REVIEW_BUTTON
        ), "Product page. There is no write review button"

    def should_be_add_to_basket_button(self):
        assert self.is_element_present(
            *ProductPageLocators.ADD_TO_BASKET_BUTTON
        ), "Product page. There is no add to basket button"

    def should_be_product_name(self):
        assert self.is_element_present(
            *ProductPageLocators.PRODUCT_NAME
        ), "Product page. There is no product name"

    def should_be_product_price(self):
        assert self.is_element_present(
            *ProductPageLocators.PRODUCT_PRICE
        ), "Product page. There is no product name"

    # добавление товара в корзину
    def add_to_basket(self):
        self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON).click()

    # проверка сообщений о добавлении продукта в корзину
    def should_be_message_adding_to_basket_product(self):
        time.sleep(2)
        self.should_be_message_adding_to_basket_product_name()
        self.should_be_message_adding_to_basket_product_price()
        self.should_be_product_name_included_in_message()
        self.should_be_product_price_included_in_message()

    def should_be_message_adding_to_basket_product_name(self):
        assert self.is_element_present(
            *ProductPageLocators.MESSAGE_BASKET_PRODUCT_NAME
        ), "Product page. There is no message adding to basket product name"

    def should_be_product_name_included_in_message(self):
        product = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        message = self.browser.find_element(
            *ProductPageLocators.MESSAGE_BASKET_PRODUCT_NAME
        ).text
        assert product == message, f"Product page. {product} not equal {message}"

    def should_be_message_adding_to_basket_product_price(self):
        assert self.is_element_present(
            *ProductPageLocators.MESSAGE_BASKET_PRODUCT_PRICE
        ), "Product page. There is no message adding to basket product price"

    def should_be_product_price_included_in_message(self):
        price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        message = self.browser.find_element(
            *ProductPageLocators.MESSAGE_BASKET_PRODUCT_PRICE
        ).text
        assert price == message, f"Product page. {price} not equal {message}"
