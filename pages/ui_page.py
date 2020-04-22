from selenium.webdriver.common.by import By

from framework.base_page import BasePage
from framework.elements.table import Table
from framework.elements.button import Button
from framework.elements.text_field import TextField


class UiPage(BasePage):
    """ Класс отдельной страницы наследуется от BasePage
        В конструкторе запускается метод __init__() родительского класса
        И инициализируются UI элементы принадлежащие странице.
        В классе можно создать вспомогательные методы-хэлперы
        объединяющие часто повторяющиеся действия в цепочки. И другие, по необходимости.
        """

    def __init__(self):
        super(UiPage, self).__init__()
        self.address = ""

        """ инициализируем UI элементы """
        #   Форма подписки
        self.text_field_name = TextField('Поле "Имя пользователя"', locator="name", loc_type=By.NAME)
        self.text_field_email = TextField('Поле "Email"', locator="email", loc_type=By.NAME)
        self.text_field_time = TextField('Поле "Время"', locator="time", loc_type=By.NAME)
        self.btn_subscribe = Button('Кнопка "Подписаться"',
                                    locator='.btn-success', loc_type=By.CSS_SELECTOR)

        #  Таблица со списком подписок
        self.subscribtions_table = Table('Таблица подписок', locator="tbody", loc_type=By.TAG_NAME)

        #   Кнопки Refresh и  Delete
        self.btn_sync = Button('Кнопка "Обновить"', locator='[data-test="sync-button"]', loc_type=By.CSS_SELECTOR)
        self.btn_clear = Button('Кнопка "Обновить"', locator='[data-test="clear-button"]', loc_type=By.CSS_SELECTOR)

    def set_email(self, value):
        self.text_field_email.set_value(value)

    def set_name(self, value):
        self.text_field_name.set_value(value)

    def set_time(self, value):
        self.text_field_time.set_value(value)

    def push_subscribe_button(self):
        self.btn_subscribe.click()

    def add_subscription(self, email, name, time):
        self.set_email(email)
        self.set_name(name)
        self.set_time(time)
        self.push_subscribe_button()

    def sync_subscriptions_list(self):
        self.btn_sync.click()

    def clear_subscriptions_list(self):
        self.btn_clear.click()
