from .base_element import BaseElement


class Slider(BaseElement):
    def __init__(self, name, locator, loc_type):
        super(Slider, self).__init__(name, locator, loc_type)
