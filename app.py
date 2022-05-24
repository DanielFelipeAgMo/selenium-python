from selenium import webdriver

sitioWeb = "https://dimayor.com.co/liga-betplay-dimayor/"

ruta  = "C:\chrome_webdriver\chromedriver.exe"

driver = webdriver.Chrome(ruta)
driver.get(sitioWeb)

clubesBoton = driver.find_element_by_css_selector("#menu-item-1414 > a")
clubesBoton.click()

clubesLiga = driver.find_element_by_css_selector("#menu-item-1427 > a")
clubesLiga.click()



btnDim = driver.find_element_by_css_selector()
btnDim.click()

variable = r('<h1/, r>')s?
resp = ['li','a']

