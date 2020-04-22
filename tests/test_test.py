# -*- coding: utf-8 -*-

import pytest
import logging
from pages.ui_page import UiPage
from api.api import Api
from tests.test_data import utils

# Чтение тестовых данных из json
test_data_json = utils.get_test_data_from_json('test_data.json')
test_data = [(item['email'], item['name'], item['time'], item['comment'])
             for item in test_data_json['test_data']]

# Чтение тестовых данных из json
test_incorrect_data_json = utils.get_test_data_from_json('test_incorrect_data.json')
test_incorrect_data = [(item['email'], item['name'], item['time'], item['comment'])
                       for item in test_data_json['test_data']]


@pytest.mark.skip
@pytest.mark.smoke
@pytest.mark.parametrize('email, name, time, comment', test_data)
def test_email(email, name, time, comment):
    """ Параметризованный тест проверяет через UI создание
        новых подписок с разными параметрами.
        Тестовые данные лежат в папке tests/test_data/test_data.json
        """
    logging.info(f'UI тест: {comment}')
    ui_page = UiPage()
    ui_page.clear_subscriptions_list()
    ui_page.add_subscription(email, name, time)
    text = ui_page.subscribtions_table.get_table_text()[0]
    if text:
        assert text == [name, email, '']
    else:
        logging.error(f'Подписка не создана!')
        assert False


@pytest.mark.smoke
@pytest.mark.parametrize('email, name, time, comment', test_data)
def test_api_add_subscription(email, name, time, comment, finally_clear_subscriptions):
    """ Параметризованный позитивный тест проверяет через API создание
        новых подписок с разными параметрами.
        Тестовые данные лежат в папке tests/test_data/test_data.json
        """
    logging.info(f'API тест: {comment}')

    data = {'email': email,
            'name': name,
            'time': time,
            'comment': comment}

    #   Отправка POST запроса для создания новой подписки
    status_code, json_data = Api.add_subscription(data)
    #   Проверка что POST запрос отработал
    assert status_code == 200
    assert 'id' in json_data
    logging.info(str(json_data))


@pytest.mark.smoke
@pytest.mark.parametrize('email, name, time, comment', test_incorrect_data)
def test_api_add_subscription_negative(email, name, time, comment, finally_clear_subscriptions):
    """ Параметризованный негативный тест проверяет через API создание
        новых подписок с разными параметрами.
        Тестовые данные лежат в папке tests/test_data/test_incorrect_data.json
        """
    logging.info(f'API тест: {comment}')

    data = {'email': email,
            'name': name,
            'time': time,
            'comment': comment}

    #   Отправка POST запроса для создания новой подписки
    status_code, json_data = Api.add_subscription(data)
    #   Проверка что POST запрос отработал
    assert status_code == 200
    assert 'error' in json_data
    logging.info(str(json_data))

