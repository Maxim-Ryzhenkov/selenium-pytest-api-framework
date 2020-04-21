from .base_element import BaseElement


class DropDownList(BaseElement):
    def __init__(self, name, locator, loc_type):
        super(DropDownList, self).__init__(name, locator, loc_type)
