import streamlit as st

class Tabs:
    def create_tab_list(self):
        tabs = []
        tab_list = []
        for i in range(22):
            tabs.append("Turma " + str(i + 1))
            
        tab_list = st.tabs(tabs)
        return tab_list
