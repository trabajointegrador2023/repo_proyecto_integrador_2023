import requests
from bs4 import BeautifulSoup
import csv

# URL de la página de hoteles en TripAdvisor para Córdoba, Argentina
url = "https://www.tripadvisor.com.ar/Hotels-g312768-oa60-zfd21371-a_distFrom.313130%2C10-a_ufe.true-Cordoba_Province_of_Cordoba_Central_Argentina-Hotels.html"

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

        # Encontrar y extraer las direcciones URL y nombres de los hoteles
        hotel_info = []

        # Buscar todos los enlaces de los hoteles
        hotel_link_elements = soup.find_all("a", class_="property_title")

        # Iterar a través de los resultados y recopilar los nombres y URLs
        for link_element in hotel_link_elements:
            hotel_url = "https://www.tripadvisor.com.ar" + link_element.get("href")
            hotel_name = link_element.text.strip()
            hotel_info.append((hotel_name, hotel_url))

        # Crear un archivo CSV para almacenar los datos
        csv_filename = "hoteles_cordoba3D.csv"  # Nombre del archivo CSV
        csv_file = open(csv_filename, mode="w", newline="", encoding="utf-8")  # Abre el archivo en modo escritura con UTF-8
        csv_writer = csv.writer(csv_file)  # Crea un escritor de CSV

        # Agregar encabezados al archivo CSV
        csv_writer.writerow(["Nombre", "URL", "Dirección", "Calificación", "Opiniones de usuarios"])

        # Ahora, puedes iterar a través de los nombres y URLs de los hoteles para extraer sus detalles
        for hotel_name, hotel_url in hotel_info[:30]:  # Limitado a los primeros 30 hoteles
            response = requests.get(hotel_url, headers=headers, timeout=10)
            if response.status_code == 200:
                hotel_soup = BeautifulSoup(response.text, 'lxml')

                # Extraer la dirección del hotel
                address_element = hotel_soup.find("span", class_="fHvkI PTrfg")
                if address_element:
                    address = address_element.text.strip()
                else:
                    address = "Dirección no encontrada"

                # Extraer la calificación del hotel
                name_element = hotel_soup.find("h1", class_="QdLfr b d Pn")
                numerical_rating_element = hotel_soup.find("span", class_="uwJeR P")
                rating_element = hotel_soup.find("div", class_="kkzVG")

                if name_element and numerical_rating_element and rating_element:
                    name = name_element.text.strip()
                    numerical_rating = numerical_rating_element.text.strip()
                    rating = rating_element.text.strip()
                else:
                    name = "Nombre no encontrado"
                    numerical_rating = "Calificación no encontrada"
                    rating = "Calificación no encontrada"

                # Extraer opiniones de usuarios
                user_reviews = hotel_soup.find_all("span", class_="QewHA H4 _a")
                reviews = [review.get_text(strip=True) for review in user_reviews]

                # Escribir los detalles del hotel en el archivo CSV
                csv_writer.writerow([name, hotel_url, address, numerical_rating, "\n".join(reviews[:5])])

            else:
                print(f"Error al obtener la página del hotel ({hotel_name}). Código de estado: {response.status_code}")

        # Cerrar el archivo CSV
        csv_file.close()

        print("Los datos se han almacenado en el archivo CSV con éxito.")

    else:
        print("Error al hacer la solicitud HTTP.")

except Exception as e:
    print("Ocurrió un error durante la solicitud HTTP:", str(e))
