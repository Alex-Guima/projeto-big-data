import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from Turma import Turma
from Tabs import Tabs
import plotly.express as px

st.set_page_config(
    page_title="Resultados 1 bim"
)
st.write ("# Media - Primeiro Bimestre")

notas = st.session_state['notas']
tabs = Tabs()
turma = Turma()

if not 'turmas' in st.session_state:
    st.session_state['turmas'] = []


if not 'opcao' in st.session_state:
    st.session_state['opcao'] = ""

if not 'fig' in st.session_state:
    st.session_state['fig'] = []

opcao_selecionada = st.selectbox("Materias",
    Turma.materias,
    placeholder="Materia"
)

def turmas_callback():
    st.session_state['turmas'] = turmas_selecionadas
    

turmas_selecionadas = st.multiselect("Escolha as turmas que deseja ver:",
    Turma.turma_ids,
    1,
    placeholder="Numero da Turma",
    on_change=turmas_callback
)



def create_plotly_graph(opcao_selecionada, turmas_selecionadas):
    dataframe = turma.get_dataframe_by_materia(opcao_selecionada)
    dataframe = dataframe.drop(columns="NOME")
    turma.set_turma_id(turmas_selecionadas)
    opcao_extensao = opcao_selecionada + ".M"
    abaixo_ou_acima_dataframe = pd.DataFrame()
    acima = dataframe[dataframe[opcao_extensao] > 6].count()
    abaixo = dataframe[dataframe[opcao_extensao] < 6].count()
    abaixo_ou_acima_dataframe.insert(0, "Acima", acima)
    abaixo_ou_acima_dataframe.insert(1, "Abaixo", abaixo)
    abaixo_ou_acima_dataframe = abaixo_ou_acima_dataframe.transpose()
    fig = px.pie(abaixo_ou_acima_dataframe,
    values=opcao_extensao,
    names=["Acima", "Abaixo"],
    color_discrete_sequence=px.colors.sequential.Bluered,
    hole=.98,
    labels=['Acima', 'Abaixo'],
    )

    return fig

fig = create_plotly_graph(opcao_selecionada, st.session_state['turmas'])
fig2 = create_plotly_graph(opcao_selecionada, st.session_state['turmas'])
st.plotly_chart(fig2)