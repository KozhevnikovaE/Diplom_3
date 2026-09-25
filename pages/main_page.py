import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators


class MainPage(BasePage):

    @allure.step("Клик по кнопке 'Конструктор'")
    def click_constructor(self):
        self.click_element(MainPageLocators.CONSTRUCTOR_BUTTON)

    @allure.step("Клик по кнопке 'Лента заказов'")
    def click_order_feed(self):
        try:
            self.click_element(MainPageLocators.CLOSE_MODAL_BUTTON)
        except:
            pass
        self.click_element(MainPageLocators.ORDER_FEED_BUTTON)

    @allure.step("Клик по первому ингредиенту")
    def click_ingredient(self):
        self.click_element(MainPageLocators.INGREDIENT)


    @allure.step("Проверить, что модальное окно открыто")
    def is_modal_open(self):
        return self.find_element(MainPageLocators.INGREDIENT_MODAL).is_displayed()

    @allure.step("Получить значение счётчика ингредиента")
    def get_counter_value(self):
        return self.get_text(MainPageLocators.COUNTER)

    @allure.step("Добавить ингредиент в заказ (двойной клик)")
    def add_ingredient_to_order(self):
        self.double_click_element(MainPageLocators.INGREDIENT)

    @allure.step("Проверить, что вкладка 'Лента заказов' активна")
    def is_order_feed_active(self):
        return self.find_element(MainPageLocators.ORDER_FEED_ACTIVE).is_displayed()

    @allure.step("Переместить ингредиент в конструктор")
    def drag_ingredient_to_constructor(self):
        self.drag_and_drop(MainPageLocators.INGREDIENT, MainPageLocators.CONSTRUCTOR_FIELD)

    @allure.step("Закрытие модального окна (крестик)")
    def close_modal(self):
        self.click_element(MainPageLocators.CLOSE_MODAL_BUTTON)
        self.wait.until(EC.invisibility_of_element_located(MainPageLocators.INGREDIENT_MODAL))

    @allure.step("Проверить, что модальное окно закрыто")
    def is_modal_closed(self):
        try:
            return not self.find_element(MainPageLocators.INGREDIENT_MODAL).is_displayed()
        except:
            return True

    @allure.step("Получить значение счётчика 'Выполнено за всё время'")
    def get_all_time_counter(self):
        return self.get_text(MainPageLocators.ORDER_FEED_ALL_TIME_COUNTER)

    @allure.step("Получить значение счётчика 'Выполнено за сегодня'")
    def get_today_counter(self):
        return self.get_text(MainPageLocators.ORDER_FEED_TODAY_COUNTER)

    @allure.step("Найти номер заказа в разделе 'В работе'")
    def find_order_in_progress(self, order_number):
        locator = (By.XPATH, f"//p[text()='{order_number}']")
        try:
            return self.find_element(locator)
        except:
            return None