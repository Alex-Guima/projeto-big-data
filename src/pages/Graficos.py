import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
import matplotlib.pyplot as plt
from Main_Page import conn
from Turma import Turma
from Tabs import Tabs

st.set_page_config(
    page_title="Graficos"
)
"# Graficos"

notas = conn.read(skiprows=[1])

tabs = Tabs()

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

tab_list = tabs.create_tab_list()

with tab_list[0]:
    turma_0 = Turma()
    turma_0.set_turma_id(0)

    if tipos_selecionados == [] and opcoes_selecionadas == []:
        st.warning("Por favor selecione pelo menos uma materia e um dos tipos de avaliacao")
    elif len(tipos_selecionados) > 0 and opcoes_selecionadas == []:
        st.warning("Por favor selecione pelo menos uma materia")
    elif len(tipos_selecionados) == 1 and len(opcoes_selecionadas) == 1:
        st.warning("Por favor selecione mais materias ou mais tipos de avaliacao") 
    else:
        "## Grafico Geral"
        "---"
        st.line_chart(turma_0.get_dataframe(tipos_selecionados, opcoes_selecionadas), x="NOME")
with tab_list[1]:
    turma_1 = Turma()
    turma_1.set_turma_id(1)
    if tipos_selecionados == [] and opcoes_selecionadas == []:
        st.warning("Por favor selecione pelo menos uma materia e um dos tipos de avaliacao")
    elif len(tipos_selecionados) > 0 and opcoes_selecionadas == []:
        st.warning("Por favor selecione pelo menos uma materia")
    elif len(tipos_selecionados) == 1 and len(opcoes_selecionadas) == 1:
        st.warning("Por favor selecione mais materias ou mais tipos de avaliacao") 
    else:
        "## Grafico Geral"
        "---"
        st.line_chart(turma_1.get_dataframe(tipos_selecionados, opcoes_selecionadas), x="NOME")

with tab_list[2]:
    turma_2 = Turma()
    turma_2.set_turma_id(2)
    if tipos_selecionados == [] and opcoes_selecionadas == []:
        st.warning("Por favor selecione pelo menos uma materia e um dos tipos de avaliacao")
    elif len(tipos_selecionados) > 0 and opcoes_selecionadas == []:
        st.warning("Por favor selecione pelo menos uma materia")
    elif len(tipos_selecionados) == 1 and len(opcoes_selecionadas) == 1:
        st.warning("Por favor selecione mais materias ou mais tipos de avaliacao") 
    else:
        "## Grafico Geral"
        "---"
        st.line_chart(turma_2.get_dataframe(tipos_selecionados, opcoes_selecionadas), x="NOME")

with tab_list[3]:
    turma_3 = Turma()
    turma_3.set_turma_id(3)
    if tipos_selecionados == [] and opcoes_selecionadas == []:
        st.warning("Por favor selecione pelo menos uma materia e um dos tipos de avaliacao")
    elif len(tipos_selecionados) > 0 and opcoes_selecionadas == []:
        st.warning("Por favor selecione pelo menos uma materia")
    elif len(tipos_selecionados) == 1 and len(opcoes_selecionadas) == 1:
        st.warning("Por favor selecione mais materias ou mais tipos de avaliacao") 
    else:
        "## Grafico Geral"
        "---"
        st.line_chart(turma_3.get_dataframe(tipos_selecionados, opcoes_selecionadas), x="NOME")
with tab_list[4]:
    turma_4 = Turma()
    turma_4.set_turma_id(4)
    if tipos_selecionados == [] and opcoes_selecionadas == []:
        st.warning("Por favor selecione pelo menos uma materia e um dos tipos de avaliacao")
    elif len(tipos_selecionados) > 0 and opcoes_selecionadas == []:
        st.warning("Por favor selecione pelo menos uma materia")
    elif len(tipos_selecionados) == 1 and len(opcoes_selecionadas) == 1:
        st.warning("Por favor selecione mais materias ou mais tipos de avaliacao") 
    else:
        "## Grafico Geral"
        "---"
        st.line_chart(turma_4.get_dataframe(tipos_selecionados, opcoes_selecionadas), x="NOME")
