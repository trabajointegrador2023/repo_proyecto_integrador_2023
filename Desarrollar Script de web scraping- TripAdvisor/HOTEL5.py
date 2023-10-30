import requests
from bs4 import BeautifulSoup

# URL de la página de hoteles en TripAdvisor para Córdoba, Argentina
url = "https://www.tripadvisor.com.ar/Hotels-g312768-Cordoba_Province_of_Cordoba_Central_Argentina-Hotels.html"

# Define un encabezado User-Agent que simula ser un navegador web (en este caso, Chrome)
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.1234.0 Safari/537.36"
}

try:
    # Realiza una solicitud HTTP con el encabezado configurado y un tiempo de espera
    response = requests.get(url, headers=headers, timeout=10)  # Espera 10 segundos como máximo

    # Verificar si la solicitud fue exitosa
    if response.status_code == 200:
        # Parsear el contenido HTML con BeautifulSoup utilizando lxml
        soup = BeautifulSoup(response.text, 'lxml')

        # Encontrar y extraer información de los nombres de los hoteles sin duplicados
        hotel_names = set()  # Utilizamos un conjunto para evitar duplicados

        # Buscar todos los elementos que contienen los nombres de los hoteles
        hotel_name_elements = soup.find_all("div", class_="listing_title")

        # Iterar a través de los resultados e imprimir los nombres
        for hotel_name_element in hotel_name_elements:
            name = hotel_name_element.text.strip()
            hotel_names.add(name)  # Agregar el nombre al conjunto

        # Iterar a través del conjunto de nombres únicos e imprimirlos
        for name in hotel_names:
            print("Nombre del hotel:", name)

    else:
        print("Error al hacer la solicitud HTTP.")

except Exception as e:
    print("Ocurrió un error durante la solicitud HTTP:", str(e))
