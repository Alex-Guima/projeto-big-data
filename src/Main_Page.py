import streamlit as st
import pandas as pd
from sqlalchemy import create_engine

st.set_page_config(
    page_title="Main Page",
)

conn = create_engine("postgresql+psycopg2://{}:{}@{}/{}".format(st.secrets["username"], st.secrets["password"], st.secrets["host"], st.secrets["database"]))

uploaded_file = st.file_uploader("Insira um arquivo:", ".xlsx")
def load_data():
    if uploaded_file is not None:
        notas = pd.read_excel(uploaded_file, skiprows=[1])
        notas = notas.round(1)
        notas.to_sql("notas_alunos", conn, if_exists="replace")
        return notas
    else:
        notas = pd.read_sql("notas_alunos", conn)
        return notas

notas = load_data()

st.write("# Bem-vindos as suas estatisticas")

st.sidebar.info("Selecione o que deseja ver")

st.dataframe(notas, hide_index=True)
