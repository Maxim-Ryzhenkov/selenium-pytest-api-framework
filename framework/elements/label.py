from .base_element import BaseElement


class Label(BaseElement):
    def __init__(self, locator, locator_type=None, name=None):
        super(Label, self).__init__(locator, locator_type, name)
