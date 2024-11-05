import numpy as np
import pandas as pd

def gerar_csv_dados_ambientais(caminho_csv, num_anos=100):
    # Definir parâmetros de geração de dados
    np.random.seed(42)

    # Geração de variáveis ambientais
    anos = np.arange(1920, 1920 + num_anos)
    temperatura = np.random.uniform(-10, 40, num_anos)  # em graus Celsius
    umidade = np.random.uniform(0, 100, num_anos)  # em porcentagem
    qualidade_ar = np.random.uniform(0, 500, num_anos)  # Índice de Qualidade do Ar (AQI)

    # Criar o DataFrame com os dados fictícios
    dados = pd.DataFrame({
        'Ano': anos,
        'Temperatura': temperatura,
        'Umidade': umidade,
        'Qualidade_Ar': qualidade_ar
    })

    # Salvar o DataFrame como um arquivo CSV
    dados.to_csv(caminho_csv, index=False)
    print(f"Arquivo CSV gerado com sucesso em: {caminho_csv}")

# Exemplo de uso:
caminho_do_csv = 'dados_ambientais.csv'
gerar_csv_dados_ambientais(caminho_do_csv)
