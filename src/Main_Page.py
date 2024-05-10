import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Main Page",
)


tabela_notas = st.file_uploader("Insira a tabela:", ".xlsx")
def load_data():
    if tabela_notas is not None:
        notas = pd.read_excel(tabela_notas, skiprows=[1])
        notas = notas.round(1)
        return notas

st.write("# Bem-vindos as suas estatisticas")

st.sidebar.info("Selecione o que deseja ver")

notas = load_data()

st.dataframe(notas, hide_index=True)
