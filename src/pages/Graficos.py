import streamlit as st
from Turma import Turma
from Tabs import Tabs

st.set_page_config(
    page_title="Graficos"
)
"# Graficos"

tabs = Tabs()

notas = st.session_state['notas']

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

for i in range(len(tab_list)):
    with tab_list[i]:
        turma = Turma()
        turma.set_turma_id(i)

        if tipos_selecionados == [] and opcoes_selecionadas == []:
            st.warning("Por favor selecione pelo menos uma materia e um dos tipos de avaliacao")
        elif len(tipos_selecionados) > 0 and opcoes_selecionadas == []:
            st.warning("Por favor selecione pelo menos uma materia")
        elif len(tipos_selecionados) == 1 and len(opcoes_selecionadas) == 1:
            st.warning("Por favor selecione mais materias ou mais tipos de avaliacao") 
        else:
            "## Grafico Geral"
            "---"
            st.line_chart(turma.get_dataframe(tipos_selecionados, opcoes_selecionadas), x="NOME")