import Utils as ut
import pandas as pd 
import streamlit as st
from Controllers.PadraoController import *
from models.Escola import *

class EscolaDAO():
    #  Função para adicionar uma novo Escola                    
    def adicionar_Escola(CodEscola, Nome):
        CodEscola = gerar_nova_matricula(registros_escola)
        noca_escola = Escola(CodEscola, Nome)
        
        if CodEscola in registros_escola:
            ut.Erro(f"Erro: Já existe um Escola com a matrícula {CodEscola}.") 
        else:
            registros_escola[CodEscola] = {
                "Cód. Escola": noca_escola.CodEscola,
                "Nome": noca_escola.Nome,
            }
            ut.Sucesso(f"Sucesso: Escola {Nome} adicionado com sucesso!")  

    # Função para listar todos os Escolas ou usando um filtro
    def listar_escola(pCodEscola=None, pNome=None):
        if not registros_escola:
            return pd.DataFrame()  # Retorna um DataFrame vazio se não houver Escolas
            
        # Criar um DataFrame
        df = pd.DataFrame.from_dict(registros_escola, orient='index')
        
        # Aplicar os filtros
        df_filtrado = df.copy()
        
        if pCodEscola is not None and pCodEscola != 0:
            df_filtrado = df_filtrado[df_filtrado['Cód. Escola'] == pCodEscola]
        
        if pNome:
            # Escolas que começam com a string de busca
            inicio = df_filtrado[df_filtrado['Nome'].str.lower().str.startswith(pNome.lower())]
            # Escolas que contêm a string de busca
            contem = df_filtrado[df_filtrado['Nome'].str.lower().str.contains(pNome.lower())]
            # Remover duplicatas mantendo a ordem
            df_filtrado = pd.concat([inicio, contem]).drop_duplicates().reset_index(drop=True)

        return df_filtrado


    # Adicionar Notas pelo Nome do Escola e a Matéria
    def adicionar_notas(CodEscola, Materia, Nota):
        if Nota < 0 or Nota > 100:
            ut.Erro("", "Nota deve estar entre 0 e 100.")
            return False
        
        try:
            CodEscola_int = int(CodEscola)  # Convertendo a matrícula para inteiro
        except ValueError:
            ut.Erro("", "A matrícula deve ser um número inteiro.")
            return False
        
        if CodEscola_int not in registros_escola:
            ut.Erro("", "Matrícula não encontrada.")
            return False
        
        Escola = registros_escola[CodEscola_int]
        Escola["Notas"][Materia] = Nota  # Adiciona ou atualiza a nota
        # ut.Sucesso("", "Nota adicionada com sucesso!")
        return True

    # Função para alterar dados de um Escola 
    def alterar_Escola(CodEscola, Nome=None, Idade=None, Classe=None, Notas=None):
        if CodEscola not in registros_escola:
            ut.Erro("", "Matrícula não encontrada.")
            return False
        
        Escola = registros_escola[CodEscola]
        
        if Nome:
            Escola["Nome"] = Nome
        if Idade:
            Escola["Idade"] = Idade
        if Classe:
            Escola["Classe"] = Classe
        if Notas:
            Escola["Notas"].update(Notas)  # Atualiza as notas existentes ou adiciona novas
        
        ut.Sucesso("", "Dados do Escola atualizados com sucesso!")
        return True

    def deletar_Escola(CodEscola: int) -> bool:
        try:
            st.write(CodEscola)
            CodEscola_int = int(CodEscola)  # Convertendo a matrícula para inteiro
        except ValueError:
            ut.Erro("", "A matrícula deve ser um número inteiro.")
            return False
        
        if CodEscola_int in registros_escola:
            del registros_escola[CodEscola_int]
            return True
        
        if CodEscola_int not in registros_escola:
            # ut.Sucesso('', f'Matrícula "{CodEscola}" deletada com sucesso') 
            return True