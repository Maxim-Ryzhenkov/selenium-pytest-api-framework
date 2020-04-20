from selenium.webdriver.common.by import By

from framework.base_page import BasePage
from framework.elements.list import List
from framework.elements.button import Button
from framework.elements.text_field import TextField


class Locators:
    SEARCH_FIELD = (By.ID, "text")
    SEARCH_BUTTON = (By.CLASS_NAME, "search2__button")
    NAVIGATION_BAR = (By.CSS_SELECTOR, ".service__name")


class YandexSearchPage(BasePage):
    def __init__(self):
        super(YandexSearchPage, self).__init__()
        self.address = ""

        self.search_field = TextField(Locators.SEARCH_FIELD)
        self.search_button = Button(Locators.SEARCH_BUTTON)
        self.navigation_bar = List(Locators.NAVIGATION_BAR)
