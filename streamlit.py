import streamlit as st
import numpy as np
from joblib import load

# Carregar o modelo treinado
modelo = load('modelo_previsao.pkl')

st.title('Previsão da Qualidade do Ar')

st.write("""
Este software permite que você insira dados de temperatura e umidade para obter uma previsão da qualidade do ar com base no modelo treinado.
""")

# Entradas do usuário
temperatura = st.number_input('Temperatura (°C)', min_value=-50.0, max_value=50.0, value=25.0, step=0.1)
umidade = st.number_input('Umidade (%)', min_value=0.0, max_value=100.0, value=50.0, step=0.1)

# Botão para fazer previsão
if st.button('Fazer Previsão'):
    # Criar a entrada de dados para o modelo
    dados_entrada = np.array([[temperatura, umidade]])

    # Fazer a previsão
    previsao = modelo.predict(dados_entrada)

    # Exibir o resultado
    st.write(f'Previsão de Qualidade do Ar (AQI): {previsao[0]:.2f}')
