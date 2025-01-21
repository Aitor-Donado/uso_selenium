from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
driver = webdriver.Chrome()

driver.get("https://www2.agenciatributaria.gob.es/static_files/common/internet/dep/taiif/subastaInmuebles/index.html#/index/?tipoBien=I")

print(driver.title)

clase_provincia = "js-index-provincia.cursor-pointer"
lista_provincias = driver.find_elements(By.CLASS_NAME, clase_provincia)

for provincia in lista_provincias:
    if "León" in provincia.text:
        provincia.click()
        break

anuncios = driver.find_elements(By.CLASS_NAME, "js-lnk-detalle-modal")
enlaces = []
for anuncio in anuncios:
    print(anuncio.text)
    identificador = anuncio.get_attribute("js-params")
    enlace = f"https://www2.agenciatributaria.gob.es/static_files/common/internet/dep/taiif/subastaInmuebles/index.html#/inmueble/{identificador}"
    enlaces.append(enlace)


lista_datos = []
for enlace in enlaces:
    dato = {}
    driver.get(enlace)
    time.sleep(2)
    listado = driver.find_element(By.CLASS_NAME, "list-unstyled.col-12.col-md-12.p-0")
    items_lista = listado.find_elements(By.TAG_NAME, "li")
    for item in items_lista:
        print(item.text)
        key = item.find_element(By.TAG_NAME, "span").text
        if "foto" not in key:
            dato[key] = item.text.replace(key,"").replace("\n","")
    lista_datos.append(dato)
    
import pandas as pd
datos_leon = pd.DataFrame(lista_datos)
datos_leon.to_csv("datos_leon.csv")

print(enlaces)
time.sleep(1)
driver.find_elements(By.CLASS_NAME, "card-body")[0].click()
print(driver.current_url)

driver.close()