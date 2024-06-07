import Utils as ut
import pandas as pd 
import streamlit as st
from Controllers.PadraoController import *
from models.Funcionario import *

class FuncionarioDAO():
    
    #  Função para adicionar uma novoFuncionario                    
    def adicionar_funcionario(Escola, Nome, Idade, Cargo):
        Matricula = gerar_nova_matricula(registros_funcionario)
        novo_Funcionario = Funcionario(Matricula, Escola, Nome, Idade, Cargo)
        
        if Matricula in registros_funcionario:
            ut.Erro(f"Erro: Já existe um Funcionário com a matrícula {Matricula}.") 
        else:
            registros_funcionario[Matricula] = {
                "Matrícula": novo_Funcionario.Matricula,
                "Escola": novo_Funcionario.Escola,
                "Nome": novo_Funcionario.Nome,
                "Idade": novo_Funcionario.Idade,
                "Cargo": novo_Funcionario.Cargo
            }
            ut.Sucesso(f"Sucesso: Funcionário {Nome} adicionado com sucesso!")  

    # Função para listar todos os funcionários ou usar um filtro
    def listar_funcionario(pEscola=None, pMatricula=None, pCargo='Todos'):
        if not registros_funcionario:
            return pd.DataFrame()  # Retorna um DataFrame vazio se não houver funcionários

        # Criar um DataFrame
        df = pd.DataFrame.from_dict(registros_funcionario, orient='index')

        # Aplicar os filtros
        df_filtrado = df.copy()

        if pEscola:
            df_filtrado = df_filtrado[df_filtrado['Escola'] == pEscola]

        if pMatricula is not None and pMatricula != 0:
            df_filtrado = df_filtrado[df_filtrado['Matrícula'] == int(pMatricula)]

        # Filtrar por cargo
        if pCargo and pCargo != 'Todos':
            df_filtrado = df_filtrado[df_filtrado['Cargo'] == pCargo]

        return df_filtrado

    # Função para alterar dados de umFuncionario 
    def alterar_Funcionario(Matricula, Escola=None, Nome=None, Idade=None, Classe=None, Cargo=None):
        if Matricula not in registros_funcionario:
            ut.Erro("", "Matrícula não encontrada.")
            return False
        
        Funcionario = registros_funcionario[Matricula]
        
        if Escola:
           Funcionario["Escola"] = Escola 
        if Nome:
           Funcionario["Nome"] = Nome
        if Idade:
           Funcionario["Idade"] = Idade
        if Cargo:
           Funcionario["Cargo"].update(Cargo)  # Atualiza as Cargo existentes ou adiciona novas
        
        ut.Sucesso("", "Dados do Funcionário atualizados com sucesso!")
        return True

    def deletar_Funcionario(Matricula: int) -> bool:
        try:
            st.write(Matricula)
            matricula_int = int(Matricula)  # Convertendo a matrícula para inteiro
        except ValueError:
            ut.Erro("", "A matrícula deve ser um número inteiro.")
            return False
        
        if matricula_int in registros_funcionario:
            del registros_funcionario[matricula_int]
            return True
        
        if matricula_int not in registros_funcionario:
            # ut.Sucesso('', f'Matrícula "{Matricula}" deletada com sucesso') 
            return True