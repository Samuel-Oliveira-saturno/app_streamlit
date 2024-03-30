import streamlit as st

def calcular_imc(peso, altura):
    # Conversão da altura de metros para centímetros
    altura_cm = altura * 100
    # Cálculo do IMC: peso / (altura^2)
    imc = peso / (altura_cm ** 2)
    return imc

def main():
    st.title('Calculadora de IMC')

    # Entrada de dados do usuário
    peso = st.number_input('Digite o peso (em kg)', min_value=0.0)
    altura = st.number_input('Digite a altura (em metros)', min_value=0.0)

    if st.button('Calcular'):
        if peso > 0 and altura > 0:
            imc = calcular_imc(peso, altura)
            st.success(f'Seu IMC é {imc:.2f}')
        else:
            st.error('Por favor, digite valores válidos para peso e altura.')

if __name__ == '__main__':
    main()

