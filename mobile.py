from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("https://suchen.mobile.de/fahrzeuge/search.html?dam=false&isSearchRequest=true&pageNumber=1&ref=srpNextPage&refId=979ff707-a93a-3364-db84-19faf433b73f&s=Car&sb=rel&vc=Car")

print(driver.title)
time.sleep(5)

btn_cookies = driver.find_element(By.CLASS_NAME, "mde-consent-accept-btn")
btn_cookies.click()

print(driver.current_url)

#driver.close()