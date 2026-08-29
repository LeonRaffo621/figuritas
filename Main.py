"""lectura txt"""
from Funciones import validar_registro, transformar_registros, reconstruir_registro
registros = reconstruir_registro("datohorario20260826.txt")
registros_validos = []
registros_invalidos = []

for registro in registros:
    datos = transformar_registros(registro)
    errores = validar_registro(datos)
    if len(errores) == 0:
        registros_validos.append(registro)
    else:
        registros_invalidos.append(registro)

#for registro in registros_validos:
    #print("----Registros valido----", "\n", registro) #Prueba para ver registros validos

#for registro in registros_invalidos:
    #print("----Registros invalido----", "\n", registro) #Prueba para ver registros invalidos