import streamlit as st
import math

def calcular_area_retangulo(base, altura):
    return base * altura

def calcular_area_triangulo(base, altura):
    return (base * altura) / 2

def calcular_area_circulo(raio):
    return math.pi * (raio ** 2)

def main():
    st.title('Calculadora de Área de Figuras Geométricas')

    figura = st.selectbox('Selecione a figura geométrica:', ['Retângulo', 'Triângulo', 'Círculo'])

    if figura == 'Retângulo':
        base = st.number_input('Digite a base do retângulo:')
        altura = st.number_input('Digite a altura do retângulo:')
        if st.button('Calcular Área'):
            area = calcular_area_retangulo(base, altura)
            st.success(f'A área do retângulo é {area:.2f} unidades²')

    elif figura == 'Triângulo':
        base = st.number_input('Digite a base do triângulo:')
        altura = st.number_input('Digite a altura do triângulo:')
        if st.button('Calcular Área'):
            area = calcular_area_triangulo(base, altura)
            st.success(f'A área do triângulo é {area:.2f} unidades²')

    elif figura == 'Círculo':
        raio = st.number_input('Digite o raio do círculo:')
        if st.button('Calcular Área'):
            area = calcular_area_circulo(raio)
            st.success(f'A área do círculo é {area:.2f} unidades²')

if __name__ == '__main__':
    main()





