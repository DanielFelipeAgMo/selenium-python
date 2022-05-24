from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

RUTA = "C:/firefox_webdriver/geckodriver.exe"

driver = webdriver.Firefox(executable_path=RUTA)
driver.get("")#Relacionando la pagina a realizar el scraping
time.sleep(5)

ejemplo = driver.find_element_by_xpath('')#Escogemos la forma en que deseamos acceder, en este caso, por xpath, puedes usar por id, class, etc.
ejemplo.click()#Hacemos click en el elemento

#Esperamos a que el elemento este disponible
WebDriverWait(driver, 5)\
    .until(EC.element_to_be_clickable((By.CSS_SELECTOR,'#name')))\
    .send_keys("Daniel Felipes")     

WebDriverWait(driver, 5)\
    .until(EC.element_to_be_clickable((By.CSS_SELECTOR,'#email')))\
    .send_keys("danielelqueteescrapea@correo.com")

WebDriverWait(driver, 5)\
    .until(EC.element_to_be_clickable((By.CSS_SELECTOR,'#phone')))\
    .send_keys("")  

WebDriverWait(driver, 5)\
    .until(EC.element_to_be_clickable((By.CSS_SELECTOR,'#message')))\
    .send_keys("Si yo quiero te robo tu página, jajajajajaja")  


WebDriverWait(driver, 3)\
    .until(EC.element_to_be_clickable((By.CSS_SELECTOR,'#submitButton')))\
    .click()

driver.quit()




