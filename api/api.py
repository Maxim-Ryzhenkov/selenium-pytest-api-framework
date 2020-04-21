import requests
from framework.api_manager import ApiManager


class Api(object):
    """ Класс предоставляет набор методов для выполнения API запросов
        описанных в документации тестируемого проекта
        """
    @staticmethod
    def add_subscriber(data, url='/api/subscribe'):
        """ Добавить новую подписку
        :param data:   {"email": "...",
                        "name": "...",
                        "time": "...",
                        "comment": "..."}
        :param url: '/api/subscribe'
        :return: объект результата запроса
        """
        result = ApiManager.post(url, body=data)
        return result

    @staticmethod
    def remove_subscribers(url='/api/subscribers'):
        """ Очистить список подписок
        :return: объект результата запроса
        """
        result = ApiManager.delete(url)
        return result

    @staticmethod
    def get_subscribers(url='/api/subscribers'):
        """ Получить список подписок
        :param url: /api/subscribers
        :return: объект результата запроса, в нем данные  в фолрмате:
                 [{ "email": "...",
                    "name": "...",
                    "comment": "...",
                    "created_at": "...",
                    "expired_at": "..." }, ... ]
        """
        result = requests.get(url)
        return result
