import streamlit as st
import pandas as pd
from Main_Page import load_data
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="Resultados 1 bim"
)
notas = load_data()
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


turma_1 = lista_alunos.iloc[0:12]
turma_1




fig, ax = plt.subplots()
ax.pie(turma_1["ARTE.T"])

st.pyplot(fig)
