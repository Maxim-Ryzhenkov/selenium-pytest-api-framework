import requests

from config import Config
from framework.api_manager import ApiManager


class Api(object):
    """ Класс предоставляет набор методов для выполнения API запросов
        описанных в документации тестируемого проекта
        """

    @staticmethod
    def add_subscription(data, url='/subscriptions'):
        """ Добавить новую подписку
        :param data:   {"email": "...",
                        "name": "...",
                        "time": "...",
                        "comment": "..."}
        :param url: '/api/subscribe'
        :returns: response из которого можно извлечь int: status_code, int: id подписки
        """
        url = Config.BASE_URL + url
        response = ApiManager.post(url, body=data)
        status_code = response.status_code
        json_data = response.json()
        return status_code, json_data

    @staticmethod
    def clear_subscriptions(url='/subscriptions'):
        """ Очистить список подписок.
            Из объекта ответа извлекается код ответа и
            словарь {'removed': (int число удаленных записей)}
        :returns: response из которого можно извлечь int: status_code, int: removed
        """
        url = Config.BASE_URL + url
        response = ApiManager.delete(url)
        status_code = response.status_code
        json_data = response.json()
        return status_code, json_data

    @staticmethod
    def get_subscriptions(url='/subscriptions'):
        """ Получить список подписок в виде списка словарей
        :param url: /api/subscribers
        :return: объект результата запроса, в нем int:status_code и
                данные в фолрмате:
                 [{ "email": "...",
                    "name": "...",
                    "comment": "...",
                    "created_at": "...",
                    "expired_at": "..."
                    "id: ..."}, ... ]
        """
        url = Config.BASE_URL + url
        response = requests.get(url)
        status_code = response.status_code
        json_data = response.json()
        return status_code, json_data
