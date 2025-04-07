import requests
from requests.auth import HTTPBasicAuth
import urllib3
import json

# Evitar warnings de SSL (porque el certificado es autofirmado)
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Datos del lockfile
port = 64288
password = "c7hziOV55XfuOcf5NZr4Cw"

# URL base
base_url = f"https://127.0.0.1:{port}"

# Ruta que quieres consultar (a modo de ejemplo)
endpoint = "/chat/v4/friends"  # Puedes cambiarlo por el que necesites

# Hacemos la petición
response = requests.get(
    base_url + endpoint,
    auth=HTTPBasicAuth('riot', password),
    verify=False  # Para ignorar certificado SSL autofirmado
)

# Imprimir respuesta
print("Status Code:", response.status_code)
print("Response JSON:", response.json())
with open("response.json", "w", encoding="utf-8") as json_file:
    json.dump(response.json(), json_file, ensure_ascii=False, indent=4)
    print("Datos guardados en response.json")






import requests
import base64
import urllib3

# Deshabilitar advertencias de certificados no verificados
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def fetch_and_save_api_data():
    # Ruta y puerto de la API local del cliente de Valorant
    base_url = "https://127.0.0.1:2999"  # Reemplaza '2999' con el puerto correcto

    # Credenciales de autenticación (puedes obtenerlas del proceso del cliente de Valorant)
    username = "riot"
    password = "tu_token_de_autenticacion"  # Reemplaza con el token de autenticación correcto

    # Codificar las credenciales en Base64
    auth = base64.b64encode(f"{username}:{password}".encode()).decode()

    # Encabezados de la solicitud
    headers = {
        "Authorization": f"Basic {auth}"
    }

    # Endpoint de ejemplo (puedes cambiarlo según lo que necesites)
    endpoint = "/chat/v4/presences"

    try:
        # Realizar la solicitud GET
        response = requests.get(base_url + endpoint, headers=headers, verify=False)
        if response.status_code == 200:
            # Guardar la respuesta en un archivo JSON
            with open("response.json", "w", encoding="utf-8") as json_file:
                json.dump(response.json(), json_file, ensure_ascii=False, indent=4)
            print("Datos guardados en response.json")
        else:
            print(f"Error al obtener datos: {response.status_code} - {response.text}")
    except Exception as e:
        print(f"Error al conectar con la API local: {e}")

# Llamar a la función
fetch_and_save_api_data()