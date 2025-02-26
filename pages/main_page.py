from .base_page import BasePage
from selenium.webdriver.common.by import By


# создаем класс MainPage как наследник класса BasePage
class MainPage(BasePage):
    # в аргументах указываем аргумент self , чтобы иметь доступ к атрибутам и методам класса:
    def go_to_login_page(self):
        # Так как браузер у нас хранится как аргумент класса BasePage, обращаться к нему нужно соответствующим образом с помощью self
        login_link = self.browser.find_element(By.CSS_SELECTOR, "#login_link")
        login_link.click()

    def should_be_login_link(self):
        assert self.is_element_present(
            By.CSS_SELECTOR, "#login_link"
        ), "Login link is not presented"
