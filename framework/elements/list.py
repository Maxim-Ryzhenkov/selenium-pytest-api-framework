from .base_element import BaseElement


class List(BaseElement):
    def __init__(self, locator, locator_type=None, name=None):
        super(List, self).__init__(locator, locator_type, name)

    def get_children_elements_text(self):
        """ Получить текст дочерних элементов в виде списка строк
        :return list of strings
        """
        children_list = self.get_children_elements_list()
        children_text = [child.text for child in children_list if len(child.text) > 0]
        return children_text
