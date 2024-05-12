import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from Turma import Turma

st.set_page_config(
    page_title="Resultados 1 bim"
)

notas = st.session_state['notas']

turma = Turma()
turma.set_turma_id(0)

opcoes_selecionadas = st.multiselect("Escolha as materias que deseja ver:",
        Turma.materias,
        ['ARTE'],
        placeholder="Escolha suas materias",
        )


st.write ("# Turma 1 - medias 1 bim")

nomes_materias = turma.get_nome_materias(turma.get_dataframe_by_materia(opcoes_selecionadas), opcoes_selecionadas)

dataframe = turma.get_dataframe_by_materia(opcoes_selecionadas)
comparison_list = []

for nome in nomes_materias:
    comparison_list.append(dataframe[nome] < 6)
    
contagem = sum(comparison_list)

contagem_falsos = len(comparison_list) - contagem

fig, ax = plt.subplots()
ax.pie(contagem_falsos)
st.pyplot(fig)