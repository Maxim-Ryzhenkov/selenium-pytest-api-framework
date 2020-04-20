from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from framework.driver import Driver


class BaseElement(object):
    def __init__(self, locator, locator_type=None, name=None):
        self.locator = locator
        self.locator_type = locator_type
        self.name = name
        self.driver = Driver().connect()

    def click(self):
        self.find_element().click()

    def find_element(self, timeout=5):
        return WebDriverWait(self.driver, timeout=timeout).until(
            EC.presence_of_element_located(self.locator),
            message=f"Can't find '{self.name}' element by locator '{self.locator}'")

    def find_elements(self, timeout=5):
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_all_elements_located(self.locator),
            message=f"Can't find elements by locator {self.locator}")

    def get_value(self):
        raise NotImplementedError

    def set_value(self, *args):
        raise NotImplementedError

    def get_children_elements_list(self):
        try:
            children_list = self.find_elements(timeout=1)
        except (LookupError, RuntimeError):
            return None
        return children_list

    def get_parent_element(self):
        raise NotImplemented

    def is_present(self):
        try:
            self.find_element(timeout=1)
        except (LookupError, RuntimeError):
            return False
        return True
