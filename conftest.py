import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options as FirefoxOptions


# обработчик опции в функции
# добавляем параметр запуска тестов в командной строке(чем запускать, хромом или фаерфоксом) По умолчанию хром
def pytest_addoption(parser):
    # parser.addoption('--browser_name', action='store', default=None, help="Choose browser: chrome or firefox")
    # Можно задать значение параметра по умолчанию,
    # чтобы в командной строке не обязательно было указывать параметр --browser_name, например, так:
    parser.addoption(
        "--browser_name",
        action="store",
        default="chrome",
        help="Choose browser: chrome or firefox",
    )
    parser.addoption(
        "--lang",
        action="store",
        default="en",
        help="Choose language: e.g. ru, en, fr, etc.",
    )


# фикстура, которая будет обрабатывать переданные в опции данные
# Запуск браузера(для каждой функции)
@pytest.fixture(scope="function")  # по умолчанию запускается для каждой функции
def browser(request):
    browser_name = request.config.getoption(
        "browser_name"
    )  # получаем параметр командной строки browser_name
    language = request.config.getoption(
        "lang"
    )  # получаем параметр командной строки lang
    browser = None
    options = Options()

    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        options = Options()
        options.add_argument(f"--lang={language}")  # Установка языка
        browser = webdriver.Chrome(options=options)

    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        options = FirefoxOptions()
        options.set_preference(
            "intl.accept_languages", language
        )  # Установка языка для Firefox
        browser = webdriver.Firefox()

    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")

    yield browser
    print("\nquit browser..")
    browser.quit()
