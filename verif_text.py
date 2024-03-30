import streamlit as st

def analisar_texto(texto):
    palavras = texto.split()
    num_palavras = len(palavras)
    num_caracteres = len(texto)
    return num_palavras, num_caracteres

def main():
    st.title('Análise de Texto')

    texto_input = st.text_area('Digite o texto:')
    num_palavras, num_caracteres = analisar_texto(texto_input)

    st.write(f'Número de palavras: {num_palavras}')
    st.write(f'Número de caracteres: {num_caracteres}')

if __name__ == '__main__':
    main()

