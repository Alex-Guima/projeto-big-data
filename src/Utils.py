import streamlit as st
import pandas as pd
from streamlit_gsheets import GSheetsConnection


class Utils:
    conn = st.connection("gsheets", type=GSheetsConnection)

    def initialize_session_state(self, uploaded_file):
        if 'notas' not in st.session_state:
            st.session_state['notas'] = ''

        if uploaded_file != None:
            notas = pd.read_excel(uploaded_file, skiprows=[1])
            notas = notas.round(1)
            st.session_state['notas'] = notas
            session_state = st.session_state['notas']
            return session_state
        else:
            notas = self.conn.read(skiprows=[1])
            st.session_state['notas'] = notas
            session_state = st.session_state['notas']
            return session_state
