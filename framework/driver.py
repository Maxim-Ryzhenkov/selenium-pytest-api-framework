from selenium import webdriver

from config import Config


class Singleton(type):
    """ Синглтон гарантирует что из любой точки
        фреймворка мы можем подключиться к одному
        и тому же объекту драйвера """

    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class Driver(metaclass=Singleton):
    """ Когда мы нам нужно взаимодействие с драйвером,
        экземпляр класса может быть создан несколько раз,
        но фактически создается только один объект драйвера """

    connection = None

    def connect(self):
        """ Устанавливить соединение с драйвером
        :return: Экземпляр веб драйвера
        """
        if self.connection is None:
            if Config.DRIVER == 'Firefox':
                self.connection = webdriver.Firefox(executable_path=Config.DRIVER_PATH[Config.DRIVER])
            elif Config.DRIVER == 'Chrome':
                self.connection = webdriver.Chrome(executable_path=Config.DRIVER_PATH[Config.DRIVER])
        return self.connection

    def down(self):
        pass
