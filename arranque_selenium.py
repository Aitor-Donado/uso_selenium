from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://www.python.org")

print(driver.title)

contenido = driver.find_element(By.ID, "content")
contenido.text

botones = contenido.find_elements(By.CLASS_NAME, "button")
len(botones)

for boton in botones:
    if boton.text.__str__() == 'PyPI Project Page Feedback':
        boton.click()
        break


print(driver.current_url)

input("Pulsa una tecla: ")

driver.close()