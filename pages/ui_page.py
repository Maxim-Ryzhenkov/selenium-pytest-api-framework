from selenium.webdriver.common.by import By

from framework.base_page import BasePage
from framework.elements.list import List
from framework.elements.button import Button
from framework.elements.text_field import TextField


class YandexSearchPage(BasePage):
    """ Класс отдельной страницы наследуется от BasePage
        В конструкторе запускается метод __init__() родительского класса
        И инициализируются UI элементы принадлежащие странице.
        В классе можно создать вспомогательные методы-хэлперы
        объединяющие часто повторяющиеся действия в цепочки. И другие, по необходимости.
        """
    def __init__(self):
        super(YandexSearchPage, self).__init__()
        self.address = ""

        """ инициализируем UI элементы """
        self.search_field = TextField('Поле поиска', locator="text", loc_type=By.ID)
        self.search_button = Button('Кнопка "Search"', locator="search2__button", loc_type=By.CLASS_NAME)
        self.navigation_bar = List('Список результатов поиска', locator=".service__name", loc_type=By.CSS_SELECTOR)
