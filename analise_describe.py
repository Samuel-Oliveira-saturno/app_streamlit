import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Criando um dataframe fictício para a análise
data = {
    'Produto': ['A', 'B', 'C', 'A', 'B', 'C', 'A', 'B', 'C'],
    'Mes': ['Jan', 'Jan', 'Jan', 'Fev', 'Fev', 'Fev', 'Mar', 'Mar', 'Mar'],
    'Vendas': [100, 150, 80, 120, 200, 90, 180, 160, 100]
}
df = pd.DataFrame(data)

def main():
    st.title('Análise Descritiva e Gráficos')

    # Exibindo os dados
    st.header('Dados de Vendas')
    st.write(df)

    # Análise Descritiva
    st.header('Análise Descritiva')
    st.write(df.groupby('Produto')['Vendas'].describe())

    # Gráficos
    st.header('Gráficos')

    # Gráfico de Barras: Vendas por Produto
    st.subheader('Vendas por Produto')
    plt.figure(figsize=(10, 6))
    sns.barplot(data=df, x='Produto', y='Vendas', estimator=sum, ci=None)
    plt.xlabel('Produto')
    plt.ylabel('Vendas')
    plt.title('Total de Vendas por Produto')
    st.pyplot()

    # Gráfico de Linhas: Vendas ao longo dos Meses
    st.subheader('Vendas ao longo dos Meses')
    plt.figure(figsize=(10, 6))
    sns.lineplot(data=df, x='Mes', y='Vendas', hue='Produto', marker='o')
    plt.xlabel('Mês')
    plt.ylabel('Vendas')
    plt.title('Vendas por Produto ao longo dos Meses')
    st.pyplot()

if __name__ == '__main__':
    main()
