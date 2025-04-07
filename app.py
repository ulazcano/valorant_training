import requests
import base64
import urllib3

# Deshabilitar advertencias de certificados no verificados
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def get_valorant_client_data():
    # Ruta y puerto de la API local del cliente de Valorant
    base_url = "https://127.0.0.1:port"  # Reemplaza 'port' con el puerto correcto (generalmente 2999 o 8080)

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
            print("Datos obtenidos con éxito:")
            print(response.json())
        else:
            print(f"Error al obtener datos: {response.status_code} - {response.text}")
    except Exception as e:
        print(f"Error al conectar con la API local: {e}")

# Llamar a la función
get_valorant_client_data()