with tab_list[5]:
    turma_5 = Turma()
    turma_5.set_turma_id(5)
    if tipos_selecionados == [] and opcoes_selecionadas == []:
        st.warning("Por favor selecione pelo menos uma materia e um dos tipos de avaliacao")
    elif len(tipos_selecionados) > 0 and opcoes_selecionadas == []:
        st.warning("Por favor selecione pelo menos uma materia")
    elif len(tipos_selecionados) == 1 and len(opcoes_selecionadas) == 1:
        st.warning("Por favor selecione mais materias ou mais tipos de avaliacao") 
    else:
        "## Grafico Geral"
        "---"
        st.line_chart(turma_5.get_dataframe(tipos_selecionados, opcoes_selecionadas), x="NOME")
with tab_list[6]:
    turma_6 = Turma()
    turma_6.set_turma_id(6)
    if tipos_selecionados == [] and opcoes_selecionadas == []:
        st.warning("Por favor selecione pelo menos uma materia e um dos tipos de avaliacao")
    elif len(tipos_selecionados) > 0 and opcoes_selecionadas == []:
        st.warning("Por favor selecione pelo menos uma materia")
    elif len(tipos_selecionados) == 1 and len(opcoes_selecionadas) == 1:
        st.warning("Por favor selecione mais materias ou mais tipos de avaliacao") 
    else:
        "## Grafico Geral"
        "---"
        st.line_chart(turma_6.get_dataframe(tipos_selecionados, opcoes_selecionadas), x="NOME")
with tab_list[7]:
    turma_7 = Turma()
    turma_7.set_turma_id(7)
    if tipos_selecionados == [] and opcoes_selecionadas == []:
        st.warning("Por favor selecione pelo menos uma materia e um dos tipos de avaliacao")
    elif len(tipos_selecionados) > 0 and opcoes_selecionadas == []:
        st.warning("Por favor selecione pelo menos uma materia")
    elif len(tipos_selecionados) == 1 and len(opcoes_selecionadas) == 1:
        st.warning("Por favor selecione mais materias ou mais tipos de avaliacao") 
    else:
        "## Grafico Geral"
        "---"
        st.line_chart(turma_7.get_dataframe(tipos_selecionados, opcoes_selecionadas), x="NOME")
with tab_list[8]:
    turma_8 = Turma()
    turma_8.set_turma_id(8)
    if tipos_selecionados == [] and opcoes_selecionadas == []:
        st.warning("Por favor selecione pelo menos uma materia e um dos tipos de avaliacao")
    elif len(tipos_selecionados) > 0 and opcoes_selecionadas == []:
        st.warning("Por favor selecione pelo menos uma materia")
    elif len(tipos_selecionados) == 1 and len(opcoes_selecionadas) == 1:
        st.warning("Por favor selecione mais materias ou mais tipos de avaliacao") 
    else:
        "## Grafico Geral"
        "---"
        st.line_chart(turma_8.get_dataframe(tipos_selecionados, opcoes_selecionadas), x="NOME")
with tab_list[9]:
    turma_9 = Turma()
    turma_9.set_turma_id(9)
    if tipos_selecionados == [] and opcoes_selecionadas == []:
        st.warning("Por favor selecione pelo menos uma materia e um dos tipos de avaliacao")
    elif len(tipos_selecionados) > 0 and opcoes_selecionadas == []:
        st.warning("Por favor selecione pelo menos uma materia")
    elif len(tipos_selecionados) == 1 and len(opcoes_selecionadas) == 1:
        st.warning("Por favor selecione mais materias ou mais tipos de avaliacao") 
    else:
        "## Grafico Geral"
        "---"
        st.line_chart(turma_9.get_dataframe(tipos_selecionados, opcoes_selecionadas), x="NOME")
with tab_list[10]:
    turma_10 = Turma()
    turma_10.set_turma_id(10)
    if tipos_selecionados == [] and opcoes_selecionadas == []:
        st.warning("Por favor selecione pelo menos uma materia e um dos tipos de avaliacao")
    elif len(tipos_selecionados) > 0 and opcoes_selecionadas == []:
        st.warning("Por favor selecione pelo menos uma materia")
    elif len(tipos_selecionados) == 1 and len(opcoes_selecionadas) == 1:
        st.warning("Por favor selecione mais materias ou mais tipos de avaliacao") 
    else:
        "## Grafico Geral"
        "---"
        st.line_chart(turma_10.get_dataframe(tipos_selecionados, opcoes_selecionadas), x="NOME")
