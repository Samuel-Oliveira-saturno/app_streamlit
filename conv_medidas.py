import streamlit as st

# Funções de conversão de unidades de comprimento
def metros_para_centimetros(valor):
    return valor * 100

def centimetros_para_metros(valor):
    return valor / 100

def metros_para_kilometros(valor):
    return valor / 1000

def kilometros_para_metros(valor):
    return valor * 1000

def polegadas_para_centimetros(valor):
    return valor * 2.54

def centimetros_para_polegadas(valor):
    return valor / 2.54

def main():
    st.title('Conversor de Unidade de Medida')

    # Entrada de valor e unidade de medida de origem
    valor = st.number_input('Digite o valor:')
    unidade_origem = st.selectbox('Selecione a unidade de medida de origem:', ['Metros', 'Centímetros', 'Quilômetros', 'Polegadas'])

    # Conversão de unidade de medida
    if unidade_origem == 'Metros':
        valor_convertido = metros_para_centimetros(valor)
        valor_convertido_km = metros_para_kilometros(valor)
        valor_convertido_in = centimetros_para_polegadas(metros_para_centimetros(valor))
    elif unidade_origem == 'Centímetros':
        valor_convertido = centimetros_para_metros(valor)
        valor_convertido_km = metros_para_kilometros(centimetros_para_metros(valor))
        valor_convertido_in = centimetros_para_polegadas(valor)
    elif unidade_origem == 'Quilômetros':
        valor_convertido = kilometros_para_metros(valor)
        valor_convertido_km = valor
        valor_convertido_in = centimetros_para_polegadas(metros_para_centimetros(kilometros_para_metros(valor)))
    elif unidade_origem == 'Polegadas':
        valor_convertido = polegadas_para_centimetros(valor)
        valor_convertido_km = metros_para_kilometros(polegadas_para_centimetros(valor))
        valor_convertido_in = valor

    # Exibir resultado da conversão
    st.write(f'Valor em {unidade_origem}: {valor}')
    st.write(f'Valor em Metros: {valor_convertido:.2f}')
    st.write(f'Valor em Quilômetros: {valor_convertido_km:.2f}')
    st.write(f'Valor em Polegadas: {valor_convertido_in:.2f}')

if __name__ == '__main__':
    main()
