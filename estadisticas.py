def calcular_estadisticas(registros_filtrados):
    if len(registros_filtrados) == 0:
        return {
            "Cantidad":0,
            "Minimo": None,
            "Maximo": None,
            "Promedio": None
        }
    lista_valores=[]
    for i in registros_filtrados():
        lista_valores.append(registros_filtrados)
    cantidad=len(lista_valores)
    minimo=min(lista_valores)
    maximo=max(lista_valores)
    promedio=sum(lista_valores)/cantidad
    return {
        "Cantidad": cantidad,
        "Minimo": minimo,
        "Maximo": maximo,
        "Promedio": promedio
    }