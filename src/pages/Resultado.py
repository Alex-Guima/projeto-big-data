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

turma = Turma()

dataframe = turma.get_dataframe_by_materia(opcoes_selecionadas)
dataframe = dataframe.drop(columns="NOME")
for opcao in opcoes_selecionadas:
    opcao_extensao = opcao + ".M"
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
    labels=['Acima', 'Abaixo']
    )
    st.plotly_chart(fig)
