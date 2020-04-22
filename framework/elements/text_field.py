import time
from .base_element import BaseElement


class TextField(BaseElement):
    def __init__(self, name: str, locator: str, loc_type: str):
        super(TextField, self).__init__(name, locator, loc_type)

    def set_value(self, value):
        """ Ввести текст в текстовое поле """
        self.click()
        self.obj.clear()
        self.obj.send_keys(value)

    def get_value(self):
        """ Получить текст из текстового поля """
        self.find_element()
        return self.obj.text
