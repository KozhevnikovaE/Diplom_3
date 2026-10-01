
import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    @allure.step("Поиск элемента: {locator}")
    def find_element(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    @allure.step("Клик по элементу: {locator}")
    def click_element(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    @allure.step("Получение текста из элемента: {locator}")
    def get_text(self, locator):
        return self.find_element(locator).text

    @allure.step("Перетащить элемент: {source_locator} в цель: {target_locator}")
    def drag_and_drop(self, source_locator, target_locator):
        self.wait.until(EC.presence_of_element_located(source_locator))
        self.wait.until(EC.presence_of_element_located(target_locator))

        element_from = self.driver.find_element(*source_locator)
        element_to = self.driver.find_element(*target_locator)

        self.driver.execute_script("""
            var source = arguments[0];
            var target = arguments[1];

            var evt = document.createEvent("DragEvent");
            evt.initMouseEvent("dragstart", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
            source.dispatchEvent(evt);

            evt = document.createEvent("DragEvent");
            evt.initMouseEvent("dragenter", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
            target.dispatchEvent(evt);

            evt = document.createEvent("DragEvent");
            evt.initMouseEvent("dragover", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
            target.dispatchEvent(evt);

            evt = document.createEvent("DragEvent");
            evt.initMouseEvent("drop", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
            target.dispatchEvent(evt);

            evt = document.createEvent("DragEvent");
            evt.initMouseEvent("dragend", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
            source.dispatchEvent(evt);
        """, element_from, element_to)