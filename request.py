import requests

# URL de tu servidor FastAPI
url = "https://valorant-training.onrender.com//send-message/"

# Datos que quieres enviar
payload = {
    "quadrant": 0,  # Número del cuadrante (0, 1, 2 o 3)
    "message": "¡Hola, cuadrante 0!",
    "color": "#FFCCCC"  # Color de fondo (puede ser en formato hex o palabra como "red")
}

# Mandar el POST
response = requests.post(url, json=payload)

# Mostrar la respuesta del servidor
print("Status Code:", response.status_code)
print("Respuesta:", response.json())