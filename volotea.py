from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://www.volotea.com/es/")

print(driver.title)


print(driver.current_url)

id_cookies_aceptar = "onetrust-accept-btn-handler"

boton_cookies = driver.find_element(By.ID, id_cookies_aceptar)
boton_cookies.click()


input("Pulsa Intro")

driver.close()