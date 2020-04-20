from .base_element import BaseElement


class ScrollBar(BaseElement):
    def __init__(self, locator, locator_type=None, name=None):
        super(ScrollBar, self).__init__(locator, locator_type, name)
