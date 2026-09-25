import pytest
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.options import Options as FirefoxOptions  
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from locators.main_page_locators import MainPageLocators

@pytest.fixture
def api_client():
    class APIClient:
        def post(self, endpoint, json=None):
            url = f"https://stellarburgers.education-services.ru/api{endpoint}"
            return requests.post(url, json=json)
    return APIClient()

@pytest.fixture(params=["chrome", "firefox"])
def driver(request):
    browser = request.param

    if browser == "chrome":
        service = ChromeService(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)

    elif browser == "firefox":
        options = FirefoxOptions()
        options.binary_location = r"C:\Users\ivank\AppData\Local\Mozilla Firefox\firefox.exe"
        
        service = FirefoxService(GeckoDriverManager().install())
        driver = webdriver.Firefox(service=service, options=options)
       

        service = FirefoxService(GeckoDriverManager().install())
        driver = webdriver.Firefox(service=service, options=options)

    else:
        raise ValueError(f"Unsupported browser: {browser}")

    driver.get("https://stellarburgers.education-services.ru")
    driver.maximize_window()

    try:
        close_button = driver.find_element(*MainPageLocators.CLOSE_MODAL_BUTTON)
        close_button.click()
    except Exception:
        pass

    yield driver
    driver.quit()

@pytest.fixture
def auth_user(api_client):
    from helpers.api_helpers import create_user_and_get_token, delete_user
    token, user_data = create_user_and_get_token(api_client)
    yield token, user_data
    delete_user(token)
