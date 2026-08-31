import json
from Funciones import validar_registro, parsear_registros, reconstruir_registro
#### PONER EL NOMBRE DE LOS ARCHIVOS EN SUS LUGARES CORRESONDIENTES: 
# Archivo_txt("nombre del archivo.txt)
# Archivo.json("nombre del archivo.json") ####

Archivo_txt=("lecturas.txt")
Archivo_json=()
registros = reconstruir_registro(Archivo_txt)
resumen={}
registros_validos =[]
registros_invalidos = []
clave_val= "Cantidad de registros validos"
clave_inv="Cantidad de registros invalidos"

try:
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
except:
    print("Error: No hay archivo TXT para leer")

try:
    with open (Archivo_json,"w") as Arj:
        json.dump(resumen,Arj,indent=1)
        json.dump(registros_validos,Arj,indent=1,ensure_ascii=False)
        if len(registros_invalidos)>0:
            json.dump(registros_invalidos,Arj,indent=1,ensure_ascii=False)
except:
    print ("Error: No hay archivo JSON para escribir")
###  Prueba para ver registros validos ###
#for registro in registros_validos:
    #print("----Registros valido----", "\n", registro)


###  Prueba para ver registros invalidos ###
#for registro in registros_invalidos:
    #print("----Registros invalido----", "\n", registro) #Prueba para ver registros invalidos