from pages.ui_page import YandexSearchPage
from api.api import Api


class TestApi:

    def test_yandex_search(self):
        ym_page = YandexSearchPage()
        ym_page.open()
        ym_page.search_field.set_value("Hello")
        ym_page.search_button.click()
        elements_text = ym_page.navigation_bar.get_children_elements_text()
        assert "Картинки" and "Видео" in elements_text

    def test_add_subscription(self):
        subscribe_data = {"email": "ryzhenkov.m@gmail.com",
                          "name": "Максим",
                          "time": "1d",
                          "comment": "Первая подписка"}

        reference_subscriptions_list = " ".join(subscribe_data.values())

        result = Api().add_subscriber(data=subscribe_data)
        assert result.status_code == 200

        ui_page = UiPage()
        ui_page.open()
        subscriptions_list = ui_page.get_subscriptions_list()
        assert subscriptions_list == reference_subscriptions_list

    def test_clear_subscriptions(self):
        pass

    def test_get_subscriptions(self):
        pass
