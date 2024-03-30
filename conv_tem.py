import streamlit as st

# Função para converter Celsius para Fahrenheit
def celsius_para_fahrenheit(temp_celsius):
    return (temp_celsius * 9/5) + 32

# Função para converter Celsius para Kelvin
def celsius_para_kelvin(temp_celsius):
    return temp_celsius + 273.15

# Função para converter Fahrenheit para Celsius
def fahrenheit_para_celsius(temp_fahrenheit):
    return (temp_fahrenheit - 32) * 5/9

# Função para converter Fahrenheit para Kelvin
def fahrenheit_para_kelvin(temp_fahrenheit):
    return (temp_fahrenheit - 32) * 5/9 + 273.15

# Função para converter Kelvin para Celsius
def kelvin_para_celsius(temp_kelvin):
    return temp_kelvin - 273.15

# Função para converter Kelvin para Fahrenheit
def kelvin_para_fahrenheit(temp_kelvin):
    return (temp_kelvin - 273.15) * 9/5 + 32

def main():
    st.title('Conversor de Unidade de Temperatura')

    # Entrada de temperatura e escala
    temperatura = st.number_input('Digite a temperatura:')
    escala_origem = st.selectbox('Selecione a escala de origem:', ['Celsius', 'Fahrenheit', 'Kelvin'])
    escala_destino = st.selectbox('Selecione a escala de destino:', ['Celsius', 'Fahrenheit', 'Kelvin'])

    # Conversão de temperatura conforme as escalas selecionadas
    if escala_origem == 'Celsius' and escala_destino == 'Fahrenheit':
        resultado = celsius_para_fahrenheit(temperatura)
    elif escala_origem == 'Celsius' and escala_destino == 'Kelvin':
        resultado = celsius_para_kelvin(temperatura)
    elif escala_origem == 'Fahrenheit' and escala_destino == 'Celsius':
        resultado = fahrenheit_para_celsius(temperatura)
    elif escala_origem == 'Fahrenheit' and escala_destino == 'Kelvin':
        resultado = fahrenheit_para_kelvin(temperatura)
    elif escala_origem == 'Kelvin' and escala_destino == 'Celsius':
        resultado = kelvin_para_celsius(temperatura)
    elif escala_origem == 'Kelvin' and escala_destino == 'Fahrenheit':
        resultado = kelvin_para_fahrenheit(temperatura)
    else:
        resultado = temperatura  # Não há conversão necessária

    # Exibir resultado da conversão
    st.write(f'A temperatura convertida é: {resultado:.2f} {escala_destino}')

if __name__ == '__main__':
    main()
