import streamlit as st
import pandas as pd
import Utils as ut
from Controllers.PadraoController import *
from models.Aluno import *

class AlunoDAO:
    # Função para adicionar um novo Aluno
    def adicionar_aluno(Escola, Nome, Idade, Classe, Notas):
        Matricula = gerar_nova_matricula(registros_alunos)
        novo_aluno = Aluno(Matricula, Escola, Nome, Idade, Classe, Notas)
        
        if Matricula in registros_alunos:
            ut.Erro(f"Erro: Já existe um aluno com a matrícula {Matricula}.") 
        else:
            registros_alunos[Matricula] = {
                "Matrícula": novo_aluno.Matricula,
                "Escola": novo_aluno.Escola,
                "Nome": novo_aluno.Nome,
                "Idade": novo_aluno.Idade,
                "Classe": novo_aluno.Classe,
                "Notas": novo_aluno.Notas
            }
            ut.Sucesso(f"Sucesso: Aluno {Nome} adicionado com sucesso!")  

    # Função para listar todos os alunos ou usando um filtro
    def listar_alunos(pEscola=None, pMatricula=None, pClasse='Todas', pDisciplina='Todas', pDesempenho=None):
        if not registros_alunos:
            return pd.DataFrame()  # Retorna um DataFrame vazio se não houver alunos
        
        # Criar um DataFrame
        df = pd.DataFrame.from_dict(registros_alunos, orient='index')

        # Expandir a coluna 'Notas'
        Notas_df = df['Notas'].apply(pd.Series)

        # Concatenar o DataFrame original com o DataFrame de Notas
        df = pd.concat([df.drop(columns=['Notas']), Notas_df], axis=1)
        
        # Convertendo as notas para float antes da formatação
        for col in Notas_df.columns:
            df[col] = df[col].astype(float)
        
        # Aplicar os filtros
        df_filtrado = df.copy()
        
        if pMatricula is not None and pMatricula != 0:
            df_filtrado = df_filtrado[df_filtrado['Matrícula'] == int(pMatricula)]
        
        if pEscola:
            df_filtrado = df_filtrado[df_filtrado['Escola'].str.lower().str.contains(pEscola.lower())]

        # Filtrar por classe
        if pClasse and pClasse != 'Todas':
            df_filtrado = df_filtrado[df_filtrado['Classe'].str.lower().str.startswith(pClasse.lower())]

        # Filtrar por matéria e desempenho
        if pDisciplina and pDisciplina != 'Todas' and pDesempenho is not None:
            if pDisciplina not in df_filtrado.columns:
                ut.Informacao("", f"Matéria '{pDisciplina}' não encontrada.")
                return pd.DataFrame()
            df_filtrado = df_filtrado[df_filtrado[pDisciplina] >= float(pDesempenho)]

        # Formatar as colunas de notas com 2 casas decimais
        notas_cols = Notas_df.columns
        for col in notas_cols:
            if col in df_filtrado.columns:
                df_filtrado.fillna(0, inplace=True)  # Preencher NaN com zero
                df_filtrado[col] = df_filtrado[col].apply(lambda x: f'{x:.2f}')
        
        return df_filtrado

    # Adicionar Notas pelo Nome do aluno e a Matéria
    def adicionar_notas(Matricula, Materia, Nota):
        if Nota < 0 or Nota > 100:
            ut.Erro("", "Nota deve estar entre 0 e 100.")
            return False
        
        if not Matricula:
            ut.Erro("", "A matrícula não pode ser vazia.")
            return False
        
        try:
            matricula_int = int(Matricula)  # Convertendo a matrícula para inteiro
        except ValueError:
            ut.Erro("", "A matrícula deve ser um número inteiro.")
            return False
        
        if matricula_int not in registros_alunos:
            ut.Erro("", "Matrícula não encontrada.")
            return False
        
        aluno = registros_alunos[matricula_int]
        aluno["Notas"][Materia] = Nota  # Adiciona ou atualiza a nota
        ut.Sucesso("", "Nota adicionada com sucesso!")
        return True

    # Função para alterar dados de um aluno 
    def alterar_aluno(Matricula, Escola=None, Nome=None, Idade=None, Classe=None, Notas=None):
        if Matricula not in registros_alunos:
            ut.Erro("", "Matrícula não encontrada.")
            return False
        
        aluno = registros_alunos[Matricula]
        
        if Escola:
           aluno["Escola"] = Escola 
        if Nome:
            aluno["Nome"] = Nome
        if Idade:
            aluno["Idade"] = Idade
        if Classe:
            aluno["Classe"] = Classe
        if Notas:
            aluno["Notas"].update(Notas)  # Atualiza as notas existentes ou adiciona novas
        
        ut.Sucesso("", "Dados do aluno atualizados com sucesso!")
        return True

    def deletar_aluno(Matricula: int) -> bool:
        try:
            st.write(Matricula)
            matricula_int = int(Matricula)  # Convertendo a matrícula para inteiro
        except ValueError:
            ut.Erro("", "A matrícula deve ser um número inteiro.")
            return False
        
        if matricula_int in registros_alunos:
            del registros_alunos[matricula_int]
            ut.Sucesso('', f'Matrícula "{Matricula}" deletada com sucesso') 
            return True
        
        if matricula_int not in registros_alunos:
            ut.Erro('', f'Matrícula "{Matricula}" não encontrada.') 
            return False
