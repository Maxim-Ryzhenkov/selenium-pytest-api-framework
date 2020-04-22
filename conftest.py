
import pytest
import logging
from _pytest.runner import CallInfo

from framework.driver import Driver
from pages.ui_page import UiPage
from api.api import Api


@pytest.fixture(scope="session", autouse=True)
def browser():
    """ Запустить браузер перед запуском тестов
        и закрыть его по окончании тестов
        """
    driver = Driver().connect()
    driver.fullscreen_window()
    yield
    driver.quit()


@pytest.fixture(scope='class', autouse=False)
def finally_clear_subscriptions():
    pass
    yield
    #    Проверим, что за бардак там создаётся если приходят некорректные данные
    status_code, json_data = Api.get_subscriptions()
    assert status_code == 200
    print(str(json_data))
    logging.info(str(json_data))
    status_code, data = Api.clear_subscriptions()
    if status_code == 200:
        logging.info(f'База подписок ощищена! Удалено {data["removed"]} записей.')
    else:
        raise RuntimeError('Не удалось очистить базу подписок!')


@pytest.fixture(scope='class', autouse=False)
def suite_data():
    print("General suite setup")
    yield
    print("General suite teardown")


@pytest.fixture(scope='module', autouse=True)
def open_ui_page():
    ui_page = UiPage()
    ui_page.open()
    yield
    pass


def pytest_exception_interact(node, call: CallInfo, report):
    logger = logging.getLogger(__name__)
    if report.failed:
        logger.error(call.excinfo)
