def test_create_dealer(api_client, dealer_data):
    """Тест создания дилера через API."""
    # 1. Отправка запроса
    response = api_client.create_dealer(dealer_data)

    # 2. Проверки
    assert "id" in response, "Ответ должен содержать 'id'"
    assert isinstance(response["id"], int), "'id' должен быть числом"

    # 3. Дополнительная проверка (опционально)
    assert response["id"] > 0, "ID должен быть положительным"