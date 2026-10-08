import sys
from datetime import datetime
from app_web.datos import cargar_json, filtrar_datoss
from estadisticas import calcular_estadisticas
from graficos import generar_grafica, exportar_csv

def main():
    if len(sys.argv)<4:
        print("Error, los argumentos son insuficientes")
        print("el uso deve ser: python procesar_datos.py <ruta_json> <estacion> <medicion>")
        sys.exit(1)
    ruta_json=sys.argv[1]
    estacion=sys.argv[2]
    medicion=sys.argv[3]
    try:
        registros_raw=cargar_json(ruta_json)
        filtrados=filtrar_datoss(registros_raw, estacion, medicion)
        if len(filtrados) ==0:
            print("no se encuentran los datos para la '{estacion}' y medicion '{medicion}'. ")
            return
        estadisticas=calcular_estadisticas(filtrados)
        print("estadisticas")
        for i ,o in estadisticas.keys():
            print(f"{i}: {o}")
        print("primeras 5")
        for i in estadisticas[5]:
            print(f"fecha: {i['fecha']}, hora: {i['hora']}, valor: {i['valor']}")
        fecha_de_hoy=datetime.now().strftime("%Y---%m---%d")
        ruta_csv= f"salidas/{fecha_de_hoy}_{estacion}_{medicion}.csv"
        ruta_png= f"salidas/{fecha_de_hoy}_{estacion}-{medicion}.png"

        exportar_csv(filtrados, ruta_csv)
        generar_grafica(filtrados, estacion, medicion, ruta_png)
        print(f"el CSV se gurardoen:{ruta_csv}")
        print(f"la grafica se guardo en: {ruta_png}")
    except Exception as error:
        print(f"se produgo un error en {error}")
main()

