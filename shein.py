from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("https://es.shein.com/")

print(driver.title)
time.sleep(5)
divs = driver.find_elements(By.TAG_NAME, "div")
len(divs)

for div in divs:
    if div.text == "Aceptar Todo":
        div.click()
        break

time.sleep(4)
svgs = driver.find_elements(By.TAG_NAME, "svg")
len(svgs)

for svg in svgs:
    if "btn-new" == svg.get_attribute("class"):
        svg.click()
        break


time.sleep(4)
clase_aspa = "sui-icons.icons-Close_12px"
aspas = driver.find_elements(By.CLASS_NAME, clase_aspa)
aspas[2].click()



print(driver.current_url)

#driver.close()