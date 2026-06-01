#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 20 11:46:45 2024

@author: laptop
"""

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
opciones = Options()
opciones.add_argument("--window-size=1080,1080")  # Establecer tamaño de ventana


# En el caso de ejecutarse en windows no es necesario el parámetro service
# ya que la ubicación del chromedriver es resuelta por selenium
from selenium.webdriver.chrome.service import Service
ubicacion_chromedriver = '/home/laptop/Proyectos Python/Selenium/chromedriver-linux64/chromedriver'
servicio = Service(ubicacion_chromedriver)
driver = webdriver.Chrome(options=opciones)


#############################
# Usar variables de entorno #
#############################
# instalar 
# pip install python-dotenv
# importar
from dotenv import load_dotenv
import os
# Cargar las variables del archivo .env
load_dotenv()
# Acceder a las variables
PASS_ECOBOLSA = os.getenv("pass_ecobolsa")


# Visitar una página web (puedes cambiar la URL según tu necesidad)
driver.get("https://www.ecobolsa.com/mercado-continuo.html")
driver.implicitly_wait(3)
time.sleep(2)

# Aceptar las cookies
from selenium.webdriver.common.by import By
driver.find_element(By.CLASS_NAME, "css-47sehv").click()

time.sleep(2)

########################
# Carga de las cookies #
########################
# Podremos evitar el proceso de logueo con unas cookies guardadas 
# de una sesión anterior
import pickle

# Comprobar si existe el archivo cookies.pckl

if os.path.exists("cookies.pckl"):
    print("El archivo cookies.pckl existe. Cargando...")
    driver.get("https://www.ecobolsa.com")  # 1. Ir al dominio base primero
    
    with open('cookies.pckl', 'rb') as cookies_file:
        cookies_guardadas = pickle.load(cookies_file)

    for cookie in cookies_guardadas:
        try:
            # 2. Limpiar atributos problemáticos
            cookie_clean = {
                'name': cookie['name'],
                'value': cookie['value'],
                'domain': cookie.get('domain', '.ecobolsa.com'),
                'path': cookie.get('path', '/'),
            }
            # Añadir expiry solo si existe y es válido
            if 'expiry' in cookie and cookie['expiry']:
                cookie_clean['expiry'] = cookie['expiry']
            # Opcional: añadir secure si existe
            if 'secure' in cookie:
                cookie_clean['secure'] = cookie['secure']
                
            driver.add_cookie(cookie_clean)
            print(f"✓ Cookie añadida: {cookie['name']}")
        except Exception as e:
            print(f"✗ Error al añadir cookie {cookie.get('name')}: {e}")
    
    # 3. Navegar a la página objetivo (solo una vez)
    driver.get("https://www.ecobolsa.com/mercado-continuo.html")
    time.sleep(3)
    print("Cookies cargadas y página recargada.")
else:
    print("El archivo cookies.pckl no existe.")
    ##########
    # Log in #
    ##########

    input("Pulsa intro para continuar: ")
    # Abrir el formulario
    enlaces = driver.find_elements(By.TAG_NAME, "a")
    for enlace in enlaces:
        if enlace.get_attribute("data-title") == "Acceso a tiempo real":
            enlace.click()
            # Escribir el email
            email = driver.find_element(By.ID, "userNameTextBox")
            email.send_keys("Aitor_Don@hotmail.com")

            # Escribir la contraseña
            passw = driver.find_element(By.ID, "password_login")
            passw.send_keys(PASS_ECOBOLSA)

            # Introducir los datos
            driver.find_element(By.ID, "SubmitLogin").click()
            time.sleep(2)
            driver.get("https://www.ecobolsa.com/mercado-continuo.html")

            ###########################
            # Guardado de las cookies #
            ###########################
            cookies = driver.get_cookies()

            # Puedo guardar las cookies en un archivo del ordenador
            # para volver a usarlas
            import pickle
            with open('cookies.pckl', 'wb') as cookies_file:
                pickle.dump(cookies, cookies_file)
            break



#######################################
# Lectura de los datos a un Dataframe #
#######################################
clase_tabla = "mercado-continuo"

tabla = driver.find_element(By.ID, clase_tabla)

# print(tabla.get_attribute("outerHTML"))

import pandas as pd
from io import StringIO
# Esta acción requiere pip install lxml
# columnas = pd.read_html(tabla.get_attribute("outerHTML"))[0]
"""
with open("resultado.txt", "w") as f:
    f.write(tabla.get_attribute("outerHTML"))
"""
# Suponiendo que 'tabla' es un WebElement de Selenium
html_content = tabla.get_attribute("outerHTML")

# Envuelve el HTML en StringIO
html_stream = StringIO(html_content)

# Lee la tabla
tabla_df = pd.read_html(html_stream)[0]

columnas = ["Valor", "Último", "Var", "Var%", "Vol", "Anterior", "Máximo", "Mínimo", "Hora"]
tabla_df.columns = columnas
tabla_df.to_csv("mercado_continuo.csv", index=False)
