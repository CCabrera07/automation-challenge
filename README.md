<<<<<<< HEAD
# Challenge Automation - SauceDemo 
Proyecto de automatización desarrollado con **Python, Selenium y Pytest** para validar funcionalidades de la web SauceDemo y un servicio API de MercadoLibre.

## Tecnologías utilizadas
- Python
- Selenium WebDriver
- Pytest
- Pytest-HTML
- Requests
- Page Object Model (POM)

## Estructura del proyecto

crowdar_automation_challenge
│
├── api_clients
│ └── mercadolibre_client.py
│
├── data
│ └── test_data.py
│
├── pages
│ ├── login_page.py
│ └── inventory_page.py
│
├── reports
│
├── screenshots
│
├── tests
│ ├── test_login.py
│ ├── test_cart.py
│ └── api
│ └── test_mercadolibre_api.py
│
├── config.py
├── conftest.py
├── pytest.ini
├── README.md
└── requirements.txt

### Instalación

## 1. Clonar el repositorio
BASH
git clone <URL_DEL_REPOSITORIOS>

## 2. Crear entorno virtual
BASH
python -m venv .venv

## 3. Activar entorno virtual
    Windows
.venv\Scripts\activate

    Mac/Linux
source .venv/bin/activate

## 4. Instalar dependencias
pip install -r requirements.txt

## 5. Ejecutar en Chrome
pytest --browser=chrome

## 6. Ejecutar en Firefox
pytest --browser=firefox

## 7. Reportes
reports/report.html

## 8. Cobertura de pruebas
   **Login**
- Login exitoso
- Login con credenciales invalidas
   **Carrito de compras**
- Agregar producto al carrito
- Validar la cantidad del producto agregado (Caso fallido)
   **API**
- Validar departamentos en MercadoLibre

## 9. Notas
- Las pruebas se pueden correr en Chrome y Firefox
- Se implementó Page Object Model para mejorar la manutención del código.
- Se implementó fixture de Pytest para manejo del navegador y login reutilizable.
- Las capturas de pantallas se agregan al reporte y al mismo tiempo se encuentran en la carpeta screenshots con fecha y hora de la captura cuando falla una prueba.
=======
# automation-challenge
>>>>>>> 381c0c03d3904104f0ded7f23113084cd026f283
