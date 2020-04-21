import time
import pytest
import logging
from _pytest.runner import CallInfo

from framework.driver import Driver


@pytest.fixture(scope="session", autouse=True)
def browser():
    """ Запустить браузер перед запуском тестов
        и закрыть его по окончании тестов
        """
    driver = Driver().connect()
    driver.fullscreen_window()
    yield
    driver.quit()


@pytest.fixture(scope='function', autouse=True)
def session_data():
    print("General module setup")
    yield
    print("General module teardown")


@pytest.fixture(scope='class', autouse=True)
def suite_data():
    print("General suite setup")
    yield
    print("General suite teardown")


@pytest.fixture(scope='function')
def case_data():
    print("General case setup")
    yield time.time()  # Может что-то передавать в кейс или не передавать
    print("General case teardown")


def pytest_exception_interact(node, call: CallInfo, report):
    logger = logging.getLogger(__name__)
    if report.failed:
        logger.error(call.excinfo)