import csv 
from pathlib import Path
import matplotlib.pyplot as plt

def exportar_csv(registros_filtrados, ruta_salida):
    path_salida=Path(ruta_salida)
    path_salida.parent.mkdir(parents=True, exist_ok=True)
    with open(path_salida, mode="w", newline="") as f:
        writre = csv.writer(f)
        writre.writerow(["fecha", "hora", "valor"])
        for reg in registros_filtrados:
            writre.writerow([reg["fecha"],reg["hora"],reg["valor"]])

def generar_grafica(registros_filtrados, estacion, medicion, ruta_salida):
    if len(registros_filtrados) ==0:
        return None
    path_salida=Path(ruta_salida)
    path_salida.parent.mkdir(parents=True,exist_ok=True)
    eje_x=[]
    eje_y=[]
    for i in registros_filtrados:
        etiquete_del_tiempo=f"{i['fecha']} {i['hora']}"
        eje_x.append(etiquete_del_tiempo)
        eje_y.append(r["valor"])

    plt.figure(figsize=(10,5))
    plt.plot(eje_x,eje_y, marcador="o", estilio_de_linea="-", color="r", eti=medicion.capitalize())
    plt.title(f"{medicion.capitalize()} en {estacion}")
    plt.xlabel("Fecha y hora")
    plt.ylabel(medicion.capitalize())
    plt.xticks(rotation=45, ha="derecha")
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(path_salida)
    plt.close()

    return str(path_salida)