with tab_list[11]:
    turma_11 = Turma()
    turma_11.set_turma_id(11)
    if tipos_selecionados == [] and opcoes_selecionadas == []:
        st.warning("Por favor selecione pelo menos uma materia e um dos tipos de avaliacao")
    elif len(tipos_selecionados) > 0 and opcoes_selecionadas == []:
        st.warning("Por favor selecione pelo menos uma materia")
    elif len(tipos_selecionados) == 1 and len(opcoes_selecionadas) == 1:
        st.warning("Por favor selecione mais materias ou mais tipos de avaliacao") 
    else:
        "## Grafico Geral"
        "---"
        st.line_chart(turma_11.get_dataframe(tipos_selecionados, opcoes_selecionadas), x="NOME")
with tab_list[12]:
    turma_12 = Turma()
    turma_12.set_turma_id(12)
    if tipos_selecionados == [] and opcoes_selecionadas == []:
        st.warning("Por favor selecione pelo menos uma materia e um dos tipos de avaliacao")
    elif len(tipos_selecionados) > 0 and opcoes_selecionadas == []:
        st.warning("Por favor selecione pelo menos uma materia")
    elif len(tipos_selecionados) == 1 and len(opcoes_selecionadas) == 1:
        st.warning("Por favor selecione mais materias ou mais tipos de avaliacao") 
    else:
        "## Grafico Geral"
        "---"
        st.line_chart(turma_12.get_dataframe(tipos_selecionados, opcoes_selecionadas), x="NOME")
with tab_list[13]:
    turma_13 = Turma()
    turma_13.set_turma_id(13)
    if tipos_selecionados == [] and opcoes_selecionadas == []:
        st.warning("Por favor selecione pelo menos uma materia e um dos tipos de avaliacao")
    elif len(tipos_selecionados) > 0 and opcoes_selecionadas == []:
        st.warning("Por favor selecione pelo menos uma materia")
    elif len(tipos_selecionados) == 1 and len(opcoes_selecionadas) == 1:
        st.warning("Por favor selecione mais materias ou mais tipos de avaliacao") 
    else:
        "## Grafico Geral"
        "---"
        st.line_chart(turma_13.get_dataframe(tipos_selecionados, opcoes_selecionadas), x="NOME")
with tab_list[14]:
    turma_14 = Turma()
    turma_14.set_turma_id(14)
    if tipos_selecionados == [] and opcoes_selecionadas == []:
        st.warning("Por favor selecione pelo menos uma materia e um dos tipos de avaliacao")
    elif len(tipos_selecionados) > 0 and opcoes_selecionadas == []:
        st.warning("Por favor selecione pelo menos uma materia")
    elif len(tipos_selecionados) == 1 and len(opcoes_selecionadas) == 1:
        st.warning("Por favor selecione mais materias ou mais tipos de avaliacao") 
    else:
        "## Grafico Geral"
        "---"
        st.line_chart(turma_14.get_dataframe(tipos_selecionados, opcoes_selecionadas), x="NOME")
with tab_list[15]:
    turma_15 = Turma()
    turma_15.set_turma_id(15)
    if tipos_selecionados == [] and opcoes_selecionadas == []:
        st.warning("Por favor selecione pelo menos uma materia e um dos tipos de avaliacao")
    elif len(tipos_selecionados) > 0 and opcoes_selecionadas == []:
        st.warning("Por favor selecione pelo menos uma materia")
    elif len(tipos_selecionados) == 1 and len(opcoes_selecionadas) == 1:
        st.warning("Por favor selecione mais materias ou mais tipos de avaliacao") 
    else:
        "## Grafico Geral"
        "---"
        st.line_chart(turma_15.get_dataframe(tipos_selecionados, opcoes_selecionadas), x="NOME")
