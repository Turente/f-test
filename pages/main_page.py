from .base_page import BasePage
from .locators import MainPageLocators


# создаем класс MainPage как наследник класса BasePage
class MainPage(BasePage):
    # в аргументах указываем аргумент self , чтобы иметь доступ к атрибутам и методам класса:
    def go_to_login_page(self):
        # Так как браузер у нас хранится как аргумент класса BasePage, обращаться к нему нужно соответствующим образом с помощью self
        link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        link.click()
        # return LoginPage(browser=self.browser, url=self.browser.current_url)

    def should_be_login_link(self):
        assert self.is_element_present(
            *MainPageLocators.LOGIN_LINK
        ), "Main page. Login link is not presented"
