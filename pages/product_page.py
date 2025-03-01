from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class ProductPage(BasePage):
    def should_be_product_page(self):
        self.should_be_product_url()
        self.should_be_write_review_button()
        self.should_be_add_to_basket_button()
        self.should_be_product_name()
        self.should_be_product_price()

    def should_be_product_url(self):
        current_url = self.browser.current_url
        substring = "?promo=newYear"  # активирую при выборе отдельной ссылки в тесте
        # substring = "?promo=offer"
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
        self.should_be_message_adding_to_basket_product_name()
        self.should_be_message_adding_to_basket_product_price()
        self.should_be_product_name_included_in_message()
        self.should_be_product_price_included_in_message()

    def should_be_message_adding_to_basket_product_name(self):
        """Проверяем, что сообщение о добавлении продукта в корзину отображает название."""
        try:
            WebDriverWait(self.browser, 10).until(
                EC.presence_of_element_located(
                    ProductPageLocators.MESSAGE_BASKET_PRODUCT_NAME
                )
            )
        except TimeoutException:
            assert (
                False
            ), "Product page. There is no message adding to basket product name"

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
        """Проверяем, что сообщение о добавлении продукта в корзину отображает цену."""
        try:
            WebDriverWait(self.browser, 10).until(
                EC.presence_of_element_located(
                    ProductPageLocators.MESSAGE_BASKET_PRODUCT_PRICE
                )
            )
        except TimeoutException:
            assert (
                False
            ), "Product page. There is no message adding to basket product price"

        assert self.is_element_present(
            *ProductPageLocators.MESSAGE_BASKET_PRODUCT_PRICE
        ), "Product page. There is no message adding to basket product price"

    def should_be_product_price_included_in_message(self):
        price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        message = self.browser.find_element(
            *ProductPageLocators.MESSAGE_BASKET_PRODUCT_PRICE
        ).text
        assert price == message, f"Product page. {price} not equal {message}"

    # проверка, что элемент не появляется на странице в течение заданного времени
    def should_not_be_success_message(self):
        assert self.is_not_element_present(
            *ProductPageLocators.SUCCESS_MESSAGE
        ), "Product page. Success message is presented, but should not be"

    # проверка, что элемент исчез в течении заданного времени
    def should_be_disappeared_success_message(self):
        assert self.is_disappeared(
            *ProductPageLocators.SUCCESS_MESSAGE
        ), "Product page. Success message does not disappear, it should disappear"
