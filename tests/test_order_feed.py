
import allure
import pytest
from pages.main_page import MainPage
from helpers.api_helpers import create_order


@allure.epic("Лента заказов")
@allure.feature("Счётчики")
class TestOrderFeed:

    @allure.story("Счётчик 'Выполнено за всё время' увеличивается")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_all_time_counter_increases(self, driver, api_client, auth_user):
        token, user_data = auth_user

        with allure.step("Переход на ленту заказов"):
            main_page = MainPage(driver)
            main_page.click_order_feed()

        with allure.step("Получение текущего значения счётчика 'Выполнено за всё время'"):
            old_count = int(main_page.get_all_time_counter())

        with allure.step("Создание заказа с ингредиентом"):
            ingredients = ["61c0c5a71d1f82001bdaaa6d"]
            create_order(token, ingredients)

        with allure.step("Получение нового значения счётчика 'Выполнено за всё время'"):
            new_count = int(main_page.get_all_time_counter())

        with allure.step("Проверка, что счётчик увеличился"):
            assert new_count > old_count, \
                f"Счётчик не увеличился: было {old_count}, стало {new_count}"

    @allure.story("Счётчик 'Выполнено за сегодня' увеличивается")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_get_today_counter_increases(self, driver, api_client, auth_user):
        token, user_data = auth_user
    
        with allure.step("Переход на ленту заказов"):
            main_page = MainPage(driver)
            main_page.click_order_feed()
    
        with allure.step("Получение текущего значения счётчика 'Выполнено за сегодня'"):
            old_count = int(main_page.get_today_counter())
    
        with allure.step("Создание заказа с ингредиентом"):
            ingredients = ["61c0c5a71d1f82001bdaaa6d"]
            create_order(token, ingredients)
    
        with allure.step("Получение нового значения счётчика 'Выполнено за сегодня'"):
            new_count = int(main_page.get_today_counter())
    
        with allure.step("Проверка, что счётчик увеличился"):
            assert new_count > old_count, \
                f"Счётчик не увеличился: было {old_count}, стало {new_count}"

    @allure.story("Номер заказа появляется в разделе 'В работе'")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_order_number_in_progress(self, driver, api_client, auth_user):
        token, user_data = auth_user

        with allure.step("Переход на ленту заказов"):
            main_page = MainPage(driver)
            main_page.click_order_feed()

        with allure.step("Создание заказа через API"):
            ingredients = ["61c0c5a71d1f82001bdaaa6d"]
            response = create_order(token, ingredients)
            order_number = response.json()["order"]["number"]

        with allure.step("Ожидание обновления ленты"):
            driver.refresh()

        with allure.step("Поиск номера заказа в разделе 'В работе'"):
            order_in_progress = main_page.find_order_in_progress(order_number)

        with allure.step("Проверка, что номер заказа отображается"):
            assert order_in_progress is not None, f"Заказ {order_number} не найден в разделе 'В работе'"