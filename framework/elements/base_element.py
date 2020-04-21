from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from framework.driver import Driver


class BaseElement(object):
    """ Элементы интерфейса умеють совершать с собой все действия,
        свойственные данному виду элементов интерфейса.
        Базовый класс описывает свойства и поведение, общие для всех элементов.
        Спецефические свойства элементов, таких как чекбоксы, слайдеры,
        выпадающие списки описываются в производных классах.
        """
    def __init__(self, name, locator, loc_type):
        self.locator = locator
        self.locator_type = loc_type
        self.name = name
        self.driver = Driver().connect()

    def click(self):
        """ Клик мышью на элементе """
        self.find_element().click()

    def find_element(self, timeout=5):
        """ Найти и вернуть объект UI элемента """
        return WebDriverWait(self.driver, timeout=timeout).until(
            EC.presence_of_element_located((self.locator_type, self.locator)),
            message=f"Can't find '{self.name}' element by locator '{self.locator}'")

    def find_elements(self, timeout=5):
        """ Найти и вернуть список объектов """
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_all_elements_located((self.locator_type, self.locator)),
            message=f"Can't find elements by locator {self.locator}")

    def get_value(self):
        """ Метод общий для элементов, но поскольку способ получения
            и тип возвращаемого будет спецефическим для разных элементов,
            то данный метод должен переопределятьс в дочерних классах.
            Например Слайдер будет возвращать проценты в диапазоне 0-100,
            а Чекбокс будет возвращать True или False
            """
        raise NotImplementedError

    def set_value(self, *args):
        """ Метод общий для элементов, но поскольку способ передачи
            и тип передаваемого значения будет спецефическим для разных элементов,
            то данный метод должен переопределятьс в дочерних классах.
            Например положение Слайдера задаётся в процентах в диапазоне 0-100,
            а Чекбокс получает True или False. (Либо on/off если угодно)
            """
        raise NotImplementedError

    def get_children_elements_list(self):
        try:
            children_list = self.find_elements(timeout=1)
        except (LookupError, RuntimeError):
            return None
        return children_list

    def get_parent_element(self):
        raise NotImplemented

    def is_present(self):
        try:
            self.find_element(timeout=1)
        except (LookupError, RuntimeError):
            return False
        return True
