from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time

URL= "https://www.saucedemo.com/"
USER= "standard_user"
PASSWORD="secret_sauce"

def get_driver():

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
    #tomar capture


    driver.find_element(By.ID, "login-button").click()


    






    