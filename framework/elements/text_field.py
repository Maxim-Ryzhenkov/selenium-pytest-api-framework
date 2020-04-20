from .base_element import BaseElement


class TextField(BaseElement):
    def __init__(self, locator, locator_type=None, name=None):
        super(TextField, self).__init__(locator, locator_type, name)

    def set_value(self, value):
        """ Ввести текст в текстовое поле """
        self.click()
        self.find_element().send_keys(value)

    def get_value(self):
        """ Получить текст из текстового поля """
        return self.find_element().text
