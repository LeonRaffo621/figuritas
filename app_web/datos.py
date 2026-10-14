import json
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from conversor.Funciones import parsear_registros

def cargar_json(r_json):
    try:
        with open(r_json, "r", encoding="utf-8", errors="ignore") as f:
            datos = json.load(f)
        return datos.get("registros_validos", datos.get("registros validos", []))
    except FileNotFoundError:
        raise FileNotFoundError(f"El archivo '{r_json}' no existe")

def filtrar_datoss(registros_raw, estacion_buscada, medicion_buscada):
    tipos_de_mediciones = {
        "temperatura": 2,
        "humedad": 3,
        "presion": 4,
        "direccion del viento": 5,
        "velocidad del viento": 6
    }
    
    medicion_normalizada = medicion_buscada.lower().strip()
    if medicion_normalizada not in tipos_de_mediciones:
        opciones_validas = ", ".join(tipos_de_mediciones.keys())
        raise ValueError(f"El tipo de medicion no es valida: '{medicion_buscada}'. Las opciones son: {opciones_validas}")
        
    indece_de_medicion = tipos_de_mediciones[medicion_normalizada]
    estacion_buscada_normalizada = estacion_buscada.upper().strip()
    
    filtrados = []
    for reg_str in registros_raw:
        fecha, hora, temperatura, humedad, presion, direccion_viento, velocidad_viento, estacion = parsear_registros(reg_str)
        
        estacion_limpia = estacion.upper().strip()
        
        if estacion_buscada_normalizada == estacion_limpia or estacion_buscada_normalizada in estacion_limpia:
            valores_parseados = [fecha, hora, temperatura, humedad, presion, direccion_viento, velocidad_viento]
            valores_str = valores_parseados[indece_de_medicion]
            
            if valores_str != "":
                try: 
                    valor_num = float(valores_str)
                    registro_dicc = {
                        "fecha": fecha,
                        "hora": int(hora) if hora != "" else 0,
                        "valor": valor_num,
                        "estacion": estacion.strip()
                    }
                    filtrados.append(registro_dicc)
                except ValueError:
                    continue
                    
    return filtrados