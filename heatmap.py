import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Criando um dataframe fictício para a análise
data = {
    'Produto': ['A', 'B', 'C', 'A', 'B', 'C', 'A', 'B', 'C'],
    'Mes': ['Jan', 'Jan', 'Jan', 'Fev', 'Fev', 'Fev', 'Mar', 'Mar', 'Mar'],
    'Vendas': [100, 150, 80, 120, 200, 90, 180, 160, 100],
    'Lucro': [20, 30, 15, 25, 40, 20, 35, 30, 18]
}
df = pd.DataFrame(data)

def main():
    st.title('Análise Descritiva, Correlação e Mapa de Calor')

    # Exibindo os dados
    st.header('Dados de Vendas')
    st.write(df)

    # Análise Descritiva
    st.header('Análise Descritiva')
    st.write(df.groupby('Produto').agg({'Vendas': 'sum', 'Lucro': 'sum'}))

    # Análise de Correlação e Mapa de Calor
    st.header('Análise de Correlação e Mapa de Calor')

    # Calculando a matriz de correlação
    correlacao = df[['Vendas', 'Lucro']].corr()

    # Gerando o mapa de calor
    plt.figure(figsize=(8, 6))
    sns.heatmap(correlacao, annot=True, cmap='coolwarm', linewidths=0.5)
    plt.title('Mapa de Calor da Correlação')
    st.pyplot()

if __name__ == '__main__':
    main()
