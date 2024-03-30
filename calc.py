import streamlit as st

def calcular_juros_compostos(capital, taxa, periodo):
    montante = capital * (1 + taxa / 100) ** periodo
    return montante

def main():
    st.title('Calculadora de Juros Compostos')

    # Entrada de dados do usuário
    capital = st.number_input('Digite o capital inicial:', min_value=0.0)
    taxa = st.number_input('Digite a taxa de juros (% ao ano):', min_value=0.0)
    periodo = st.number_input('Digite o período de tempo (anos):', min_value=0.0)

    # Botão para calcular
    if st.button('Calcular'):
        montante_final = calcular_juros_compostos(capital, taxa, periodo)
        st.success(f'O montante final após {periodo} anos será de R${montante_final:.2f}')

if __name__ == '__main__':
    main()


