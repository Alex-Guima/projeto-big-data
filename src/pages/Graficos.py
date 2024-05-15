import streamlit as st
import plotly.express as px
from Turma import Turma
from Tabs import Tabs

st.set_page_config(
    page_title="Graficos"
)
"# Graficos"

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
for i in range(len(tab_list)):
    with tab_list[i]:
        turma = Turma()
        turma.set_turma_id(i)

        dataframe = turma.get_dataframe(tipos_selecionados, opcoes_selecionadas)

        if tipos_selecionados == [] and opcoes_selecionadas == []:
            st.warning("Por favor selecione pelo menos uma materia e um dos tipos de avaliacao")
        elif len(tipos_selecionados) > 0 and opcoes_selecionadas == []:
            st.warning("Por favor selecione pelo menos uma materia")
        elif len(tipos_selecionados) == 1 and len(opcoes_selecionadas) == 1:
            st.warning("Por favor selecione mais materias ou mais tipos de avaliacao") 
        else:
            for opcao in opcoes_selecionadas:
                for tipo in tipos_selecionados:
                    "# Grafico " + tipo + " "  + opcao 
                    opcao_extensao = opcao + turma.check_type(tipo)
                    fig = px.scatter(dataframe,
                    x="NOME",
                    y=dataframe[opcao_extensao],
                    size=dataframe[opcao_extensao],
                    color=dataframe[opcao_extensao],
                    hover_name="NOME"
                    )
                    st.plotly_chart(fig)