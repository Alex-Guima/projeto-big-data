import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="Resultados 1 bim"
)

notas = st.session_state['notas']

st.write ("# Turma 1 - medias 1 bim")

lista_alunos = notas[["ARTE.T", 
"FILOSOFIA.T",
'GEOGRAFIA.T',
'HISTÓRIA.T',
'LÍNGUA INGLESA.T',
'LÍNGUA PORTUGUESA.T',
'MATEMÁTICA.T',
'QUÍMICA.T',
'REDAÇÃO.T',
'BIOLOGIA.T',
'FÍSICA.T',
]]

mylabels = ["ARTE.T", 
"FILOSOFIA.T",
'GEOGRAFIA.T',
'HISTÓRIA.T',
'LÍNGUA INGLESA.T',
'LÍNGUA PORTUGUESA.T',
'MATEMÁTICA.T',
'QUÍMICA.T',
'REDAÇÃO.T',
'BIOLOGIA.T',
'FÍSICA.T'
]


turma_1 = lista_alunos.iloc[:13]
turma_1




fig, ax = plt.subplots()
ax.pie(turma_1["ARTE.T"])

st.pyplot(fig)
