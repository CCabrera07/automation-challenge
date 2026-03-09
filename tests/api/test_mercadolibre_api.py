from api_clients.mercadolibre_client import MercadoLibreClient
import pytest

@pytest.mark.api
def test_get_mercadolibre_departments():
    client = MercadoLibreClient()

    response = client.get_departments()

    assert response.status_code == 200, f"Esperado status 200, recibido {response.status_code}"

    data = response.json()

    assert "departments" in data
    assert len(data["departments"]) > 0