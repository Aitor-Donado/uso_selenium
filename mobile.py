from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("https://suchen.mobile.de/fahrzeuge/search.html?dam=false&isSearchRequest=true&pageNumber=2&ref=srpNextPage&refId=979ff707-a93a-3364-db84-19faf433b73f&s=Car&sb=rel&vc=Car")

print(driver.title)
time.sleep(0.8)
if driver.find_element(By.CLASS_NAME, "mde-consent-accept-btn"):
    btn_cookies = driver.find_element(By.CLASS_NAME, "mde-consent-accept-btn")
    btn_cookies.click()

anuncios = driver.find_elements(By.CLASS_NAME, "mN_WC")
len(anuncios)

enlaces = []
for i, anuncio in enumerate(anuncios):
    #anuncio = anuncios[3]
    #anuncio.screenshot("anuncio.png")
    anuncio.text
    path = ".//a/div[2]/section/div/div"
    enlace = anuncio.find_element(By.TAG_NAME, "a")
    enlaces.append(enlace.get_attribute("href"))
    try:
        detalles = anuncio.find_element(By.XPATH, path)
        print(detalles.text)
    except:
        print(f"Elemento {i} no encontrado")

enlace = enlaces[3]
driver.get(enlace)

print(driver.current_url)

#driver.close()