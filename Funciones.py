import sys
def def_n(n):
    if str(n).isnumeric():
        numero = int(n)
        return (numero)
    else:
        return False

def convertidor_Fecha(F):
    n=def_n(F)
    if n:
        dia =n // 1000000
        mes = (n// 10000) % 100
        año = n % 10000 
        return dia,mes,año

def Es_bisiesto(F):
    convertido = convertidor_Fecha(F)[2]
    if convertido % 400 == 0:
        return 29
    elif convertido % 100 == 0:
        return 28
    elif convertido % 4 == 0:
        return 29
    else:
        return 28
    
def validar_fecha(F):
    if def_n(F):
        fecha=convertidor_Fecha(F)
        dia,mes,año=fecha
        if len(str(F)) == 8:
            if 1<=mes<=12:
                meses_31=[1,3,5,7,8,10,12]
                meses_30=[4,6,9,11]
                if mes in meses_31:
                    if 1 <= dia <= 31:
                        return True
                    else:
                        return False
                elif mes in meses_30:
                    if 1 <= dia <= 30:
                        return True
                    else:
                        return False
                elif mes==2:
                    if 1 <= dia <= Es_bisiesto(F) :
                        return True
                    else:
                        return False
            else:
                return "Error: Verifique que la fecha sea valida"
        else:
            return "Error: Sin dato de fecha"
    else:
        return "Error: Formato de fecha inválido"

def validar_hora(H):
    try:
        hora = int(H)
        if  hora < 0 or hora > 23:
            return "Error: Hora fuera de rango"
        else:
            return True
                
    except ValueError:
        return "Error: Formato de hora inválido"
        
def validar_temperatura(T):
    try:
        float(T)
        return True
    except ValueError:
        return "Error: Formato de temperatura inválido"

def validar_humedad(HUM):
    try:
        H=float(HUM)
        if  0 <= H and H <= 100:
            return True
        else:
            return "Error: Humedad fuera del rango"
    except ValueError:
        return "Error: Formato de la humedad inválido"

def validar_presion_viento(P):
    if P == "":
        return True
    try:
        hpa=float(P)
        if 0 <= hpa:
            return True
        else:
            return "Error: fuera de rango"   
    except ValueError:
        return "Error: Formato inválido"
      
def validar_direccion(d):
    try:
        num=float(d)
        if 0 <= num <= 360:
            return True
        else:
            return "Error: Dirección fuera de rango"
    except ValueError:
        return "Error: Formato de diraccion inválido"

def reconstruir_registro(AR):
    registros = []
    registro_actual = None
    try:
        with open(AR, "r") as archivo:
            for linea in archivo:
                linea = linea.rstrip("\n")
                if linea.strip() == "":
                    continue
                if linea[:8].strip().isnumeric():
                    if registro_actual is not None:
                        registros.append(registro_actual)
                    registro_actual = linea
                else:
                    if registro_actual is not None:
                        registro_actual = registro_actual.rstrip() + linea[44:].strip()
            if registro_actual is not None:
                registros.append(registro_actual)
        return registros
    except:
        return("Sin archivo TXT")

def parsear_registros(registro):
    fecha=registro[0:8].strip()
    hora = registro[9:15].strip()
    temperatura = registro[16:21].strip()
    humedad = registro[22:26].strip()
    presion = registro[27:34].strip()
    direccion_viento = registro[35:39].strip()
    velocidad_viento = registro[40:44].strip()
    nombre = registro[44:].strip()
    return fecha, hora, temperatura, humedad, presion, direccion_viento, velocidad_viento, nombre

def validar_registro(datos):
    errores = []
    fecha, hora, temperatura, humedad, presion, direccion, velocidad, nombre = datos
    resultado = validar_fecha(fecha)
    if resultado is not True:
        errores.append(resultado)

    resultado = validar_hora(hora)
    if resultado is not True:
        errores.append(resultado)

    resultado =validar_temperatura(temperatura) 
    if resultado is not True:
        errores.append(resultado)

    resultado = validar_humedad(humedad)   
    if resultado is not True:
        errores.append(resultado)

    resultado = validar_presion_viento(presion)
    if resultado is not True:
        errores.append(resultado)

    resultado = validar_direccion(direccion)
    if resultado is not True:
        errores.append(resultado)

    resultado = validar_presion_viento(velocidad)  
    if resultado is not True:
        errores.append(resultado)
    if nombre == "":
        errores.append("Nombre de estación vacío")

    return errores

def ruta_consola():
    if len(sys.argv)!=3:
        print("ERROR: Argumanetos incorrectos")
        print("Uso esperado: Main.py <lectura.txt> <archivo_salida.json>")
        sys.exit(1)
    archivo_txt=sys.argv[1]
    archivo_json=sys.argv[2]
    return archivo_txt, archivo_json
