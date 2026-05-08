import requests
import time
import os

# Render asigna una URL a tu servicio, búscala en el panel
# Ejemplo: https://mi-agente-ia.onrender.com
URL = os.environ.get("RENDER_EXTERNAL_URL", "https://tu-app.onrender.com")

def ping_agente():
    print(f"Iniciando Keep-Alive para: {URL}")
    while True:
        try:
            response = requests.get(URL)
            print(f"Ping exitoso: {response.status_code}")
        except Exception as e:
            print(f"Error al despertar al agente: {e}")
        
        # Espera 10 minutos (600 segundos)
        time.sleep(600)

if __name__ == "__main__":
    ping_agente()
