import json
from conversor.Funciones import parsear_registros

def cargar_json(r_json):
    try:
        with open(r_json, "r") as f:
            datos=json.load(f)
        return datos.get("registros validos", [])
    except FileNotFoundError:
        raise FileNotFoundError(f"El archivo '{r_json}' no exixte")

def filtrar_datoss(registros_raw, estacion_buscada, medicion_buscada):
    tipos_de_mediciones={
        "temperatura":2,
        "humedad":3,
        "percion": 4,
        "direccion del viento": 5,
        "velocidad del viento":6
    }
    medicion_normalizada=medicion_buscada.lower().strip()
    if medicion_normalizada not in tipos_de_mediciones:
        raise ValueError(f"El tipode medicion no es valida: '{medicion_buscada}'. Las opciones de mediciones son: {list(tipos_de_mediciones.keys())}")
    indece_de_medicion=tipos_de_mediciones[medicion_normalizada]
    estacion_buscada_normalizada=estacion_buscada.upper().strip()
    filtrados=[]
    for reg_str in registros_raw:
        fecha, hora, temperatura, humedad, precion, direccion_viento, velocidad_viento, estacion=  parsear_registros(reg_str)
        if estacion.upper().strio()==estacion_buscada_normalizada:
            valores_parseados= [fecha, hora, temperatura, humedad, precion, direccion_viento, velocidad_viento]
            valores_str=valores_parseados[indece_de_medicion]
            if valores_str !="":
                try: 
                    valor_num=float(valores_str)
                    registro_dicc={
                        "fecha": fecha,
                        "hora": int(hora),
                        "valor": valor_num,
                        "estacion": estacion
                    }
                    filtrados.append(registro_dicc)
                except ValueError:
                    continue
    return filtrados

