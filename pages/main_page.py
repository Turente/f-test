from .base_page import BasePage
from .locators import MainPageLocators


# Создаем класс MainPage как наследник класса BasePage
# __init__: Это специальный метод инициализации (конструктор) в Python.
# Вызывая super().__init__(), вы вызываете конструктор родительского класса (BasePage),
# что позволяет ему выполнить свою логику и инициализировать любые атрибуты, которые он может иметь.
# Конструктор с ключевым словом super на самом деле только вызывает конструктор класса предка и
# передает ему все те аргументы, которые мы передали в конструктор MainPage.
# Это заглушка
class MainPage(BasePage):
    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)
