import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from Turma import Turma
from Tabs import Tabs
import plotly.express as px

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
        dataframe = turma.get_dataframe_by_materia(opcoes_selecionadas)
        for opcao in opcoes_selecionadas:
            "# Grafico " + opcao
            opcao_extensao = opcao + ".M"
            fig = px.scatter(turma.get_dataframe_by_materia(opcoes_selecionadas),
            x="NOME",
            y=dataframe[opcao_extensao],
            size=dataframe[opcao_extensao],
            color=dataframe[opcao_extensao],
            hover_name="NOME"
            )
            st.plotly_chart(fig)

