# Trabajo Integrador \[Parte 1\] - Figuritas repetidas

## Integrantes

* **León Muñoz Raffo**

* **Thiago Emil Udi**

* **Ramiro Sánchez Conejeros**

## Descripción del Trabajo

El objetivo principal de esta etapa es procesar un archivo de texto (`.txt`) que contiene registros meteorológicos de distintas estaciones. El programa lee los datos raw, reconstruye aquellas líneas que vienen cortadas, valida que los parámetros (fecha, hora, temperatura, humedad, presión y viento) cumplan los rangos correspondientes y guarda todo en un archivo estructurado `.json`.

Además, se incluyeron módulos auxiliares para filtrar los datos válidos generados, calcular estadísticas básicas (promedio, mínimos, máximos) y exportar los resultados a un archivo CSV y un gráfico `.png`.

## Estructura del Proyecto

El repositorio está organizado de la siguiente forma:

```
Proyecto/
│
├── Main.py              # Script principal para parsear y validar el TXT a JSON
├── Funciones.py         # Validaciones de fecha, hora, parámetros y lectura del TXT
├── Datos.py             # Módulo para cargar el JSON y filtrar mediciones por estación
├── estadisticas.py      # Funciones para calcular min, max, promedio y cantidad de datos
├── graficos.py          # Exportación a CSV y generación de gráficos con Matplotlib
├── Procesar_datos.py    # Script ejecutable para procesar métricas, generar CSV y gráficos
├── lectura.txt          # Archivo de entrada de ejemplo con mediciones meteorológicas
├── salida.json          # Archivo JSON generado tras correr Main.py
└── README.md            # Documentación del proyecto

```

## Ejecución del Programa

La primera parte del trabajo tiene dos etapas principales de ejecución desde la terminal:

### 1. Limpieza y validación de datos (`Main.py`)

Lee el archivo de texto y genera el JSON con los datos separados entre válidos e inválidos.

```
python Main.py <archivo_entrada.txt> <archivo_salida.json>

```

**Ejemplo:**

```
python Main.py lectura.txt salida.json

```

### 2. Análisis, estadísticas y gráficos (`Procesar_datos.py`)

Toma el archivo JSON generado anteriormente, filtra por una estación específica y un tipo de medición, imprime las estadísticas en consola y guarda los resultados en la carpeta `salidas/`.

```
python Procesar_datos.py <ruta_json> <nombre_estacion> <tipo_medicion>

```

**Ejemplo:**

```
python Procesar_datos.py salida.json "Estación 1" temperatura

```

> **Mediciones disponibles:** `temperatura`, `humedad`, `presion` (o `percion`), `direccion del viento`, `velocidad del viento`.

## Detalle de Validaciones Realizadas

Dentro de `Funciones.py`, cada registro pasa por las siguientes comprobaciones antes de considerarse válido:

* **Fecha:** Formato numérico de 8 dígitos (`DDMMAAAA`), verificando días por mes y años bisiestos para febrero.

* **Hora:** Valor entero entre `0` y `23`.

* **Temperatura:** Formato numérico convertible a decimal (`float`).

* **Humedad:** Valor numérico porcentual entre `0%` y `100%`.

* **Presión y Viento:** Presión atmosférica y velocidad de viento no negativas.

* **Dirección del viento:** Ángulo entre `0°` y `360°`.

* **Estación:** El nombre no debe estar vacío.

## Estructura del Archivo de Salida (`JSON`)

El archivo JSON producido se organiza en tres secciones principales:

```
{
    "informacion_general": {
        "Cantidad de registros validos": 12,
        "Cantidad de registros invalidos": 3,
        "cantidad de registros": 15
    },
    "registros_validos": [
        "01022024 1400 25.4 60.0 1013.2 180.0 12.5 Estacion Central"
    ],
    "registros_invalidos": [
        {
            "linea": "01022024 2500 25.4 60.0 ...",
            "errores": [
                "Error: Hora fuera de rango"
            ]
        }
    ]
}

```

## Mensajes del Sistema

Al ejecutar los scripts verás mensajes por consola como:

* `Procesamiento finalizado con éxito.`

* `Archivo generado: salida.json`

* `ERROR: Argumentos incorrectos` *(si falta algún parámetro en la terminal)*.

* `Error: El archivo ... no existe.`
