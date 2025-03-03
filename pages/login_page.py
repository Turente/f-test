from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # проверка на корректный url адрес
        current_url = self.browser.current_url
        substring = "login"
        assert substring in current_url, "Login page. There is no login URL"

    def should_be_login_form(self):
        # проверка, что есть форма логина
        assert self.is_element_present(
            *LoginPageLocators.LOGIN_FORM
        ), "Login page. There is no login form"

    def should_be_register_form(self):
        # проверка, что есть форма регистрации на странице
        assert self.is_element_present(
            *LoginPageLocators.REGISTER_FORM
        ), "Login page. There is no register form"

    def register_new_user(self, email, password):
        self.browser.find_element(*LoginPageLocators.REGISTER_EMAIL).send_keys(email)
        self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD).send_keys(
            password
        )
        self.browser.find_element(
            *LoginPageLocators.REGISTER_CONFIRM_PASSWORD
        ).send_keys(password)
        self.browser.find_element(*LoginPageLocators.BUTTON_REGISTER).click()
