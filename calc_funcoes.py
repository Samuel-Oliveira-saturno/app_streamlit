import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

def calcular_funcao_1_grau(a, b, x):
    return a * x + b

def calcular_funcao_2_grau(a, b, c, x):
    return a * x**2 + b * x + c

def calcular_funcao_exponencial(base, expoente):
    return base ** expoente

def calcular_funcao_trigonometrica(angulo, funcao):
    if funcao == 'Seno':
        return np.sin(np.radians(angulo))
    elif funcao == 'Cosseno':
        return np.cos(np.radians(angulo))
    elif funcao == 'Tangente':
        return np.tan(np.radians(angulo))

def main():
    st.title('Calculadora de Funções')

    tipo_funcao = st.selectbox('Selecione o tipo de função:', ['1º Grau', '2º Grau', 'Exponencial', 'Trigonométrica'])

    if tipo_funcao == '1º Grau':
        a = st.number_input('Digite o coeficiente a:')
        b = st.number_input('Digite o coeficiente b:')
        x = st.number_input('Digite o valor de x:')
        resultado = calcular_funcao_1_grau(a, b, x)
        st.write(f'O resultado da função é: {resultado}')

    elif tipo_funcao == '2º Grau':
        a = st.number_input('Digite o coeficiente a:')
        b = st.number_input('Digite o coeficiente b:')
        c = st.number_input('Digite o coeficiente c:')
        x = st.number_input('Digite o valor de x:')
        resultado = calcular_funcao_2_grau(a, b, c, x)
        st.write(f'O resultado da função é: {resultado}')

    elif tipo_funcao == 'Exponencial':
        base = st.number_input('Digite a base:')
        expoente = st.number_input('Digite o expoente:')
        resultado = calcular_funcao_exponencial(base, expoente)
        st.write(f'O resultado da função é: {resultado}')

    elif tipo_funcao == 'Trigonométrica':
        angulo = st.number_input('Digite o valor do ângulo:')
        funcao = st.selectbox('Selecione a função:', ['Seno', 'Cosseno', 'Tangente'])
        resultado = calcular_funcao_trigonometrica(angulo, funcao)
        st.write(f'O resultado da função é: {resultado}')

if __name__ == '__main__':
    main()
