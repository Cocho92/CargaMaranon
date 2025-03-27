import os
import requests
import openpyxl
import json
import pandas as pd
from time import sleep
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

# Configuración desde variables de entorno
API_URL = os.getenv('API_URL', 'http://localhost:8000')  # Ejemplo seguro
API_KEY = os.getenv('API_KEY')
API_TOKEN = os.getenv('API_TOKEN')
EXCEL_FILE = os.getenv('EXCEL_FILE', 'datos_atenciones.xlsx')  # Valor por defecto
SHEET_NAME = os.getenv('SHEET_NAME', 'Hoja1')  # Valor por defecto
DELAY_BETWEEN_REQUESTS = float(os.getenv('DELAY_BETWEEN_REQUESTS', 1))  # Valor por defecto

# Headers constantes
HEADERS = {
    'Token': API_TOKEN,
    'Content-Type': 'application/json'
}

def enviar_atencion(datos_fila):
    """Envía una atención a la API"""
    payload = json.dumps({
        "aplicacion": "Maranon",
        "operacion": "informarInsertarAtencion",
        "apiKey": API_KEY,
        "datos": {
            "IdPaciente": str(datos_fila["IdPaciente"]),
            "Ambito": datos_fila["Ambito"],
            "IdPlanCobertura": str(datos_fila["IdPlanCobertura"]),
            "IDInternacion": str(datos_fila["IDInternacion"]),
            "FechaHora": datos_fila["FechaHora"],
            "TipoAtencion": datos_fila["TipoAtencion"],
            "CodigoAtencion": datos_fila["CodigoAtencion"],
            "IdProfesional": str(datos_fila["IdProfesional"]),
            "IdServicio": str(datos_fila["IdServicio"])
        }
    })
    
    try:
        response = requests.post(API_URL, headers=HEADERS, data=payload)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error al enviar datos: {e}")
        return None
    
def main():
    #Leer Archivo excel
    try:
        df= pd.read_excel(EXCEL_FILE, sheet_name=SHEET_NAME)
    except Exception as e:
        print(f"")

