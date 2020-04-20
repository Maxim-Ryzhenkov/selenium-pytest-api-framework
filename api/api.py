import requests
from framework.api_manager import ApiManager


class Api(object):
    """ Класс предоставляет набор методов для выполнения API запросов
        описанных в документации тестируемого проекта
        """

    def add_subscriber(self, data, url='/api/subscribe'):
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

    def remove_subscribers(self, url='/api/subscribers'):
        """ Очистить список подписок
        :return: объект результата запроса
        """
        result = ApiManager.delete(url)
        return result

    def get_subscribers(self, url='/api/subscribers'):
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
