from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
driver = webdriver.Chrome()

driver.get("https://www.volotea.com/es/")

print(driver.title)
print(driver.current_url)

id_cookies_aceptar = "onetrust-accept-btn-handler"
boton_cookies = driver.find_element(By.ID, id_cookies_aceptar)
boton_cookies.click()
time.sleep(1)

id_origen = "input-text_sf-origin"
casilla_origen = driver.find_element(By.ID, id_origen)
casilla_origen.click()

clase_origen = "v7-menu-secondary__search-input.ng-untouched.ng-pristine.ng-valid.ng-star-inserted"
casilla_origen = driver.find_element(By.CLASS_NAME, clase_origen)
casilla_origen.get_attribute("id")

casilla_origen.clear()

casilla_origen.send_keys("Bilbao")

driver.find_elements(By.CLASS_NAME, "v7-card__box")[0].click()

clase_ciudad = "v7-card__title.v7-sub-title.v7-sub-title--md.v7-u-bold"
destinos = driver.find_elements(By.CLASS_NAME, clase_ciudad)

for destino in destinos:
    if destino.text == "Gran Canaria":
        destino.click()

driver.close()