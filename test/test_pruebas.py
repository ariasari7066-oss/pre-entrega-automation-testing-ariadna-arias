import pytest
from selenium.webdriver.common.by import By
import sys
import os

# Agrega la carpeta padre al path para poder importar módulos desde utils
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))

# Importamos funciones helper: login_saucedemo para loguearse y get_driver para inicializar Selenium
from utils.auxiliares import login_saucedemo, get_driver

# -------------------------------
# Fixture de pytest para inicializar el navegador
# -------------------------------
@pytest.fixture
def driver():
    # Creamos el driver usando la función get_driver()
    driver = get_driver()
    # yield devuelve el driver al test que lo llame
    yield driver
    # Al finalizar el test, cerramos el navegador para liberar recursos
    driver.quit()

# -------------------------------
# Test 1: Login correcto
# -------------------------------
def test_login(driver):
    # Llamamos a la función de login
    login_saucedemo(driver)
    
    # Verificamos que la URL después del login sea la correcta
    assert "/inventory.html" in driver.current_url
    
    # Buscamos el título de la página de productos
    titulo  = driver.find_element(By.CSS_SELECTOR, 'div.header_secondary_container .title').text
    
    # Verificamos que el título sea 'Products'
    assert titulo == 'Products'

# -------------------------------
# Test 2: Verificación del catálogo de productos
# -------------------------------
def test_catalogo(driver):
    # Logueamos primero
    login_saucedemo(driver)
    
    # Buscamos todos los productos por su clase CSS
    products = driver.find_elements(By.CLASS_NAME, 'inventory_item')
    
    # Verificamos que haya al menos un producto en el catálogo
    assert len(products) > 0

# -------------------------------
# Test 3: Agregar producto al carrito
# -------------------------------
def test_carrito(driver):
    # Logueamos primero
    login_saucedemo(driver)
    
    # Obtenemos la lista de productos
    products = driver.find_elements(By.CLASS_NAME, 'inventory_item')
    
    # Verificamos que exista al menos un producto
    assert len(products) > 0
    
    # Hacemos clic en el botón "Agregar al carrito" del primer producto
    products[0].find_element(By.TAG_NAME, 'button').click()
    
    # Obtenemos el número de productos en el carrito
    badge = driver.find_element(By.CLASS_NAME, 'shopping_cart_badge').text
    
    # Verificamos que el carrito tenga un producto
    assert badge == "1"
