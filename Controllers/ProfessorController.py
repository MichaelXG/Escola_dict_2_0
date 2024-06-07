import Utils as ut
import pandas as pd 
import streamlit as st
from Controllers.PadraoController import *
from models.Professor import *

class ProfessorDAO():
    
    def carregar_disciplinas_professor(Matricula_prof):
        for prof_info in registros_professor.values():
            if prof_info["Matrícula"] == int(Matricula_prof):
                return prof_info.get("Disciplinas", [])
        return None
    
    # Função para carregar as classes do professor
    def carregar_classe_professor(Matricula_prof):
        for prof_info in registros_professor.values():
            if prof_info["Matrícula"] == int(Matricula_prof):
                return prof_info.get("Classe", [])
        return None
            
    #  Função para adicionar uma novo Professor                    
    def adicionar_professor(Nome, Idade, Disciplinas):
        Matricula = gerar_nova_matricula(registros_professor)
        novo_Professor = Professor(Matricula, Nome, Idade, Disciplinas)
        
        if Matricula in registros_professor:
            ut.Erro(f"Erro: Já existe um Professor com a matrícula {Matricula}.") 
        else:
            registros_professor[Matricula] = {
                "Matrícula": novo_Professor.Matricula,
                "Nome": novo_Professor.Nome,
                "Idade": novo_Professor.Idade,
                "Disciplinas": novo_Professor.Disciplinas
            }
            ut.Sucesso(f"Sucesso: Professor {Nome} adicionado com sucesso!")  

    # Função para listar todos os professores ou usar um filtro
    def listar_professor(pEscola=None, pMatricula=None, pClasse='Todas', pDisciplina='Todas'):
        if not registros_professor:
            return pd.DataFrame()  # Retorna um DataFrame vazio se não houver Professor

        # Criar um novo dicionário combinando os registros de funcionários e professores
        registros_completos = {}

        for matricula, dados_funcionario in registros_funcionario.items():
            if dados_funcionario['Cargo'] == 'Professor(a)':
                dados_professor = next((dados for dados in registros_professor.values() if dados['Matrícula'] == matricula), None)
                if dados_professor:
                    registro_completo = {
                        'Matrícula': matricula,
                        'Escola': dados_funcionario['Escola'],
                        'Classes': dados_professor['Classe'],
                        'Disciplinas': dados_professor['Disciplinas']
                    }
                    registros_completos[matricula] = registro_completo

        # Criar um DataFrame dos registros completos
        df_completo = pd.DataFrame.from_dict(registros_completos, orient='index')

        # Aplicar os filtros
        df_filtrado = df_completo.copy()
        
        # Filtrar por escola
        if pEscola is not None:
            df_filtrado = df_filtrado[df_filtrado['Escola'] == pEscola]
        
        # Filtrar por matrícula
        if pMatricula is not None and pMatricula != 0:
            df_filtrado = df_filtrado[df_filtrado['Matrícula'] == int(pMatricula)]

        # Filtrar por classe
        if pClasse and pClasse != 'Todas':
            df_filtrado = df_filtrado[df_filtrado['Classes'].apply(lambda x: pClasse in x)]

        # Filtrar por disciplina
        if pDisciplina and pDisciplina != 'Todas':
            df_filtrado = df_filtrado[df_filtrado['Disciplinas'].str.contains(pDisciplina)]

        # Substituir a coluna 'Matrícula' pelo nome do professor correspondente à matrícula
        df_filtrado['Professor(a)'] = df_filtrado['Matrícula'].map(lambda matricula: registros_funcionario[matricula]['Nome'])

        # Remover a coluna 'Matrícula' após substituir pelo nome
        df_filtrado.drop(columns=['Matrícula'], inplace=True)

        # Reordenar as colunas para que 'Professor(a)' seja a primeira
        cols = list(df_filtrado.columns)
        cols = ['Professor(a)'] + [col for col in cols if col != 'Professor(a)']
        df_filtrado = df_filtrado[cols]

        # Renomear a coluna 'Classe' para 'Classe(s)'
        df_filtrado.rename(columns={'Classes': 'Classe(s)'}, inplace=True)
        # Converter a lista de classes em uma string com quebras de linha
        df_filtrado['Classe(s)'] = df_filtrado['Classe(s)'].apply(lambda x: ' \n | \n'.join(x))

        # Expandir a coluna 'Disciplinas' e concatenar todas as disciplinas em uma única coluna
        df_filtrado['Disciplinas'] = df_filtrado['Disciplinas'].apply(lambda x: '\n'.join(x))

        return df_filtrado


    # Adicionar Disciplinas pelo Nome do Professor e a Matéria
    def adicionar_disciplina(Matricula, Materia, Nota):
        if Nota < 0 or Nota > 100:
            ut.Erro("", "Nota deve estar entre 0 e 100.")
            return False
        
        try:
            matricula_int = int(Matricula)  # Convertendo a matrícula para inteiro
        except ValueError:
            ut.Erro("", "A matrícula deve ser um número inteiro.")
            return False
        
        if matricula_int not in registros_professor:
            ut.Erro("", "Matrícula não encontrada.")
            return False
        
        Professor = registros_professor[matricula_int]
        Professor["Disciplinas"][Materia] = Nota  # Adiciona ou atualiza a nota
        # ut.Sucesso("", "Nota adicionada com sucesso!")
        return True

    # Função para alterar dados de um Professor 
    def alterar_Professor(Matricula, Nome=None, Idade=None, Classe=None, Disciplinas=None):
        if Matricula not in registros_professor:
            ut.Erro("", "Matrícula não encontrada.")
            return False
        
        Professor = registros_professor[Matricula]
        
        if Nome:
            Professor["Nome"] = Nome
        if Idade:
            Professor["Idade"] = Idade
        if Classe:
            Professor["Classe"] = Classe
        if Disciplinas:
            Professor["Disciplinas"].update(Disciplinas)  # Atualiza as Disciplinas existentes ou adiciona novas
        
        ut.Sucesso("", "Dados do Professor atualizados com sucesso!")
        return True

    def deletar_professor(Matricula: int) -> bool:
        try:
            st.write(Matricula)
            matricula_int = int(Matricula)  # Convertendo a matrícula para inteiro
        except ValueError:
            ut.Erro("", "A matrícula deve ser um número inteiro.")
            return False
        
        if matricula_int in registros_professor:
            del registros_professor[matricula_int]
            return True
        
        if matricula_int not in registros_professor:
            # ut.Sucesso('', f'Matrícula "{Matricula}" deletada com sucesso') 
            return True