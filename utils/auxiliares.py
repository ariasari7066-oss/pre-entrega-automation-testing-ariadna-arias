from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.remote.webdriver import WebDriver

URL= "https://www.saucedemo.com/"
USER= "standard_user"
PASSWORD="secret_sauce"


def get_driver() -> WebDriver:

    options= Options()
    options.add_argument("--window-size=1920,1080")


    #Instalacion Driver
    service=Service(ChromeDriverManager().install())
    driver= webdriver.Chrome(service=service , options=options)
    
    time.sleep(5)
    return driver 



def login_saucedemo(driver):

    driver.get(URL)

    #Ingresar credenciales
    driver.find_element(By.NAME, "user-name").send_keys(USER) 
    driver.find_element(By.NAME, "password").send_keys(PASSWORD)
    time.sleep(5)
    
    tomar_screenshot(driver, "login_correcto.png")
   
    driver.find_element(By.ID, "login-button").click()
    
import os

def tomar_screenshot(driver, nombre_archivo):
    """
    Guarda una captura de pantalla en la carpeta 'reports'.
    """
    os.makedirs("reports", exist_ok=True)  # crea la carpeta si no existe
    ruta = os.path.join("reports", nombre_archivo)
    driver.save_screenshot(ruta)
    print(f"Screenshot guardada en: {ruta}")
   


    