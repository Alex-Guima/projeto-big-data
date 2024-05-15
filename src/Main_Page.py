import streamlit as st
import pandas as pd
from streamlit_gsheets import GSheetsConnection
from Turma import Turma

conn = st.connection("gsheets", type=GSheetsConnection)

st.write("# Bem-vindos as suas estatisticas")

st.write("## Upload de Arquivos")
st.info("Caso deseje, faca upload de tabelas aqui")

def file_callback():
    Turma.notas = st.session_state['notas']

uploaded_file = st.file_uploader("Selecione seu Arquivo", 
[".xlsx", ".xls"],
on_change=file_callback
)

if 'uploaded_file' not in st.session_state:
    st.session_state['uploaded_file'] = None
if 'notas' not in st.session_state:
    st.session_state['notas'] = None

if uploaded_file:
    st.session_state['notas'] = pd.read_excel(uploaded_file, skiprows=[1])
    Turma.notas = st.session_state['notas']
else:
    st.session_state['notas'] = conn.read(skiprows=[1])
    Turma.notas = st.session_state['notas']
st.dataframe(st.session_state['notas'], hide_index=True)

st.sidebar.info("Selecione o que deseja ver")

