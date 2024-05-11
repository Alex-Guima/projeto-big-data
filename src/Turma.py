import streamlit as st
import numpy as np
import pandas as pd
from Main_Page import notas

class Turma:
    materias = ["ARTE", "FILOSOFIA", "GEOGRAFIA", "HISTÓRIA", 
"LÍNGUA INGLESA", "LÍNGUA PORTUGUESA", "MATEMÁTICA", "QUÍMICA",
"REDAÇÃO", "BIOLOGIA", "FÍSICA" ]

    tipos = ["Media", "Prova", "Teste"]

    def __init__(self):
        self.lista_alunos = []

    def add_alunos(self, alunos):
        for aluno in alunos:
            self.lista_alunos.append(aluno)

    def get_notas(self, tipos, opcoes):
        notas_turma = notas[notas["NOME"].isin(self.lista_alunos)]
        notas_turma = notas_turma.round(2)
        notas_turma = notas_turma.transpose()
        for opcao in opcoes:
            for tipo in tipos:
                yield notas_turma[opcao + self.check_type(tipo)]
    

            

    def check_type(self, tipo):
        tipo = tipo.lower()
        if tipo == "media":
            return ".M"
        elif tipo == "prova":
            return ".P"
        else:
            return ".T"

    def get_dataframe(self, tipo, opcoes):
        df = pd.DataFrame()
        notas = self.get_notas(tipo, opcoes)
        for nota in notas:
            df = pd.concat([df, nota], axis=1)
        return df
        
        


    

    
