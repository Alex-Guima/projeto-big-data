import streamlit as st
import pandas as pd
from streamlit_gsheets import GSheetsConnection
from Utils import Utils

utilities = Utils()

st.write("# Bem-vindos as suas estatisticas")

st.write("## Upload de Arquivos")
st.info("Caso deseje, faca upload de tabelas aqui")

def file_uploader_callback():
    st.session_state['notas'] = uploaded_file

uploaded_file = st.file_uploader("Selecione seu Arquivo", [".xlsx", ".xls"], on_change=form_callback())

if 'uploaded_file' not in st.session_state:
    st.session_state['uploaded_file'] = None

if uploaded_file != None:
    st.session_state['uploaded_file'] = uploaded_file

session_state = utilities.initialize_session_state(st.session_state['uploaded_file'])

st.dataframe(session_state, hide_index=True)

st.sidebar.info("Selecione o que deseja ver")

