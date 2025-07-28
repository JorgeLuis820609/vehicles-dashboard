import pandas as pd
import plotly.express as px
import streamlit as st

# Título de la app
st.header('Panel interactivo de vehículos')

# Cargar datos
car_data = pd.read_csv('vehicles_us.csv')

# Botón para histograma
if st.button('Mostrar histograma de odómetro'):
    st.write('Histograma de odómetro:')
    fig1 = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig1, use_container_width=True)

# Botón para gráfico de dispersión
if st.button('Mostrar gráfico de dispersión odómetro vs precio'):
    st.write('Gráfico de dispersión entre odómetro y precio:')
    fig2 = px.scatter(car_data, x="odometer", y="price")
    st.plotly_chart(fig2, use_container_width=True)
