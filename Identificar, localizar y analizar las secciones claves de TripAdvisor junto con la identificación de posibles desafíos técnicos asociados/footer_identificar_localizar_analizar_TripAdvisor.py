import requests
from bs4 import BeautifulSoup

# URL de la página web
url = "https://www.tripadvisor.com.ar/"

# Define un encabezado User-Agent que simula ser Chrome
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.1234.0 Safari/537.36"
}

# Realiza la solicitud HTTP con el encabezado configurado
response = requests.get(url, headers=headers)

# Verifica si la solicitud fue exitosa (código de respuesta 200)
if response.status_code == 200:
    # El contenido de la página está en response.text
    # Puedes utilizar BeautifulSoup con 'lxml' para analizarlo
    soup = BeautifulSoup(response.text, 'lxml')

    # Ahora puedes buscar el elemento <footer> en el HTML
    footer = soup.find('footer')

    # Imprime el contenido del footer
    if footer:
        print(footer.prettify())
        
        # Puedes realizar más análisis del contenido del footer aquí
        # Por ejemplo, para extraer todos los enlaces dentro del footer:
        footer_links = footer.find_all('a')
        for link in footer_links:
            print("Enlace:", link.get('href'))
            
        # También puedes extraer texto u otros elementos según tus necesidades
        
    else:
        print("No se encontró el elemento <footer> en la página.")

else:
    print("Error al hacer la solicitud HTTP.")
