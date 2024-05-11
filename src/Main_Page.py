import streamlit as st
import pandas as pd
from streamlit_gsheets import GSheetsConnection

st.set_page_config(
    page_title="Main Page",
)

st.write("# Bem-vindos as suas estatisticas")
conn = st.connection("gsheets", type=GSheetsConnection)
notas = conn.read(skiprows=[1])
st.dataframe(notas, hide_index=True)

st.sidebar.info("Selecione o que deseja ver")



