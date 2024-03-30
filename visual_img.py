import streamlit as st
from PIL import Image

def main():
    st.title('Visualizador de Imagens')
    uploaded_file = st.file_uploader('Carregue uma imagem:', type=['jpg', 'png', 'jpeg'])
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption='Imagem carregada', use_column_width=True)

if __name__ == '__main__':
    main()
