import streamlit as st
import pandas as pd

def salvar_dados_csv(dados):
    df = pd.DataFrame([dados])
    df.to_csv('dados_usuarios.csv', index=False)

def main():
    st.title('App para Armazenar Dados')
    
    # Entrada de dados do usuário
    nome = st.text_input('Nome:')
    idade = st.number_input('Idade:', min_value=0, max_value=150, step=1)
    peso = st.number_input('Peso (kg):', min_value=0.0)
    altura = st.number_input('Altura (cm):', min_value=0.0)
    endereco = st.text_area('Endereço:')
    
    # Botão para salvar os dados
    if st.button('Salvar Dados'):
        dados = {'Nome': nome, 'Idade': idade, 'Peso': peso, 'Altura': altura, 'Endereço': endereco}
        salvar_dados_csv(dados)
        st.success('Dados salvos com sucesso!')

if __name__ == '__main__':
    main()




