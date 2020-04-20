from .base_element import BaseElement


class Slider(BaseElement):
    def __init__(self, locator, locator_type=None, name=None):
        super(Slider, self).__init__(locator, locator_type, name)
