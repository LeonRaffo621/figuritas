"""lectura txt"""
from Funciones import validar_registro, parsear_registros, reconstruir_registro
#### PONER ARCHIVO A LEER EN "nombre_archivo" ejemplo "datohorario20260826" ####

registros = reconstruir_registro("nombre_archivo")
registros_validos = []
registros_invalidos = []

for registro in registros:
    datos = parsear_registros(registro)
    errores = validar_registro(datos)
    if len(errores) == 0:
        registros_validos.append(registro)
    else:
        registros_invalidos.append({
            "linea":registro,
            "errores":errores
            })

###  Prueba para ver registros validos ###
#for registro in registros_validos:
    #print("----Registros valido----", "\n", registro)


###  Prueba para ver registros invalidos ###
#for registro in registros_invalidos:
    #print("----Registros invalido----", "\n", registro) #Prueba para ver registros invalidos