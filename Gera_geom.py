import streamlit as st
import altair as alt
import pandas as pd
import numpy as np

# Funções para criar as figuras geométricas
def criar_triangulo(base, altura):
    x = [0, base / 2, base, 0]
    y = [0, altura, 0, 0]
    return pd.DataFrame({'x': x, 'y': y})

def criar_retangulo(largura, altura):
    x = [0, largura, largura, 0, 0]
    y = [0, 0, altura, altura, 0]
    return pd.DataFrame({'x': x, 'y': y})

def criar_circulo(raio, pontos=100):
    theta = np.linspace(0, 2*np.pi, pontos)
    x = raio * np.cos(theta)
    y = raio * np.sin(theta)
    return pd.DataFrame({'x': x, 'y': y})

# Interface do aplicativo
st.title('Gráficos de Figuras Geométricas')

figura = st.selectbox('Selecione a figura:', ['Triângulo', 'Retângulo', 'Círculo'])

if figura == 'Triângulo':
    base = st.slider('Base do triângulo', 1, 10, 5)
    altura = st.slider('Altura do triângulo', 1, 10, 5)
    df = criar_triangulo(base, altura)
elif figura == 'Retângulo':
    largura = st.slider('Largura do retângulo', 1, 10, 5)
    altura = st.slider('Altura do retângulo', 1, 10, 5)
    df = criar_retangulo(largura, altura)
elif figura == 'Círculo':
    raio = st.slider('Raio do círculo', 1, 10, 5)
    df = criar_circulo(raio)

# Gerar gráfico com Altair
chart = alt.Chart(df).mark_point(filled=True).encode(
    x='x',
    y='y',
    color=alt.value('blue'),  # Cor das figuras
    size=alt.value(100)  # Tamanho dos pontos
).properties(
    width=500, height=500  # Tamanho do gráfico
)

st.altair_chart(chart)
