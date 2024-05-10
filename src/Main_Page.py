import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Main Page",
)

@st.cache_resource
def load_data():
    notas = pd.read_excel("data/TrabalhoBigB1.xlsx", skiprows=[1])
    notas = notas.round(1)
    return notas

st.write("# Bem-vindos as suas estatisticas")

st.sidebar.info("Selecione o que deseja ver")

notas = load_data()

st.dataframe(notas, hide_index=True)
