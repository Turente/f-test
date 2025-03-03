from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math
from .locators import BasePageLocators


# конструктор — метод, который вызывается, когда мы создаем объект
class BasePage:

    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

        # в аргументах указываем аргумент self , чтобы иметь доступ к атрибутам и методам класса:

    def go_to_login_page(self):
        # Так как браузер у нас хранится как аргумент класса BasePage, обращаться к нему нужно соответствующим образом с помощью self
        link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        link.click()
        # return LoginPage(browser=self.browser, url=self.browser.current_url)

    def go_to_basket_page(self):
        link = self.browser.find_element(*BasePageLocators.BASKET_LINK)
        link.click()

    def should_be_login_link(self):
        assert self.is_element_present(
            *BasePageLocators.LOGIN_LINK
        ), "Main page. Login link is not presented"

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    # метод для получения проверочного кода; для проверки того, что тест написан на Selenium
    def solve_quiz_and_get_code(self):
        try:
            # Ожидание появления первого алерта
            alert = WebDriverWait(self.browser, 10).until(EC.alert_is_present())
            x = alert.text.split(" ")[2]
            try:
                # Вычисление ответа
                answer = str(math.log(abs((12 * math.sin(float(x))))))
                alert.send_keys(answer)
                alert.accept()
            except ValueError as e:
                print(f"Error calculating answer: {e}")
                return
        except NoAlertPresentException:
            print("No alert present before solving the quiz")
            return

        try:
            # Ожидание появления второго алерта
            alert = WebDriverWait(self.browser, 10).until(EC.alert_is_present())
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    # метод, который проверяет, что элемент не появляется на странице в течение заданного времени
    # упадет, как только увидит искомый элемент. Не появился: успех, тест зеленый
    def is_not_element_present(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(
                EC.presence_of_element_located((how, what))
            )
        except TimeoutException:
            return True

        return False

    # проверка, что какой-то элемент исчезает
    # будет ждать до тех пор (4 секунды), пока элемент не исчезнет
    # если элемент не исчезает - вернет False, если исчез - вернет True
    def is_disappeared(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException).until_not(
                EC.presence_of_element_located((how, what))
            )
        except TimeoutException:
            return False

        return True

    # проверка, что пользователь залогинен
    def should_be_authorized_user(self):
        assert self.is_element_present(*BasePageLocators.USER_ICON), "User icon is not presented," \
                                                                 " probably unauthorised user"