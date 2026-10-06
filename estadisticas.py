def calcular_estadisticas(registros_filtrados):
    if not registros_filtrados:
        return {
            "Cantidad":0,
            "Minimo": None,
            "Maximo": None,
            "Promedio": None
        }
    valores=[r["valor"] for r in registros_filtrados]
    cantidad=len(valores)
    minimo=min(valores)
    maximo=max(valores)
    promedio=sum(valores)/cantidad
    return {
        "Cantidad": cantidad,
        "Minimo": minimo,
        "Maximo": maximo,
        "Promedio": promedio
    }