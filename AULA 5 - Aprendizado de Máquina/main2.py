

import pandas as pd
import streamlit as st


dados  = pd.read_excel('dados_2.xlsx')
print(dados)


st.write(dados.head())
st.table(dados)
st.write(dados.describe())


