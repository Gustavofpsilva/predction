import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error
from joblib import dump

def treinar_modelo_qualidade_ar(caminho_csv, caminho_modelo):
    # Carregar os dados do CSV
    dados = pd.read_csv(caminho_csv)

    # Exibir as primeiras linhas para garantir que os dados foram carregados corretamente
    print("Primeiras linhas dos dados:")
    print(dados.head())

    # Separar as variáveis de entrada (features) e a variável de saída (target)
    X = dados[['Temperatura', 'Umidade']]
    y = dados['Qualidade_Ar']

    # Dividir os dados em conjunto de treino e teste (80% treino, 20% teste)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Instanciar o modelo de Regressão Linear
    modelo = LinearRegression()

    # Treinar o modelo com os dados de treino
    modelo.fit(X_train, y_train)

    # Fazer predições no conjunto de teste
    y_pred = modelo.predict(X_test)

    # Avaliar o modelo
    mae = mean_absolute_error(y_test, y_pred)
    mse = mean_squared_error(y_test, y_pred)
    rmse = mse ** 0.5

    print(f"MAE: {mae:.2f}")
    print(f"MSE: {mse:.2f}")
    print(f"RMSE: {rmse:.2f}")

    # Salvar o modelo treinado em um arquivo .pkl
    dump(modelo, caminho_modelo)
    print(f"Modelo salvo com sucesso em: {caminho_modelo}")

# Exemplo de uso:
caminho_do_csv = 'dados_ambientais.csv'
caminho_do_modelo = 'modelo_qualidade_ar_previsao.pkl'
treinar_modelo_qualidade_ar(caminho_do_csv, caminho_do_modelo)
