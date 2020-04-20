from .base_element import BaseElement


class Button(BaseElement):
    def __init__(self, locator, locator_type=None, name=None):
        super(Button, self).__init__(locator, locator_type, name)

    def is_enabled(self):
        """ Проверить, активна ли кнопка """
        raise NotImplementedError
