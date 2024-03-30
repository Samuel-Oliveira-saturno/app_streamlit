import streamlit as st
import pandas as pd
from datetime import datetime

# Função para carregar ou criar o dataframe de atividades
def carregar_dataframe():
    try:
        df = pd.read_csv('registro_atividades.csv')
    except FileNotFoundError:
        df = pd.DataFrame(columns=['Data', 'Atividade'])
    return df

# Função para salvar o dataframe no arquivo CSV
def salvar_dataframe(df):
    df.to_csv('registro_atividades.csv', index=False)

# Função principal
def main():
    st.title('Registro de Atividades Diárias')

    df = carregar_dataframe()

    # Seção para adicionar nova atividade
    st.header('Adicionar Nova Atividade')
    nova_atividade = st.text_input('Digite a atividade realizada:')
    if st.button('Adicionar Atividade'):
        if nova_atividade.strip() != '':
            hoje = datetime.now().strftime('%Y-%m-%d')
            df = df.append({'Data': hoje, 'Atividade': nova_atividade}, ignore_index=True)
            salvar_dataframe(df)
            st.success('Atividade adicionada com sucesso.')

    # Seção para exibir o registro de atividades
    st.header('Registro de Atividades')
    st.write(df)

if __name__ == '__main__':
    main()
