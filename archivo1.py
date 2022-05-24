# Librerías
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time


# Opciones de navegación
options =  webdriver.FirefoxOptions()
options.add_argument('--start-maximized')
options.add_argument('--disable-extensions')
# Esta es la ruta del driver del navegador, sea chrome o firefox
driver_path = 'C:/firefox_webdriver/geckodriver.exe'

driver = webdriver.Firefox(executable_path=driver_path, options=options)

time.sleep(5)



# Inicializamos el navegador
# Relacionando la pagina a realizar el scraping
driver.get("")

#Escogemos la forma en que deseamos acceder, en este caso, por xpath, puedes usar por id, class, etc.
WebDriverWait(driver, 5)\
    .until(EC.element_to_be_clickable((By.XPATH('/html/body/nav/div/div/ul/li[5]/a'))))\
    .click()

