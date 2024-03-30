import streamlit as st
import random
import string

def gerar_senha(tamanho):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    return senha

def main():
    st.title('Gerador de Senhas')

    tamanho = st.slider('Selecione o tamanho da senha:', min_value=6, max_value=20)
    nova_senha = gerar_senha(tamanho)

    st.write(f'Sua nova senha é: {nova_senha}')

if __name__ == '__main__':
    main()


