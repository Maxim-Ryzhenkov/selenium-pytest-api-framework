from .base_element import BaseElement


class ScrollBar(BaseElement):
    def __init__(self, name, locator, loc_type):
        super(ScrollBar, self).__init__(name, locator, loc_type)
