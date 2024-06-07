import streamlit as st
from Controllers.PadraoController import *
from Controllers.AlunoController import *
import streamlit_antd_components as sac
import Utils as ut

if 'opcoes_alunos' not in st.session_state:
    st.session_state.opcoes_alunos = []

if 'Escola' not in st.session_state:
    st.session_state.Escola = None
        
if 'Aluno' not in st.session_state:
    st.session_state.Aluno = None
    
if 'Disciplina' not in st.session_state:
    st.session_state.Disciplina = 'Todas'

if 'Nota' not in st.session_state:
    st.session_state.Nota = 0

def Form_Lancar_Notas():  
    
    ut.Divisor('Lançar Notas dos Alunos', 'graph-up-arrow', 'rgb(20,80,90)', 'LancarNotas01')
    
    with st.container(): 
        row_0_col0, row_0_col1, row_0_col2, row_0_col3 = st.columns([2, 3, 3, 2]) 
        row_2_col1, row_2_col2, row_2_col3, row_2_col4, row_2_col5 = st.columns([3, 3, 2, 3, 3])
  
        # Linha 00
        with row_0_col0:
            # Seleção da escola fora do formulário
            escola_selecionada = st.selectbox("Escola", opcoes_escola, index=None if st.session_state.Suporte else opcoes_escola.index(st.session_state.Escola_L) if st.session_state.Escola_L in opcoes_escola else None, placeholder='Selecione uma escola...', key='Escola_Selectbox', disabled= not st.session_state.Suporte)
            # Atualiza as opções de Alunos
            if escola_selecionada != st.session_state.Escola:
                st.session_state.Escola = escola_selecionada
                escola_selecionada = st.session_state.Escola.split(" - ", 1)[-1] if st.session_state.Escola else None
                st.session_state.opcoes_alunos = carregar_opcoes_alunos(escola_selecionada)
          
        with row_0_col1:
            st.session_state.Aluno = st.selectbox('Aluno(a)', st.session_state.opcoes_alunos, index=None, placeholder='Selecione um Aluno(a)...', key='Aluno_Selectbox')
            if not st.session_state.Aluno:
                st.error('O campo "Aluno(a)" é obrigatório.')
                
        # Linha 01        
        with row_0_col2:
            Disciplina = st.selectbox('Disciplina', disciplinas_p, index=0, placeholder='Selecione uma Disciplina...')
            if Disciplina != st.session_state.Disciplina:
                st.session_state.Disciplina = Disciplina
                if Disciplina == 'Todas':
                    st.session_state.Nota = 0     
                    st.error('O campo "Disciplina" não pode ser "Todas" para salvar uma nota.')  
        
        with row_0_col3:   
            st.session_state.Nota = st.number_input("Nota", step=1, min_value=0, max_value=100, value=0 if Disciplina == 'Todas' else st.session_state.Nota, disabled=(Disciplina == 'Todas')) 
            if st.session_state.Disciplina != 'Todas' and st.session_state.Nota == 0:
                st.error('O campo "Nota" deve ser maior que 0.')
            
        # Linha 02
        with row_2_col1:   
            st.write('')
        
        with row_2_col2:
           st.write('')   
            
        with row_2_col3: 
            selected_lancar_nota = sac.buttons([
                 sac.ButtonsItem(label='Salvar Nota', icon='clipboard-check', color='#25C3B0'),
                 ], label=' . ', align='center', radius='lg', color='rgb(20,80,90)', index=None)
            
        with row_2_col4: 
            st.write('') 
        
        with row_2_col5: 
            st.write('') 
                    
        ut.Divisor('Listar as Notas Lançadas', 'clipboard2-data', 'rgb(20,80,90)', 'LancarNotas02')
        
        if 'Escola' in st.session_state and st.session_state.Escola:
            Escola = st.session_state.Escola.split(" - ", 1)[-1]
        else:
            Escola = None
        # Recupera a matrícula do aluno selecionado
        if 'Aluno' in st.session_state and st.session_state.Aluno:
            Matricula = st.session_state.Aluno.split(' ', 1)[0]
        else:
            Matricula = None
        
        if 'Aluno' in st.session_state and st.session_state.Aluno:
            NomeAluno = st.session_state.Aluno.split(" - ", 1)[-1]
        else:
            NomeAluno = None
            
        with st.container(border=True):
            # Chama a função listar_alunos com os filtros selecionados
            df_filtrado = AlunoDAO.listar_alunos(Escola, Matricula, 'Todas', st.session_state.Disciplina, 0)

            # Mostra as notas filtradas em um DataFrame do Pandas
            if not df_filtrado.empty:
                # Obter o DataFrame estilizado
                styled_df = style_df(df_filtrado)
                # Exibir o DataFrame estilizado como HTML
                st.write(styled_df.to_html(), unsafe_allow_html=True)
            else:
                st.write("Não há Notas lançadas.")   
       
    if selected_lancar_nota == 'Salvar Nota':

        if st.session_state.Aluno and st.session_state.Disciplina != 'Todas' and st.session_state.Nota > 0:
            if AlunoDAO.adicionar_notas(Matricula, st.session_state.Disciplina, st.session_state.Nota):
                ut.Sucesso("", f"Nota de {st.session_state.Disciplina} atualizada para {NomeAluno} com sucesso!")
            else:
                ut.Informacao("", "Aluno inválido.")
        else:
            ut.Alerta('', 'Não é possível salvar a nota. Verifique se um aluno está selecionado, a disciplina não é "Todas" e a nota é maior que 0.')
        
    ut.Divisor('Copyright (c) 2024','','rgb(20,80,90)', 'LancarNotas03')
