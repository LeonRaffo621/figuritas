import json
from pathlib import Path
from Funciones import validar_registro, parsear_registros, reconstruir_registro, ruta_consola

Archivo_txt, Archivo_json = ruta_consola()
Archivo_txt = Path(Archivo_txt)
resumen={}
registros_validos =[]
registros_invalidos = []
clave_val= "Cantidad de registros validos"
clave_inv="Cantidad de registros invalidos"


if Archivo_txt.is_file():
    registros = reconstruir_registro(Archivo_txt)
    for registro in registros:
        datos = parsear_registros(registro)
        errores = validar_registro(datos)
        if len(errores) == 0:
            registros_validos.append(registro)
            if clave_val not in resumen:
                resumen[clave_val]=1
            else:
                resumen[clave_val]+=1       
        else:
            registros_invalidos.append({
                "linea":registro,
                "errores":errores
                })
            if clave_inv not in resumen:
                resumen[clave_inv]=1
            else:
                resumen[clave_inv]+=1
    suma_de_registros=resumen[clave_val]+resumen[clave_inv]
    resumen["cantidad de registros"]=suma_de_registros        
    datos_json = {
        "informacion_general": resumen,
        "registros_validos": registros_validos,
        "registros_invalidos": registros_invalidos
    }

    try:
        with open(Archivo_json, "w") as Arj:
            json.dump(datos_json, Arj, indent=4, ensure_ascii=False)
        print("\nProcesamiento finalizado con éxito.")
        print(f"Archivo generado: {Archivo_json}")
    except Exception as e:
        print(f"Error al escribir el archivo JSON: {e}")

    print (resumen)
else:
    print(f"Error: El archivo {Archivo_txt} no existe.")