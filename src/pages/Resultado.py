import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from Turma import Turma
from Tabs import Tabs
import pyplot.express as px

st.set_page_config(
    page_title="Resultados 1 bim"
)

notas = st.session_state['notas']
tabs = Tabs()

opcoes_selecionadas = st.multiselect("Escolha as materias que deseja ver:",
        Turma.materias,
        ['ARTE'],
        placeholder="Escolha suas materias",
        )


st.write ("# Turma 1 - medias 1 bim")

tab_list = tabs.create_tab_list()

for i in range(len(tab_list)):
    with tab_list[i]:
        turma = Turma()
        turma.set_turma_id(i)
        
        fig= px.scatter(
            df.query(turma.get_dataframe_by_materia(opcoes_selecionadas)),
            size=turma.get_notas_by_materias(opcoes_selecionadas)
        ) 

        st.

nomes_materias = turma.get_nome_materias(turma.get_dataframe_by_materia(opcoes_selecionadas), opcoes_selecionadas)

dataframe = turma.get_dataframe_by_materia(opcoes_selecionadas)

fig = px.scatter(
    dataframe.query(nomes_materias < 6),
    x=nomes_materias,
    y="Nota"

)