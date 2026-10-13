import sys
import streamlit as st
import pandas as pd
from datos import cargar_json, filtrar_datoss
from estadisticas import calcular_estadisticas
from graficos import exportar_csv, generar_grafica

def main():
    st.title("Navegador de Estaciones Meteorologico")
    st.write("Esta aplicacion web se creo para poder consultar y analizar los datos de los Servicios Meteorologicos Nacional")
