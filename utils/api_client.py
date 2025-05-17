import requests
import os
from bearer_token import get_bearer_token


class ApiClient:
    def __init__(self):
        self.base_url = os.getenv("API_BASE_URL")  # Чтение из переменных окружения
        if not self.base_url:
            raise ValueError("Не задан API_BASE_URL в переменных окружения!")

    def create_dealer(self, data):
        """Отправляет POST-запрос для создания дилера."""
        url = f"{self.base_url}/privat/dealers"
        response = requests.post(url, json=data)
        response.raise_for_status()  # Проверка на ошибки
        return response.json()  # Возвращает JSON (ожидаем {"id": число})

    def __init__(self, base_url, token=None):
        self.base_url = base_url
        self.headers = {"Authorization": f"Bearer {get_bearer_token}"} if get_bearer_token else {}

    def create_dealer(self, data):
        response = requests.post(..., headers=self.headers)