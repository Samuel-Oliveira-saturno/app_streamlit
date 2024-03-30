import streamlit as st
import time

# Função para exibir o contador regressivo
def exibir_contador(tempo_total, tipo_contagem):
    while tempo_total:
        minutos, segundos = divmod(tempo_total, 60)
        contador = '{:02d}:{:02d}'.format(minutos, segundos)
        st.write(f'Tempo de {tipo_contagem}: {contador}', end="\r")
        time.sleep(1)
        tempo_total -= 1

# Função principal
def main():
    st.title('Relógio Pomodoro')

    # Configuração dos tempos de trabalho e pausa
    tempo_trabalho = st.number_input('Tempo de trabalho (minutos):', min_value=1)
    tempo_pausa = st.number_input('Tempo de pausa (minutos):', min_value=1)

    # Botão para iniciar o ciclo Pomodoro
    if st.button('Iniciar Ciclo Pomodoro'):
        st.write('Ciclo Pomodoro Iniciado!')
        while True:
            exibir_contador(tempo_trabalho * 60, 'Trabalho')
            st.write('Tempo de pausa! 👀')
            exibir_contador(tempo_pausa * 60, 'Pausa')
            st.write('De volta ao trabalho! 🚀')

if __name__ == '__main__':
    main()
