import streamlit as st
import psutil

def obter_info_cpu():
    info_cpu = {
        'Núcleos Físicos': psutil.cpu_count(logical=False),
        'Núcleos Lógicos': psutil.cpu_count(logical=True),
        'Uso da CPU (%)': psutil.cpu_percent(interval=1),
    }
    return info_cpu

def obter_info_memoria():
    info_memoria = {
        'Total de Memória (GB)': round(psutil.virtual_memory().total / (1024**3), 2),
        'Memória Disponível (GB)': round(psutil.virtual_memory().available / (1024**3), 2),
        'Uso da Memória (%)': psutil.virtual_memory().percent,
    }
    return info_memoria

def obter_info_armazenamento():
    info_armazenamento = {
        'Total de Armazenamento (GB)': round(psutil.disk_usage('/').total / (1024**3), 2),
        'Armazenamento Disponível (GB)': round(psutil.disk_usage('/').free / (1024**3), 2),
        'Uso do Armazenamento (%)': psutil.disk_usage('/').percent,
    }
    return info_armazenamento

def main():
    st.title('Monitoramento de Desempenho de Hardware')

    # Obter informações da CPU
    info_cpu = obter_info_cpu()
    st.subheader('Informações da CPU')
    for key, value in info_cpu.items():
        st.write(f'{key}: {value}')

    # Obter informações da memória
    info_memoria = obter_info_memoria()
    st.subheader('Informações de Memória')
    for key, value in info_memoria.items():
        st.write(f'{key}: {value}')

    # Obter informações de armazenamento
    info_armazenamento = obter_info_armazenamento()
    st.subheader('Informações de Armazenamento')
    for key, value in info_armazenamento.items():
        st.write(f'{key}: {value}')

if __name__ == '__main__':
    main()


