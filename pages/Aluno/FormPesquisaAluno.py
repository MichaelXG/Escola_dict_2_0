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

if 'Desempenho' not in st.session_state:
    st.session_state.Desempenho = 0
    
def Form_PesquisaAluno():  

    ut.Divisor('Pesquisar Alunos', 'search', 'rgb(20,80,90)', 'key_Alunos01')

    with st.container():  
        row_0_col0, row_0_col1, row_0_col2, row_0_col3, row_0_col4 = st.columns([2, 3, 3, 3, 2])   
        row_1_col1, row_1_col2 = st.columns([8, 0.01]) 
        row_2_col1, row_2_col2, row_2_col3, row_2_col4, row_2_col5= st.columns([3, 3, 2, 3, 3])
         
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
            # Configura o selectbox com as opções e o índice definido
            st.session_state.Aluno = st.selectbox('Aluno(a)', st.session_state.opcoes_alunos, index=None, placeholder='Selecione um Aluno(a)...', key='Aluno_Selectbox')
            
        with row_0_col2:
            st.session_state.Classe = st.selectbox('Classe', classe_p, index=0, placeholder='Seleciona a classe...')
        
        with row_0_col3:
            Disciplina = st.selectbox('Disciplina', disciplinas_p, index=0, placeholder='Seleciona uma Disciplina...')
            if Disciplina != st.session_state.Disciplina:
                st.session_state.Disciplina = Disciplina
                if Disciplina == 'Todas':
                    st.session_state.Desempenho = 0

        with row_0_col4:
            st.session_state.Desempenho = st.number_input("Desempenho", min_value=0, max_value=100, value= 0 if Disciplina == 'Todas' else st.session_state.Desempenho, disabled=(Disciplina == 'Todas'))

        with row_1_col1:
            sac.menu([sac.MenuItem(type='divider')], color='rgb(20,80,90)', open_all=False, return_index=False, index=None, key='key_divisor')
        with row_1_col2:   
            st.write('')
       
        # Linha 02
        with row_2_col1:   
            st.write('')
        
        with row_2_col2:
           st.write('')   
            
        with row_2_col3: 
            form_submit_button_peqsuisar = st.button('Pesquisar')            
        with row_2_col4: 
            st.write('') 
        
        with row_2_col5: 
            st.write('') 
            
        if form_submit_button_peqsuisar:
            if 'Escola' in st.session_state and st.session_state.Escola:
                Escola = st.session_state.Escola.split(" - ", 1)[-1]
            else:
                Escola = None

            # Recupera a matrícula do aluno selecionado
            if 'Aluno' in st.session_state and st.session_state.Aluno:
                Matricula = st.session_state.Aluno.split(' ', 1)[0]
            else:
                Matricula = None
                
            # Chama a função listar_Alunos com os filtros selecionados
            df_filtrado = AlunoDAO.listar_alunos(Escola, Matricula, st.session_state.Classe, Disciplina, st.session_state.Desempenho)
            # Mostra as Alunos filtradas em um DataFrame do Pandas
            if not df_filtrado.empty:
                # Obter o DataFrame estilizado
                styled_df = style_df(df_filtrado)
                # Exibir o DataFrame estilizado como HTML
                st.write(styled_df.to_html(), unsafe_allow_html=True)
            else:
                st.write("Não há Alunos correspondentes aos filtros selecionados.")        
         
    ut.Divisor('Copyright (c) 2024','','rgb(20,80,90)', 'key_Alunos02')