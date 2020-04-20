import os


class Config(object):
    ROOT_DIR = os.path.dirname(__file__)

    BASE_URL = 'https://ya.ru'

    ALLOWED_BROWSERS = [
        'Firefox',
        'Chrome',
    ]

    DRIVER_PATH = {
        'Chrome': os.path.join(ROOT_DIR, 'chromedriver'),
        'Firefox': os.path.join(ROOT_DIR, 'geckodriver'),
    }

    DRIVER = 'Firefox'
