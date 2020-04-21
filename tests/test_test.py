import pytest
import time
from pages.ui_page import YandexSearchPage
from api.api import Api

WORDS = ['Ololo!', 'Max', 'World']


@pytest.mark.smoke
@pytest.mark.parametrize('word', WORDS)
def test_yandex_search(word):
    ym_page = YandexSearchPage()
    ym_page.open()
    print(f'Тестирую параметр {word}')
    ym_page.search_field.set_value(word)
    ym_page.search_button.click()
    elements_text = ym_page.navigation_bar.get_children_elements_text()
    assert "Картинки" and "Видео" in elements_text