with tab_list[16]:
    turma_16 = Turma()
    turma_16.set_turma_id(16)
    if tipos_selecionados == [] and opcoes_selecionadas == []:
        st.warning("Por favor selecione pelo menos uma materia e um dos tipos de avaliacao")
    elif len(tipos_selecionados) > 0 and opcoes_selecionadas == []:
        st.warning("Por favor selecione pelo menos uma materia")
    elif len(tipos_selecionados) == 1 and len(opcoes_selecionadas) == 1:
        st.warning("Por favor selecione mais materias ou mais tipos de avaliacao") 
    else:
        "## Grafico Geral"
        "---"
        st.line_chart(turma_16.get_dataframe(tipos_selecionados, opcoes_selecionadas), x="NOME")
with tab_list[17]:
    turma_17 = Turma()
    turma_17.set_turma_id(17)
    if tipos_selecionados == [] and opcoes_selecionadas == []:
        st.warning("Por favor selecione pelo menos uma materia e um dos tipos de avaliacao")
    elif len(tipos_selecionados) > 0 and opcoes_selecionadas == []:
        st.warning("Por favor selecione pelo menos uma materia")
    elif len(tipos_selecionados) == 1 and len(opcoes_selecionadas) == 1:
        st.warning("Por favor selecione mais materias ou mais tipos de avaliacao") 
    else:
        "## Grafico Geral"
        "---"
        st.line_chart(turma_17.get_dataframe(tipos_selecionados, opcoes_selecionadas), x="NOME")
with tab_list[18]:
    turma_18 = Turma()
    turma_18.set_turma_id(18)
    if tipos_selecionados == [] and opcoes_selecionadas == []:
        st.warning("Por favor selecione pelo menos uma materia e um dos tipos de avaliacao")
    elif len(tipos_selecionados) > 0 and opcoes_selecionadas == []:
        st.warning("Por favor selecione pelo menos uma materia")
    elif len(tipos_selecionados) == 1 and len(opcoes_selecionadas) == 1:
        st.warning("Por favor selecione mais materias ou mais tipos de avaliacao") 
    else:
        "## Grafico Geral"
        "---"
        st.line_chart(turma_18.get_dataframe(tipos_selecionados, opcoes_selecionadas), x="NOME")
with tab_list[19]:
    turma_19 = Turma()
    turma_19.set_turma_id(19)
    if tipos_selecionados == [] and opcoes_selecionadas == []:
        st.warning("Por favor selecione pelo menos uma materia e um dos tipos de avaliacao")
    elif len(tipos_selecionados) > 0 and opcoes_selecionadas == []:
        st.warning("Por favor selecione pelo menos uma materia")
    elif len(tipos_selecionados) == 1 and len(opcoes_selecionadas) == 1:
        st.warning("Por favor selecione mais materias ou mais tipos de avaliacao") 
    else:
        "## Grafico Geral"
        "---"
        st.line_chart(turma_19.get_dataframe(tipos_selecionados, opcoes_selecionadas), x="NOME")
with tab_list[20]:
    turma_20 = Turma()
    turma_20.set_turma_id(20)
    if tipos_selecionados == [] and opcoes_selecionadas == []:
        st.warning("Por favor selecione pelo menos uma materia e um dos tipos de avaliacao")
    elif len(tipos_selecionados) > 0 and opcoes_selecionadas == []:
        st.warning("Por favor selecione pelo menos uma materia")
    elif len(tipos_selecionados) == 1 and len(opcoes_selecionadas) == 1:
        st.warning("Por favor selecione mais materias ou mais tipos de avaliacao") 
    else:
        "## Grafico Geral"
        "---"
        st.line_chart(turma_20.get_dataframe(tipos_selecionados, opcoes_selecionadas), x="NOME")
with tab_list[21]:
    turma_21 = Turma()
    turma_21.set_turma_id(21)
    if tipos_selecionados == [] and opcoes_selecionadas == []:
        st.warning("Por favor selecione pelo menos uma materia e um dos tipos de avaliacao")
    elif len(tipos_selecionados) > 0 and opcoes_selecionadas == []:
        st.warning("Por favor selecione pelo menos uma materia")
    elif len(tipos_selecionados) == 1 and len(opcoes_selecionadas) == 1:
        st.warning("Por favor selecione mais materias ou mais tipos de avaliacao") 
    else:
        "## Grafico Geral"
        "---"
        st.line_chart(turma_21.get_dataframe(tipos_selecionados, opcoes_selecionadas), x="NOME")