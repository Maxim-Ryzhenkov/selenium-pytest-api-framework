from .base_element import BaseElement


class Button(BaseElement):
    def __init__(self, name, locator, loc_type):
        super(Button, self).__init__(name, locator, loc_type)

    def is_enabled(self):
        """ Проверить, активна ли кнопка """
        raise NotImplementedError
