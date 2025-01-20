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

id_origen = "header-mobile__search origin"
casilla_origen = driver.find_element(By.ID, id_origen)
casilla_origen.screenshot("casilla.png")
casilla_origen.get_attribute("id")

casilla_origen.clear()
casilla_origen.send_keys("Bilbao")
casilla_origen.send_keys(Keys.ENTER)


clase_ciudad = "v7-card__title.v7-sub-title.v7-sub-title--md.v7-u-bold"
destinos = driver.find_elements(By.CLASS_NAME, clase_ciudad)

for destino in destinos:
    # print(destino.text)
    if destino.text == "Gran Canaria":
        destino.click()

driver.find_element(By.CLASS_NAME, "v7-input-text").click()

def extrae_dia(dia, mes: str):
    fila_datos = {}
    if dia.find_elements(By.CLASS_NAME, "v7-cal__amount"):
        fila_datos["mes"] = mes
        fila_datos["numero_dia"] = dia.find_element(By.CLASS_NAME, "v7-cal__number").text
        fila_datos["precio"] = dia.find_element(By.CLASS_NAME, "v7-cal__amount").text
        return fila_datos


tag_mes = "sf-calendar-month"
meses = driver.find_elements(By.TAG_NAME, tag_mes)
len(meses)

mes = meses[1]
def extrae_mes(mes):
    tag_dia = "sf-calendar-day"
    dias = mes.find_elements(By.TAG_NAME, tag_dia)
    for dia in dias:
        print(extrae_dia(dia, "Febrero"))

extrae_mes(mes)


driver.close()