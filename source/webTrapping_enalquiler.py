import csv
from time import sleep
import pandas as pd
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
#Usamos selenium.Establecemos los drivers y la url madre para la extraccion de los datos
opts = Options()
opts.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.6045.123 Safari/537.36")
opts.add_argument("--headless")
driver = webdriver.Chrome(service = Service(ChromeDriverManager().install()), options=opts)
driver.get('https://www.enalquiler.com/search?provincia=16')
#se define la paginacion maxima
PAGINACION_MAX = 100 #para evitar saturar el sevidor
PAGINACION_ACTUAL = 1

list_inmuebles = [] #Estructura de datos con la  lista final de inmuebles
sleep(3) #para evitar saturar el sevidor

while PAGINACION_MAX > PAGINACION_ACTUAL:
    sleep(2) #para evitar saturar el sevidor
    #Extraemos los link de cada inmueble
    links_inmuebles = driver.find_elements(By.XPATH,'//a[@class="qa-search-tituloCard-exist propertyCard__description--title"]')
    links_de_la_pagina = []

    for a_link in links_inmuebles:
        links_de_la_pagina.append(a_link.get_attribute("href"))
    #Por cada inmueble extraemos los datos
    for link in links_de_la_pagina:
        try:
            sleep(2)
            driver.get(link)
            inmueble = dict()
            inmueble["titulo"] = driver.find_element(By.XPATH, '//div[@class="qa-search-tituloCard-exist property-info-title"]').text
            inmueble["precio"] = driver.find_element(By.XPATH, '//b[@class="priceBlock__price"]').text
            inmueble["lugar"]  = driver.find_element(By.XPATH, '//div[@class="overflow"]').text

            caracteristicas = driver.find_elements(By.XPATH,'//li[@class="resume-list-item"]')
            list_caracteristicas = dict()
            i = 0
            for caracteristica in caracteristicas:
                key= "C"+str(i)
                inmueble[key]= caracteristica.text
                i+=1

            caracteristicas = driver.find_elements(By.XPATH, '//ul[@class="property-characteristics-block-list"]')
            for caracteristica in caracteristicas:
                key = "C" + str(i)
                inmueble[key] = caracteristica.text
                i += 1

            lugar_esps = driver.find_elements(By.XPATH, '//div[@class="property-location-wrapper"]/address/div')
            i = 0
            for lugar_esp in lugar_esps:
                key = "L" + str(i)
                inmueble[key] = lugar_esp.text
                i += 1

            inmueble["descripcion"] = driver.find_element(By.XPATH, '//span[@id="description"]').text  # span  CardPrice

            list_inmuebles.append(inmueble)
            driver.back()

        except Exception as e:
            #controla si se propude algun error
            print(e)
            driver.back()

    try:
        #Obtenemos la paginacion para pasar a la siguiente pagina
        paginacion = driver.find_element(By.XPATH,'//a[text()="Siguiente"]')
        link_siguiente= paginacion.get_attribute("href")
        driver.get(link_siguiente)

    except:
       break

    PAGINACION_ACTUAL += 1

#Una  vez montado la estructura  con la informacion de los inmuebles   lo tranformamos en json
json_inmuebles = json.dumps(list_inmuebles, indent = 4)
# Convertimos el  JSON data en  pandas DataFrame
df = pd.read_json(json_inmuebles)
# Generamos el CVS a traver del  DataFrame
df.to_csv("salida.csv", index=False)