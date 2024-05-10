import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
import matplotlib.pyplot as plt
from Main_Page import load_data

st.set_page_config(
    page_title="Graficos"
)

notas = load_data()

tab1, tab2, tab3 = st.tabs(["Turma 1", "Turma 2", "Turma 3"])

lista_alunos = notas['NOME'].unique()

turma_1 = lista_alunos[:13]

turma_2 = lista_alunos[13:35]

turma_3 = lista_alunos[35:52]

materias = ["ARTE", "FILOSOFIA", "GEOGRAFIA", "HISTÓRIA", 
"LÍNGUA INGLESA", "LÍNGUA PORTUGUESA", "MATEMÁTICA", "QUÍMICA",
"REDAÇÃO", "BIOLOGIA", "FÍSICA" ]

notas_turma_1 = notas[notas['NOME'].isin(turma_1)]
notas_turma_2 = notas[notas['NOME'].isin(turma_2)]
notas_turma_3 = notas[notas['NOME'].isin(turma_3)]

media_turma_1 = notas_turma_1.drop(columns='NOME').round(2)
media_turma_2 = notas_turma_2.drop(columns='NOME').round(2)
media_turma_3 = notas_turma_3.drop(columns='NOME').round(2)

def selecionar_opcoes_media(turma):
        opcoes_selecionadas = st.multiselect("Escolha as materias que deseja ver:",
        materias,
        ["ARTE", "BIOLOGIA"],
        placeholder="Escolha suas materias",
        key="medias" + str(turma)
        )
        for i in opcoes_selecionadas:   
            yield i + ".M"

def selecionar_opcoes_prova(turma):
        opcoes_selecionadas = st.multiselect("Escolha as materias que deseja ver:",
        materias,
        ["ARTE", "BIOLOGIA"],
        placeholder="Escolha suas materias",
        key="provas" + str(turma)
        )
        for i in opcoes_selecionadas:   
            yield i + ".P"

def selecionar_opcoes_teste(turma):
        opcoes_selecionadas = st.multiselect("Escolha as materias que deseja ver:",
        materias,
        ["ARTE", "BIOLOGIA"],
        placeholder="Escolha suas materias",
        key="teste" + str(turma)
        )
        for i in opcoes_selecionadas:   
            yield i + ".T"


with tab1:
    st.dataframe(media_turma_1, use_container_width=True)

    "---"
    st.write(" ## Grafico Medias por Materia")
    
    
    grafico_medias = st.line_chart(media_turma_1[selecionar_opcoes_media(turma_1)])
    "---"
    st.write(" ## Grafico Provas por Materia")
    grafico_provas = st.line_chart(media_turma_1[selecionar_opcoes_prova(turma_1)])

    "---"
    st.write("## Grafico Testes por Materia")
    grafico_testes = st.line_chart(media_turma_1[selecionar_opcoes_teste(turma_1)])

with tab2:
    st.dataframe(media_turma_2, use_container_width=True)

    "---"
    st.write(" ## Grafico Medias por Materia")
    
    
    grafico_medias = st.line_chart(media_turma_2[selecionar_opcoes_media(turma_2)])
    "---"
    st.write(" ## Grafico Provas por Materia")
    grafico_provas = st.line_chart(media_turma_2[selecionar_opcoes_prova(turma_2)])

    "---"
    st.write("## Grafico Testes por Materia")
    grafico_testes = st.line_chart(media_turma_2[selecionar_opcoes_teste(turma_2)])


with tab3:
    st.dataframe(media_turma_3, use_container_width=True)

    "---"
    st.write(" ## Grafico Medias por Materia")
    
    
    grafico_medias = st.line_chart(media_turma_3[selecionar_opcoes_media(turma_3)])
    "---"
    st.write(" ## Grafico Provas por Materia")
    grafico_provas = st.line_chart(media_turma_3[selecionar_opcoes_prova(turma_3)])

    "---"
    st.write("## Grafico Testes por Materia")
    grafico_testes = st.line_chart(media_turma_3[selecionar_opcoes_teste(turma_3)])
    "---"