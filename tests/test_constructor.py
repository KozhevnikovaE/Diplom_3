import allure
import pytest
from pages.main_page import MainPage
from locators.main_page_locators import MainPageLocators


@allure.epic("Основная функциональность")
@allure.feature("Конструктор")
class TestConstructor:

    @allure.story("Переход по клику на 'Конструктор'")
    def test_constructor_click(self, driver):
        main_page = MainPage(driver)
        main_page.click_order_feed()
        assert main_page.get_all_time_counter() is not None  

        main_page.click_constructor()
        assert main_page.find_element(MainPageLocators.CONSTRUCTOR_FIELD) is not None

    @allure.story("Переход по клику на 'Лента заказов'")
    def test_order_feed_click(self, driver):
        main_page = MainPage(driver)
        main_page.click_order_feed()
        assert main_page.get_all_time_counter() is not None
    
    @allure.story("Клик по ингредиенту — открывается модальное окно")
    def test_ingredient_modal(self, driver):
        main_page = MainPage(driver)
        main_page.click_ingredient()
        assert main_page.is_modal_open()

    @allure.story("Закрытие модального окна по крестику")
    def test_close_modal(self, driver):
        main_page = MainPage(driver)
        main_page.click_ingredient()
        main_page.close_modal()
        assert main_page.is_modal_closed()

    @allure.story("Счётчик ингредиента увеличивается при добавлении")
    def test_counter_increases(self, driver):
        main_page = MainPage(driver)
        initial = main_page.get_counter_value()
        main_page.drag_ingredient_to_constructor()
        new = main_page.get_counter_value()
        assert int(initial) < int(new)