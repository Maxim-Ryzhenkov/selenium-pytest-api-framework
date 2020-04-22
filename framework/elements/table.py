from selenium.webdriver.common.by import By

from .base_element import BaseElement


class Table(BaseElement):
    def __init__(self, name, locator, loc_type):
        super(Table, self).__init__(name, locator, loc_type)

    def get_table_text(self):
        """ Получить текст из таблица в виде списка списков
            где строки - это ряды таблицы,
            а вложенные списки - текст ячеек
        :return: [[td1, td2, td3],
                  [td1, td2, td3], ...]
        """
        table_data = list()
        self.find_element()
        rows = self.obj.find_elements(By.TAG_NAME, "tr")  # get all of the rows in the table
        if len(rows) < 2:
            return None
        for row in rows[:-1]:
            # TODO: Весь метод заточен под одну конкретную таблицу
            # TODO: у которой последний ряд содержит невалидные данные или
            # TODO: нет нужных тегов и попытка его распарсить вызовет падение.
            # TODO: Если проект увеличится то метод следует доработать
            first_cell = row.find_element(By.TAG_NAME, "th")
            cells = row.find_elements(By.TAG_NAME, "td")
            row_data = [col.text for col in cells]
            row_data.insert(0, first_cell.text)
            table_data.append(row_data)
        return table_data

    def parse(self):
        table = self.find_element()
        rows = table.find_elements(By.TAG_NAME, "tr")  # get all of the rows in the table
        for row in rows:
            # Get the columns (all the column 2)
            col = row.find_elements(By.TAG_NAME, "td")  # note: index start from 0, 1 is col 2

    def get_children_elements_text(self):
        """ Получить текст дочерних элементов в виде списка строк
        :return list of strings
        """
        children_list = self.get_children_elements_list()
        children_text = [child.text for child in children_list if len(child.text) > 0]
        return children_text
