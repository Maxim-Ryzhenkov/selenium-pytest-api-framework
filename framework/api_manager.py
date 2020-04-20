import requests


class ApiManager:
    """ Класс предоставляет методы для отправки основных http запросов,
        на основе библиотеки requests
        """

    headers = {'Content-Type': 'application/json'}
    cookie = ""

    @staticmethod
    def auth(url, user, password):
        """ В тестовом проекте аутентификация не требуется,
            поэтому это просто заготовка на будущее """
        result = requests.post(url, auth=(user, password))
        # Куки тоже могут понадобится для работы ;)
        # ApiManager.cookie = {'SESSION_ID': result.cookies.get("SESSION_ID")}
        return result

    @staticmethod
    def get(url):
        """ Отправить GET запрос """
        result = requests.get(url,
                              headers=ApiManager.headers)
        return result

    @staticmethod
    def post(url, body):
        """ Отправить POST запрос """
        result = requests.post(url,
                               json=body,
                               headers=ApiManager.headers)
        return result

    @staticmethod
    def delete(url):
        """ Отправить DELETE запрос """
        result = requests.delete(url,
                                 headers=ApiManager.headers)
        return result
