from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
driver = webdriver.Chrome()

driver.get("https://www2.agenciatributaria.gob.es/static_files/common/internet/dep/taiif/subastaInmuebles/index.html#/index/?tipoBien=I")

print(driver.title)
print(driver.current_url)

clase_provincia = "js-index-provincia.cursor-pointer"
lista_provincias = driver.find_elements(By.CLASS_NAME, clase_provincia)

for provincia in lista_provincias:
    if "León" in provincia.text:
        provincia.click()

driver.find_elements(By.CLASS_NAME, "card-body")[0].click()

driver.close()