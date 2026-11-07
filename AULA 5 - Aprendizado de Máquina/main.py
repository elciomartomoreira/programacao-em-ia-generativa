import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression

st.header("Previsão de Vendas")

# Dados: [Investimento em Marketing] -> Faturamento
dados_vendas = pd.DataFrame({
    'investimento': [100, 200, 300, 400, 500, 600],
    'faturamento': [1200, 2500, 3200, 4800, 5100, 6300]
})

# objetivo: previsão de FATURAMENTO baseado nos investimentos

modelo_previsao = LinearRegression()
modelo_previsao.fit(dados_vendas[['investimento']], dados_vendas['faturamento'])

h_fatur = st.slider('dados_vendas', 0,600,100)
previsao_faturamento = modelo_previsao.predict([[h_fatur]])

st.metric(
    label="Faturamento Previsto", value=f"R$ {previsao_faturamento[0]:.2f}"
)

print(previsao_faturamento)