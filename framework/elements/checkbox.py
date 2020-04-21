from .base_element import BaseElement


class CheckBox(BaseElement):
    def __init__(self, name, locator, loc_type):
        super(CheckBox, self).__init__(name, locator, loc_type)
