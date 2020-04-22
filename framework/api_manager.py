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
        response = requests.post(url, auth=(user, password))
        # Куки тоже могут понадобится для работы ;)
        # ApiManager.cookie = {'SESSION_ID': result.cookies.get("SESSION_ID")}
        return response

    @staticmethod
    def get(url):
        """ Отправить GET запрос
        return: Метод вернёт объект,
            который имеет атрибуты в т.ч. status_code и text
            Подробнее в документации библиотеки requests
            """
        response = requests.get(url,
                                headers=ApiManager.headers)
        return response

    @staticmethod
    def post(url, body):
        """ Отправить POST запрос
        return: Метод вернёт объект,
                который имеет атрибуты в т.ч. status_code и text
                Подробнее в документации библиотеки requests
        """

        result = requests.post(url,
                               json=body,
                               headers=ApiManager.headers)
        return result

    @staticmethod
    def delete(url):
        """ Отправить DELETE запрос
        return: Метод вернёт объект,
            который имеет атрибуты в т.ч. status_code и text
            Подробнее в документации библиотеки requests
            """
        response = requests.delete(url,
                                   headers=ApiManager.headers)
        return response
