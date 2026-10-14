import sys
import os
import streamlit as st
import pandas as pd
from datos import cargar_json, filtrar_datoss
from estadisticas import calcular_estadisticas
from graficos import exportar_csv, generar_grafica
from conversor.Funciones import parsear_registros

if len(sys.argv)>1:
    ruta_json=sys.argv[1]
else:
    ruta_json="observaciones.json"
def app_web():
    st.title("Navegador de Estaciones Meteorologico")
    st.write("Esta aplicacion web se creo para poder consultar y analizar los datos de los Servicios Meteorologicos Nacional")
    archivo=cargar_json(ruta_json)
    if len(archivo)==0:
        st.warning("no se pudo cargar el archivo o no tiene nada")
        return
    nombres_estaciones=[]
    for i in archivo:
        *_,estacion=parsear_registros(i)
        estacion_limpia=estacion.strip()
        if estacion_limpia not in nombres_estaciones:
            nombres_estaciones.append(estacion_limpia)
    nombres_estaciones.sort()
    if not nombres_estaciones:
        st.write("las estaciones del archivo no son validas")
        return
    st.sidebar.header("opciones a buscar:")
    estacion_eleguida=st.sidebar.selectbox("cual estacion busca: ", nombres_estaciones)
    seleccion_de_variable=st.sidebar.selectbox("seleccione que magnitud buscada:",["temperatura", "humedad", "presion", "direccion del viento", "velocidad del viento"])
    archivo_filtrado=filtrar_datoss(archivo, estacion_eleguida, seleccion_de_variable)
    st.subheader(f"la estacion eleguida es: {estacion_eleguida}")
    if len(archivo_filtrado)>0:
        estadisticas=calcular_estadisticas(archivo_filtrado)
        cl1,cl2,cl3=st.columns(3)
        cl1.metric("promedio",f"{estadisticas.get('Promedio', 0)}")
        cl2.metric("maximo",f"{estadisticas.get('Maximo', 0)}")
        cl3.metric("minimo",f"{estadisticas.get('Minimo', 0)}")
        st.write("la tabla de los datos")
        df_tabla=pd.DataFrame(archivo_filtrado)
        st.dataframe(df_tabla)
        os.makedirs("salidas",exist_ok=True)
        ruta_csv="salidas/datos_de_la_estacion.csv"
        ruta_png="salidas/grafico.png"
        generar_grafica(archivo_filtrado, estacion_eleguida, seleccion_de_variable, ruta_png)
        if os.path.exists(ruta_png):
            st.image(ruta_png, caption=f"grafico de {seleccion_de_variable}, de la estacion {estacion_eleguida}")
        exportar_csv(archivo_filtrado,ruta_csv)
        with open(ruta_csv, "rb") as f:
            st.download_button(label="descarga del CSV", data=f, file_name="datos_de_la_estacion.csv", mime="text/csv")
    else:
        st.info("no se encuentran datos para los filtros selecionados")
app_web()