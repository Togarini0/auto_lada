import pytest
from data.get_data import GET_ENDPOINTS  # Данные для GET

@pytest.mark.parametrize("endpoint, params, expected_status", GET_ENDPOINTS)
def test_get_methods(api_client, endpoint, params, expected_status):
    response = api_client.get(endpoint, params=params)
    assert response.status_code == expected_status
    assert "data" in response.json()  # Пример проверки структуры ответа