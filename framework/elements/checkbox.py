from .base_element import BaseElement


class CheckBox(BaseElement):
    def __init__(self, locator, locator_type=None, name=None):
        super(CheckBox, self).__init__(locator, locator_type, name)
