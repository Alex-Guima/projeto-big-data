import streamlit as st
import numpy as np
import pandas as pd

class Turma:
    materias = ["ARTE", "FILOSOFIA", "GEOGRAFIA", "HISTÓRIA", 
"LÍNGUA INGLESA", "LÍNGUA PORTUGUESA", "MATEMÁTICA", "QUÍMICA",
"REDAÇÃO", "BIOLOGIA", "FÍSICA" ]

    tipos = ["Media", "Prova", "Teste"]

    turma_ids = []
    
    for i in range(22):
        turma_ids.append(i + 1)

    turma_id = 0

    if 'notas' not in st.session_state:
        st.session_state['notas'] = None

    notas = st.session_state['notas']

    def filter_materias(self, opcoes_selecionadas):
        if opcoes_selecionadas in self.materias:
            return True
        else:
            return False

    def set_turma_id(self, turma_id):
        if type(turma_id) == list:
            self.turma_id = []
            for item in turma_id:
                self.turma_id.append(item)
        else:
            self.turma_id = turma_id
    
    def get_turma_id(self):
        return self.turma_id

    def get_notas(self, tipos, opcoes):
        turma = self.get_turma()
        notas = self.notas
        notas_turma = notas[notas["NOME"].isin(turma)]
        notas_turma = notas_turma.round(2)
        for opcao in opcoes:
            for tipo in tipos:
                yield notas_turma[opcao + self.check_type(tipo)]

    def get_notas_by_materia(self, materia):
        turma = self.get_turma()
        notas = self.notas
        notas_turma = notas[notas["NOME"].isin(turma)]
        notas_turma = notas_turma.round(2)
        yield notas_turma[materia + ".M"]

    def check_type(self, tipo):
        tipo = tipo.lower()
        if tipo == "media":
            return ".M"
        elif tipo == "prova":
            return ".P"
        else:
            return ".T"

    def get_dataframe(self, tipo, opcoes):
        notas = self.notas
        turma = self.get_turma()
        df = pd.DataFrame()
        notas = self.get_notas(tipo, opcoes)
        for nota in notas:
            df = pd.concat([df, nota], axis=1)
        df.insert(0,"NOME", turma)
        df.set_index("NOME")
        return df

    def get_dataframe_by_materia(self, materia):
        notas = self.notas
        turma = self.get_turma()
        df = pd.DataFrame()
        notas = self.get_notas_by_materia(materia)
        for nota in notas:
            df = pd.concat([df, nota], axis=1)
        df.insert(0,"NOME", turma)
        df.set_index("NOME")
        return df
        
    def get_turma(self):
        notas = self.notas
        turma_id = self.get_turma_id()
        if type(turma_id) == list:
            for item in turma_id:
                turma_id = item
        match turma_id:
            case 0:
                return notas["NOME"][:13]
            case 1:
                return notas["NOME"][13:35]
            case 2:
                return notas["NOME"][35:52]
            case 3:
                return notas["NOME"][52:74]
            case 4:
                return notas["NOME"][74:91]
            case 5:
                return notas["NOME"][91:124]
            case 6:
                return notas["NOME"][124:191]
            case 7:
                return notas["NOME"][191:226]
            case 8:
                return notas["NOME"][226:261]
            case 9:
                return notas["NOME"][261:304]
            case 10:
                return notas["NOME"][304:349]
            case 11:
                return notas["NOME"][349:392]
            case 12:
                return notas["NOME"][392:434]
            case 13:
                return notas["NOME"][434:469]
            case 14:
                return notas["NOME"][469:504]
            case 15:
                return notas["NOME"][504:539]
            case 16:
                return notas["NOME"][539:583]
            case 17:
                return notas["NOME"][583:624]
            case 18:
                return notas["NOME"][624:637]
            case 19:
                return notas["NOME"][637:655]
            case 20:
                return notas["NOME"][655:674]
            case 21:
                return notas["NOME"][674:708]

    def get_nome_materias(self, df, materias):
        nomes_materias = []
        for col in df:
            nomes_materias.append(col)
        nomes_materias.remove("NOME")
        return nomes_materias

    def filter_nota_by_aluno(self, nome, dataframe): 
        nome = int(nome)
        notas_aluno_especifico = dataframe.iloc[nome]
        return notas_aluno_especifico