import streamlit as st

def main():
    st.title('Lista de Compras')
    item = st.text_input('Digite o item:')
    if st.button('Adicionar à Lista'):
        st.write(f'Item adicionado: {item}')

if __name__ == '__main__':
    main()
