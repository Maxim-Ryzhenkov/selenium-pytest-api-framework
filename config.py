import os


class Config(object):
    ROOT_DIR = os.path.dirname(__file__)
    TEST_DATA_DIR = os.path.join(ROOT_DIR, 'tests', 'test_data')

    BASE_URL = 'http://localhost:4000'

    ALLOWED_BROWSERS = [
        'Firefox',
        'Chrome',
    ]

    DRIVER_PATH = {
        'Chrome': os.path.join(ROOT_DIR, 'drivers', 'chromedriver'),
        'Firefox': os.path.join(ROOT_DIR, 'drivers', 'geckodriver'),
    }

    DRIVER = 'Chrome'
