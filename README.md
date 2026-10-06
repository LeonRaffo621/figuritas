# Trabajo Integrador[Parte 1] - Figuritas repetidas

## Integrantes

- Leon Muñoz Raffo
- Thiago Emil Udi
- Ramiro Sanchez conejeros

---

## Descripción

Este programa procesa un archivo de texto que contiene registros meteorológicos, valida la información de cada registro y genera un archivo JSON con un resumen del procesamiento.

Cada registro es analizado verificando la validez de sus campos (fecha, hora, temperatura, humedad, presión, dirección y velocidad del viento, y nombre de la estación). Los registros válidos e inválidos son separados y almacenados en el archivo JSON de salida.

---

## Requisitos

- Python 3.x
- No se requieren librerías externas. El programa utiliza únicamente módulos estándar de Python (`json` y `sys`).

---

## Estructura del proyecto

```
Proyecto/
│
├── Main.py
├── Funciones.py
├── lectura.txt          # Archivo de entrada (ejemplo)
├── salida.json          # Archivo generado por el programa
└── README.md
```

---

## Ejecución

Abrir una terminal en la carpeta del proyecto y ejecutar:

```bash
python Main.py <archivo_entrada.txt> <archivo_salida.json>
```

### Ejemplo

```bash
python Main.py lectura.txt salida.json
```

Donde:

- `lectura.txt` es el archivo de entrada.
- `salida.json` es el nombre del archivo JSON que será generado.

---

## Archivo de entrada

El programa recibe un archivo de texto (`.txt`) que contiene registros meteorológicos.

El archivo de entrada contiene registros de mediciones meteorológicas. Cada registro incluye información sobre la fecha y hora de la medición, la temperatura, la humedad, la presión atmosférica, la dirección y velocidad del viento y el nombre de la estación meteorológica correspondiente.

Los registros pueden ocupar una o más líneas y son reconstruidos automáticamente antes de ser procesados.

---

## Validaciones realizadas

El programa verifica:

- Fecha válida.
- Hora entre 0 y 23.
- Temperatura con formato numérico.
- Humedad entre 0 y 100%.
- Presión atmosférica válida.
- Dirección del viento entre 0° y 360°.
- Velocidad del viento válida.
- Nombre de la estación no vacío.

---

## Archivo de salida

El programa genera un archivo JSON con tres secciones principales:

- Información general.
- Registros válidos.
- Registros inválidos.

### Estructura del JSON

```json
{
    "informacion_general": {
        "Cantidad de registros validos": 0,
        "Cantidad de registros invalidos": 0,
        "cantidad de registros": 0
    },
    "registros_validos": [
        "..."
    ],
    "registros_invalidos": [
        {
            "linea": "...",
            "errores": [
                "..."
            ]
        }
    ]
}
```

---

## Mensajes del programa

Durante la ejecución el programa puede mostrar mensajes como:

- Procesamiento finalizado con éxito.
- Error al escribir el archivo JSON.
- Error por cantidad incorrecta de argumentos al ejecutar el programa.

---

## Observaciones

- El nombre del archivo de entrada y del archivo de salida se reciben mediante argumentos de la línea de comandos (`sys.argv`).
- El archivo JSON se genera automáticamente al finalizar el procesamiento.