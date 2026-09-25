import allure
import requests

BASE_URL = "https://stellarburgers.education-services.ru/api"


@allure.step("Создание пользователя и получение токена")
def create_user_and_get_token(api_client):
    from helpers.generators import generate_user
    user_data = generate_user()
    response = api_client.post("/auth/register", json=user_data)
    token = response.json().get("accessToken")
    return token, user_data


@allure.step("Создание заказа")
def create_order(token, ingredients):
    headers = {"Authorization": token}
    payload = {"ingredients": ingredients}
    response = requests.post(f"{BASE_URL}/orders", json=payload, headers=headers)
    return response


@allure.step("Удаление пользователя")
def delete_user(token):
    headers = {"Authorization": token}
    return requests.delete(f"{BASE_URL}/auth/user", headers=headers)