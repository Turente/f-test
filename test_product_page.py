from pages.product_page import ProductPage
from pages.login_page import LoginPage
import pytest
import time


# @pytest.mark.parametrize(
#    "link",
#   [
#     "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
#      "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
#      "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
#     "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
#     "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
#     "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
#     "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
#     pytest.param(
#          "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
#         marks=pytest.mark.xfail,
#     ),
#     "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
#     "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9",
#   ],
# )
def test_guest_can_add_product_to_basket(
    browser,
):  # ,link): # если убираем параметризацию - тут нужно убрать линк
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"  # проверка отдельной ссылки, перед этим убрать параметризацию
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.should_be_product_page()
    product_page.add_to_basket()
    product_page.solve_quiz_and_get_code()
    product_page.should_be_message_adding_to_basket_product()


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()  # проверки страницы логина
