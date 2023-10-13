import selenium
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# definimos la url a controlar
url = "https://www.tripadvisor.com/Hotel_Review-g312768-d482464-Reviews-Amerian_Cordoba_Park_Hotel-Cordoba_Province_of_Cordoba_Central_Argentina.html"
# especificamos la direccion de la carpeta donde esta el webdriver para el navegador
path_driver = os.chdir("C:\chromedriver")
#generamos un canal en el navegador elegido para ejecutar el driver(aqui la variable driver es un objeto)
driver = webdriver.Chrome()
# antes de traer la ventana o abrirla, le damos la propiedad de maximizar la misma
driver.maximize_window()
# ahora le pasamos la variable con el nombre de la direccion de la pagina a controlar
driver.get(url)
# encontramos el primer texto de prueba
casa = []
# texto de prueba 0
texto_0 = driver.find_element(By.XPATH,"/html/body/div[2]/div[2]/div[1]/div[2]/div/div/div[1]/div[2]/div[1]/h1")
print("-----------")
print(texto_0.text)
print("-----------")
"""
# texto de prueba 1
texto_1 = driver.find_element(By.XPATH,"/html/body/div[2]/div[2]/div[1]/div[2]/div/div/div[1]/div[3]/div[1]/div[2]/span[2]")
print("-----------")
print(texto_1.text)
print("-----------")

# texto de prueba 2
texto_2 = driver.find_element(By.XPATH,"/html/body/div[2]/div[2]/div[2]/div[4]/div/div/div[4]/div/div/div/div/div[2]/div[1]/div[3]/div")
print("-----------")
print(texto_2.text)
print("-----------")
"""
# texto de prueba 3
texto_3 = driver.find_element(By.XPATH,"/html/body/div[2]/div[2]/div[2]/div[10]/div/div/div[3]/div[1]/div/div[3]/div[2]/div[3]")
print("-----------")
print(texto_3.text)
print("-----------")
# para poder ver la ventana y que no se cierre rapido, le damos la funcion tiempo, durmiendola unos segundos
time.sleep(1)