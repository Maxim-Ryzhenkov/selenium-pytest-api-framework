from .base_element import BaseElement


class List(BaseElement):
    def __init__(self, name, locator, loc_type):
        super(List, self).__init__(name, locator, loc_type)

    def get_children_elements_text(self):
        """ Получить текст дочерних элементов в виде списка строк
        :return list of strings
        """
        children_list = self.get_children_elements_list()
        children_text = [child.text for child in children_list if len(child.text) > 0]
        return children_text
