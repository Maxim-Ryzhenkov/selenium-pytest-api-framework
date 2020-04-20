from .base_element import BaseElement


class DropDownList(BaseElement):
    def __init__(self, locator, locator_type=None, name=None):
        super(DropDownList, self).__init__(locator, locator_type, name)
