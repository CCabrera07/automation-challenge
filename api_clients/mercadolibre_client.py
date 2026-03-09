import requests


class MercadoLibreClient:

    BASE_URL = "https://www.mercadolibre.com.ar"

    def get_departments(self):
        url = f"{self.BASE_URL}/menu/departments"

        headers = {
            "User-Agent": "Mozilla/5.0"
        }

        return requests.get(url, headers=headers)