from config import Config
from framework.driver import Driver


class BasePage(object):
    """ Родительский класс для всех страниц тестируемого приложения
        Класс реализует поведение общее для всех страниц.
        Новые страницы должны наследоваться от BasePage
        """
    def __init__(self):
        self.driver = Driver().connect()
        self.base_url = Config.BASE_URL
        self.address = ''
        self.url = f"{self.base_url}/{self.address}"

    def open(self):
        """ Открыть в браузере базовую страницу приложения """
        return self.driver.get(self.url)

    def is_opened(self):
        pass
