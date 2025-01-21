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

# Hemos intentado acceder a la casilla con id
# Pero el elemento no es clicable
# id_origen = "input-text_sf-origin"
# casilla_origen = driver.find_element(By.ID, id_origen)

clase_origen = "v7-sf__group-item--origin"
casilla_origen = driver.find_elements(By.CLASS_NAME, clase_origen)[0]
casilla_origen.click()
time.sleep(1)

id_origen = "header-mobile__search origin"
casilla_origen = driver.find_element(By.ID, id_origen)
casilla_origen.screenshot("casilla.png")
casilla_origen.get_attribute("id")

casilla_origen.clear()
casilla_origen.send_keys("Bilbao")
time.sleep(1)
casilla_origen.send_keys(Keys.ENTER)

time.sleep(1)
clase_ciudad = "v7-card__title.v7-sub-title.v7-sub-title--md.v7-u-bold"
destinos = driver.find_elements(By.CLASS_NAME, clase_ciudad)

destinos[0].screenshot("destino.png")
for destino in destinos:
    print(destino.text)
    if destino.text == "Gran Canaria":
        destino.click()
        break

time.sleep(1)
driver.find_element(By.CLASS_NAME, "v7-input-text").click()
time.sleep(0.5)
casillas_meses = driver.find_elements(By.CLASS_NAME, "v7-input-select__item")

nombres_meses = [casilla_mes.text for casilla_mes in casillas_meses]

def extrae_dia(dia, mes: str):
    fila_datos = {}
    if dia.find_elements(By.CLASS_NAME, "v7-cal__amount"):
        fila_datos["mes"] = mes
        fila_datos["numero_dia"] = dia.find_element(By.CLASS_NAME, "v7-cal__number").text
        fila_datos["precio"] = dia.find_element(By.CLASS_NAME, "v7-cal__amount").text
        lista_datos.append(fila_datos)
        print(fila_datos)

def extrae_mes(mes, nombre_mes):
    tag_dia = "sf-calendar-day"
    dias = mes.find_elements(By.TAG_NAME, tag_dia)
    for dia in dias:
        extrae_dia(dia, nombre_mes)

tag_mes = "sf-calendar-month"
meses = driver.find_elements(By.TAG_NAME, tag_mes)

lista_datos = []
for mes, nombre_mes in zip(meses, nombres_meses):
    extrae_mes(mes, nombre_mes)

import pandas as pd
datos = pd.DataFrame(lista_datos)

datos.to_csv("Bilbao-GranCanaria.csv")

driver.close()