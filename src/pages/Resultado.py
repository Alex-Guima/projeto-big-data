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


st.write ("# Media - Primeiro Bimestre")

nome = st.text_input("Insira o nome do Aluno (de acordo com a tabela)")

if nome:
    turma = Turma()
    dataframe = turma.get_dataframe_by_materia(opcoes_selecionadas)
    notas_aluno_especifico = turma.filter_nota_by_aluno(nome, dataframe)
    notas_aluno_especifico
else:
    st.warning("Por favor insira um nome")
        
