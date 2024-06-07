import streamlit as st
from Controllers.PadraoController import *
from Controllers.FuncionarioController import *
import streamlit_antd_components as sac
import Utils as ut
    
# Inicializa o estado
if 'opcoes_funcionarios' not in st.session_state:
    st.session_state.opcoes_funcionarios = []

if 'Escola' not in st.session_state:
    st.session_state.Escola = None

if 'funcionario_selecionado' not in st.session_state:
    st.session_state.funcionario_selecionado = None

if 'Cargo' not in st.session_state:
    st.session_state.Cargo = None

def Form_PesquisaFuncionario():  

    ut.Divisor('Pesquisar Funcionário', 'search', 'rgb(20,80,90)', 'key_Funcionario01')

    # Linha 00
    with st.container():
        row_0_col0, row_0_col1, row_0_col2 = st.columns([2, 3, 3])

        with row_0_col0:
            # Seleção da escola fora do formulário
            escola_selecionada = st.selectbox("Escola", opcoes_escola, index=None if st.session_state.Suporte else opcoes_escola.index(st.session_state.Escola_L) if st.session_state.Escola_L in opcoes_escola else None, placeholder='Selecione uma escola...', key='Escola_Selectbox', disabled= not st.session_state.Suporte)
            # Atualiza as opções de funcionários com base na escola selecionada
            if escola_selecionada != st.session_state.Escola:
                st.session_state.Escola = escola_selecionada
                escola_selecionada = st.session_state.Escola.split(" - ", 1)[-1] if st.session_state.Escola else None
                st.session_state.opcoes_funcionarios = carregar_opcoes_funcionarios(escola_selecionada)
       
        with row_0_col1:            
            # Configura o selectbox com as opções e o índice definido
            st.session_state.funcionario_selecionado = st.selectbox('Funcionário(a)', st.session_state.opcoes_funcionarios, index=None, placeholder='Selecione um funcionário(a)...', key='Funcionario_Selectbox')

        with row_0_col2:
            st.session_state.Cargo = st.selectbox('Cargo', cargos_escola_p, index=0, placeholder='Seleciona a Cargo...')
        
        row_1_col1, row_1_col2 = st.columns([8, 0.01])  
        row_2_col1, row_2_col2, row_2_col3, row_2_col4, row_2_col5 = st.columns([3, 3, 2, 3, 3]) 
        
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
             
            if 'funcionario_selecionado' in st.session_state and st.session_state.funcionario_selecionado:
                Matricula = st.session_state.funcionario_selecionado.split(' ', 1)[0]
            else:
                Matricula = None  
                            
            # Chama a função listar_Funcionario com os filtros selecionados
            df_filtrado = FuncionarioDAO.listar_funcionario(Escola, Matricula, st.session_state.Cargo)
            # Mostra os funcionários filtrados em um DataFrame do Pandas
            if not df_filtrado.empty:
                # Obter o DataFrame estilizado
                styled_df = style_df(df_filtrado)
                # Exibir o DataFrame estilizado como HTML
                st.write(styled_df.to_html(), unsafe_allow_html=True)
            else:
                st.write("Não há Funcionários correspondentes aos filtros selecionados.")        
         
    ut.Divisor('Copyright (c) 2024','','rgb(20,80,90)', 'key_Funcionario02')
