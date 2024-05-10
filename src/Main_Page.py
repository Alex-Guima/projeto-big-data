import streamlit as st
import pandas as pd
from psycopg2 import sql
from sqlalchemy import create_engine

st.set_page_config(
    page_title="Main Page",
)



st.write("# Bem-vindos as suas estatisticas")
conn = create_engine(
    "postgresql+psycopg2://{}:{}@{}:{}/{}".format(st.secrets["username"], st.secrets["password"], st.secrets["host"], st.secrets["port"], st.secrets["database"])
)

uploaded_files = st.file_uploader("Insira um arquivo excel:", ".xlsx")

if uploaded_files != None:
    notas = pd.read_excel(uploaded_files, skiprows=[1])
    notas.to_sql("notas_alunos", conn, if_exists="replace", index=True)
    st.dataframe(notas, hide_index=True)
else:
    notas = None
    st.warning("Insira algum arquivo")

st.sidebar.info("Selecione o que deseja ver")



