from .base_element import BaseElement


class Label(BaseElement):
    def __init__(self, name, locator, loc_type):
        super(Label, self).__init__(name, locator, loc_type)
