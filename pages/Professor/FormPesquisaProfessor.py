import streamlit as st
from Controllers.PadraoController import *
from Controllers.ProfessorController import *
import streamlit_antd_components as sac
import Utils as ut

# Inicializa o estado
if 'Escola' not in st.session_state:
    st.session_state.Escola = None

if 'opcoes_professores' not in st.session_state:
    st.session_state.opcoes_professores = []

if 'Classe' not in st.session_state:
    st.session_state.Classe = None
    
if 'Disciplina' not in st.session_state:
    st.session_state.Disciplina = 'Todas'
    
def Form_PesquisaProfessor():
    ut.Divisor('Pesquisar Professor', 'search', 'rgb(20,80,90)', 'key_Professor01')

    with st.container():
        row_0_col0, row_0_col1, row_0_col2, row_0_col3 = st.columns([2, 3, 2.5, 3])

        with row_0_col0:
            # Seleção da escola fora do formulário
            escola_selecionada = st.selectbox("Escola", opcoes_escola, index=None if st.session_state.Suporte else opcoes_escola.index(st.session_state.Escola_L) if st.session_state.Escola_L in opcoes_escola else None, placeholder='Selecione uma escola...', key='Escola_Selectbox', disabled= not st.session_state.Suporte)
            # Atualiza as opções de professores com base na escola selecionada
            if escola_selecionada != st.session_state.Escola:
                st.session_state.Escola = escola_selecionada
                escola_selecionada = st.session_state.Escola.split(" - ", 1)[-1] if st.session_state.Escola else None
                st.session_state.opcoes_professores = carregar_opcoes_professores(escola_selecionada)

        with row_0_col1:
            # Configura o selectbox com as opções e o índice definido
            professor = st.selectbox('Professor(a)', st.session_state.opcoes_professores, index=None, placeholder='Selecione um Professor(a)...', key='Professor_Selectbox')
            # Inicializa a variável Matricula com None
            Matricula = None
            # Recupera a matrícula do professor selecionado
            if professor:
                # Divide a string na posição do primeiro espaço em branco
                Matricula = professor.split(' ', 1)[0] if isinstance(professor, str) else None
                
        with row_0_col2:
            st.session_state.Classe = st.selectbox('Classe', classe_p, index=0, placeholder='Selecione a classe...')
        
        with row_0_col3:
            st.session_state.Disciplina = st.selectbox('Disciplina', disciplinas_p, index=0, placeholder='Selecione uma Matéria...')
        
        row_1_col1, row_1_col2 = st.columns([8, 0.01])
        row_2_col1, row_2_col2, row_2_col3, row_2_col4, row_2_col5 = st.columns([3, 3, 2, 3, 3])
        
        with row_1_col1:
            sac.menu([sac.MenuItem(type='divider')], color='rgb(20,80,90)', open_all=False, return_index=False, index=None, key='key_divisor')
        
        with row_1_col2:   
            st.write('')
        
        with row_2_col1:   
            st.write('')
        
        with row_2_col2:
            st.write('')   
        
        with row_2_col3: 
            # Botão para pesquisar
            form_submit_button_pesquisar = st.button('Pesquisar')
        
        with row_2_col4: 
            st.write('') 
        
        with row_2_col5: 
            st.write('')  
    
    if form_submit_button_pesquisar:
        if 'Escola' in st.session_state and st.session_state.Escola:
            Escola = st.session_state.Escola.split(" - ", 1)[-1]
        else:
            Escola = None

        # Chama a função listar_professor com os filtros selecionados
        df_filtrado = ProfessorDAO.listar_professor(Escola, Matricula, st.session_state.Classe, st.session_state.Disciplina)
        # Mostra os professores filtrados em um DataFrame do Pandas
        if not df_filtrado.empty:                
            styled_df = df_filtrado.style.applymap(style_df_notas)
            st.write(styled_df.to_html(), unsafe_allow_html=True)
        else:
            st.write("Não há professores correspondentes aos filtros selecionados.")
    
    ut.Divisor('Copyright (c) 2024', '', 'rgb(20,80,90)', 'key_Professor02')

