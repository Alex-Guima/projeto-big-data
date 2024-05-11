import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
import matplotlib.pyplot as plt
from Main_Page import conn
from Turma import Turma

st.set_page_config(
    page_title="Graficos"
)
"# Graficos"

notas = conn.read(skiprows=[1])

turma_1 = Turma()
turma_2 = Turma()
turma_3 = Turma()

turma_1.add_alunos(notas["NOME"][:13])
turma_2.add_alunos(notas["NOME"][13:35])
turma_3.add_alunos(notas["NOME"][35:52]) 

opcoes_selecionadas = st.multiselect("Escolha as materias que deseja ver:",
        Turma.materias,
        ['ARTE'],
        placeholder="Escolha suas materias",
        )

tipos_selecionados = st.multiselect("Escolha a modalidade de avaliacao:",
        Turma.tipos,
        ['Media', 'Prova', 'Teste'],
        placeholder="Escolha sua modalidade de avaliacao",
        )

tab1, tab2, tab3 = st.tabs(["Turma 1", "Turma 2", "Turma 3"])

with tab1:
    if tipos_selecionados == [] and opcoes_selecionadas == []:
        st.warning("Por favor selecione pelo menos uma materia e um dos tipos de avaliacao")
    elif len(tipos_selecionados) == 1 and len(opcoes_selecionadas) == 1:
        st.warning("Por favor selecione mais materias ou mais tipos de avaliacao") 
    else:
        "## Grafico Geral"
        "---"
        st.line_chart(turma_1.get_dataframe(tipos_selecionados, opcoes_selecionadas).drop(columns="NOME"))
with tab2:
    if tipos_selecionados == [] and opcoes_selecionadas == []:
        st.warning("Por favor selecione pelo menos uma materia e um dos tipos de avaliacao")
    elif len(tipos_selecionados) == 1 and len(opcoes_selecionadas) == 1:
        st.warning("Por favor selecione mais materias ou mais tipos de avaliacao") 
    else:
        "## Grafico Geral"
        "---"
        st.line_chart(turma_2.get_dataframe(tipos_selecionados, opcoes_selecionadas).drop(columns="NOME"))
        
with tab3:
    if tipos_selecionados == [] and opcoes_selecionadas == []:
        st.warning("Por favor selecione pelo menos uma materia e um dos tipos de avaliacao")
    elif len(tipos_selecionados) == 1 and len(opcoes_selecionadas) == 1:
        st.warning("Por favor selecione mais materias ou mais tipos de avaliacao") 
    else:
        "## Grafico Geral"
        "---"
        st.line_chart(turma_3.get_dataframe(tipos_selecionados, opcoes_selecionadas).drop(columns="NOME"))