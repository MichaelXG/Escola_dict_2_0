import streamlit as st
from Controllers.PadraoController import *
from Controllers.ProfessorController import *
from Controllers.NavegadorController import *
import streamlit_antd_components as sac
import Utils as ut

def Form_Professor():
    
    def disable_form(action:int):
        if action == 0:
            st.session_state.Novo = True
            st.session_state.form_Habilitado = False
        elif action == 1 or action == 3:
            st.session_state.Edit = True
            st.session_state.form_Habilitado = False
        
    def reset_session_state():
        # Definir st.session_state como um dicionário vazio
        st.session_state.contador = 0
        st.session_state.form_Habilitado = True
        st.session_state.Primeiro_acesso = True
        st.session_state.Edit = False
        st.session_state.Novo = False                     
        
    reset_session_state() 
    
    if "widget" not in st.session_state:
        st.session_state.widget = ""

    if 'index' not in st.session_state:
        st.session_state.index = 0

    if 'Matricula_prof' not in st.session_state:
        st.session_state.Matricula_prof = 0

    if 'Nome' not in st.session_state:
        st.session_state.Nome = ''

    if 'Idade' not in st.session_state:
        st.session_state.Idade = None

    if 'Classe' not in st.session_state:
        st.session_state.Classe = None

    ut.Divisor('Adicionar / Alterar Professor', 'mortarboard-fill', 'rgb(20,80,90)', 'key_Professor1')

    Escola = None if st.session_state.Suporte else st.session_state.Escola_L.split(" - ", 1)[-1]
    df_filtrado_qtd = ProfessorDAO.listar_professor(Escola, None, 'Todas', 'Todas') 
    p_max_value = len(df_filtrado_qtd) -1
        
    def menu_itens():
        action = sac.buttons([
            # 0 - Novo
            sac.ButtonsItem(label='', icon='plus-circle', color='rgb(20,80,90)'), 
            # 1 - Editar
            sac.ButtonsItem(label='', icon='pen', color='yellow'),
            # 2 - Salvar
            sac.ButtonsItem(label='', icon='check2-circle', color='green', disabled= True),
            # 3 - Cancelar
            sac.ButtonsItem(label='', icon='x-circle', color='red'),
            # 4 - Atualizar
            sac.ButtonsItem(label='', icon='arrow-repeat', color='orange'),
            # 5 - First
            sac.ButtonsItem(label='', icon='chevron-double-left', color='rgb(20,80,90)'),
            # 6 - Prior
            sac.ButtonsItem(label='', icon='chevron-left', color='rgb(20,80,90)'),
            # 7 - Next
            sac.ButtonsItem(label='', icon='chevron-right', color='rgb(20,80,90)'),
            # 8 - Last
            sac.ButtonsItem(label='', icon='chevron-double-right', color='rgb(20,80,90)'),
            # 9 - Deletar
            sac.ButtonsItem(label='', icon='trash-fill', color='dark'),
            # 10 - Informação
            sac.ButtonsItem(icon='info-circle', color='blue')
         ], label='', key='menu-nav-escola', align='center', radius='lg', color='rgb(20,80,90)', return_index=True, index=8)
    
        return action

    # Cria o menu de navegação entre os itens
    action_escola = menu_itens()
    
    # Cria um novo dicionário combinando os registros de funcionários e professores
    registros_completos = {}

    # Itera sobre os registros de funcionários
    for matricula, dados_funcionario in registros_funcionario.items():
        if dados_funcionario['Cargo'] == 'Professor(a)':
            # Encontra o registro correspondente no registros_professor usando a matrícula
            dados_professor = next((dados for dados in registros_professor.values() if dados['Matrícula'] == matricula), None)
            
            # Se o professor foi encontrado no registros_professor
            if dados_professor:
                # Cria um novo registro combinado
                registro_completo = {
                    'Matrícula': matricula,
                    'Escola': dados_funcionario['Escola'],
                    'Classes': dados_professor['Classe'],
                    'Disciplinas': dados_professor['Disciplinas']
                }
                # Adiciona o registro combinado ao novo dicionário
                registros_completos[matricula] = registro_completo

    # Filtrar os registros dos professores da escola logada
    if not st.session_state.Suporte:
        get_record_user_geral = {matricula: professor for matricula, professor in registros_completos.items() if professor['Escola'] == Escola}
    else:
        get_record_user_geral = {matricula: professor for matricula, professor in registros_completos.items()}

    get_record_user_atual = NavegadorRegistros(get_record_user_geral)
    get_record_user = {}
    
    # st.write('get_record_user ', get_record_user)
    if action_escola == 0:  # Novo
        disable_form(action_escola)
        get_record_user = None

    if action_escola == 1:  # Editar
        disable_form(action_escola)
        get_record_user = get_record_user_atual.editar(st.session_state.index)

    if action_escola == 2:  # Salvar
        pass  # Implemente a lógica para salvar as alterações no registro

    if action_escola == 4:  # Atualizar
        ut.fn_spinner_3('Aguarde, recarregando o registro...')
        get_record_user = get_record_user_atual.refresh(st.session_state.index)

    if action_escola == 3:  # Cancelar
        if not(st.session_state.form_Habilitado):
            reset_session_state()
        else:
            ut.Alerta('', f'O item não esta em edição.')
                    
        get_record_user_geral = {}
        get_record_user_atual = {}
        get_record_user = {}
        get_record_user_geral = registros_professor
        get_record_user_atual = NavegadorRegistros(get_record_user_geral)
        get_record_user = get_record_user_atual.refresh(st.session_state.index)
    
    if action_escola == 4:  # Atualizar
        reset_session_state()
        ut.fn_spinner_3('Aguarde, recarregando o registro...')   
        get_record_user_geral = registros_professor 
        get_record_user_atual = NavegadorRegistros(get_record_user_geral)
        get_record_user = {}
        get_record_user = get_record_user_atual.refresh(st.session_state.index)   
                                                          
    if action_escola == 5:  # First
        ut.fn_spinner_3('Carregando primeiro registro...')
        get_record_user = get_record_user_atual.first_registro()

    if action_escola == 6:  # Prior
        if st.session_state.index > 0:  # Verifica se não está no primeiro registro
            ut.fn_spinner_3('Carregando registro anterior...')
            get_record_user = get_record_user_atual.registro_prior(st.session_state.index)
        else:
            ut.Alerta('', 'Já está no primeiro registro.')
            get_record_user = get_record_user_atual.first_registro()  # Mantém o primeiro registro na tela

    if action_escola == 7:  # Next
        ut.fn_spinner_3('Carregando próximo registro...')
        if st.session_state.index < p_max_value:
            get_record_user = get_record_user_atual.next_registro(st.session_state.index)
        else:
            ut.Alerta('', 'Já está no último registro.')
            get_record_user = get_record_user_atual.last_registro() 
             
    if action_escola == 8:  # Último registro
        ut.fn_spinner_3('Carregando último registro...')
        get_record_user = get_record_user_atual.last_registro()
    
    if action_escola == 9:  # Deletar 
        if ProfessorDAO.deletar_Professor(st.session_state.Matricula_prof): 
            ut.fn_spinner_3('Aguarde...')   
            ut.Sucesso('', f'Usuário "{st.session_state.Matricula_prof} - {st.session_state.Nome}" deletado com sucesso')
            get_record_user_geral = registros_professor 
            get_record_user_atual = NavegadorRegistros(get_record_user_geral)
            get_record_user = {}
            get_record_user = get_record_user_atual.last_registro()
            reset_session_state()
            
    if action_escola == 10:  # Informação
        get_record_user = get_record_user_atual.informacoes(st.session_state.index)
        ut.Alerta('', 'Não implementado...')
   
    if get_record_user:
        st.session_state.Matricula_prof = get_record_user.get('Matrícula', 0)
        st.session_state.Nome = get_record_user.get('Nome', '')
        st.session_state.Idade = get_record_user.get('Idade', None)


    # Exibir o registro na tela
    if bool(get_record_user) and st.session_state.Novo == False:
        
        if bool(get_record_user):
            permissao_editar = False if not(st.session_state.form_Habilitado) else True
        else:
            permissao_editar = True
            ut.Alerta('', 'Edição permitida somente pelo Administrador.')
            
        with st.form(key='form_Professor', clear_on_submit=True):
            row_0_col1, row_0_col2 = st.columns([4, 4])
            row_1_col1, row_1_col2 = st.columns([4, 4])
            row_2_col1, row_2_col2 = st.columns([10, 0.01])
            row_4_col1, row_4_col2, row_4_col3, row_4_col4, row_4_col5 = st.columns([2, 2, 1, 2, 2])

            with row_0_col1:
                # Filtrando apenas os professores do dicionário de funcionários
                professores = {k: v for k, v in registros_funcionario.items() if v['Cargo'] == 'Professor(a)'}

                # Primeiro, obtenha uma lista de opções para o selectbox
                # Adicionando nome do professor do dicionário de registros_funcionario
                opcoes_professores = [
                    f'{prof["Matrícula"]} - {registros_funcionario[prof["Matrícula"]]["Nome"]}' 
                    for prof in registros_professor.values()
                ]

                # Agora, defina o índice com base na matrícula do professor atualmente selecionado na sessão
                # Certifique-se de que a matrícula esteja como string
                matricula_selecionada = str(st.session_state.get('Matricula_prof', ''))

                # Se a matrícula selecionada estiver na lista de matrículas dos professores, defina o índice correspondente
                if matricula_selecionada in [opcao.split(" ")[0] for opcao in opcoes_professores]:
                    index_matricula_selecionada = [opcao.split(" ")[0] for opcao in opcoes_professores].index(matricula_selecionada)
                else:
                    # Caso contrário, defina o índice como None para selecionar a opção padrão
                    index_matricula_selecionada = None

                # Por fim, configure o selectbox com as opções e o índice definido
                st.session_state.Professor = st.selectbox('Professor(a)', opcoes_professores, index=index_matricula_selecionada, placeholder='Selecione um Professor(a)...', disabled=permissao_editar)

                # Recupera a matrícula do professor selecionado
                if st.session_state['Professor']:
                    # Divide a string na posição do primeiro espaço em branco
                    matricula = st.session_state['Professor'].split(' ', 1)[0]
                    # Atualiza a matrícula na sessão
                    st.session_state['Matricula_prof'] = matricula

                if not st.session_state['Professor']:
                    st.error('O campo "Professor(a)" é Obrigatorio.')
 
            with row_0_col2:
                st.write('')     
                
            # Linha 01    
            with row_1_col1:
                st.write('')
                with st.expander("Classes", expanded=False):
                    # Classes já selecionadas para o professor
                    classes_selecionadas = ProfessorDAO.carregar_classe_professor(st.session_state.Matricula_prof)
                    Classes = []
                    Classes = sac.transfer(items=classes, label='', index=[classes.index(classe) for classe in classes_selecionadas if classe in classes], format_func='title', titles=['Disponíveis', 'Selecionadas'], reload=True, align='center', color='rgb(20,80,90)', search=True, pagination=True,  disabled=permissao_editar)

            with row_1_col2:
                st.write('')
                with st.expander("Disciplinas", expanded=False):
                    # Disciplinas já selecionadas para o professor
                    disciplinas_selecionadas = ProfessorDAO.carregar_disciplinas_professor(st.session_state.Matricula_prof)
                    Disciplinas = []
                    Disciplinas = sac.transfer(items=disciplinas, label='', index=[disciplinas.index(disciplina) for disciplina in disciplinas_selecionadas if disciplina in disciplinas], format_func='title', titles=['Disponíveis', 'Selecionadas'], reload=True, align='center', color='rgb(20,80,90)', search=True, pagination=True,  disabled=permissao_editar)
                
            # Linha 02
            with row_2_col1:
                sac.menu([sac.MenuItem(type='divider')], color='rgb(20,80,90)', open_all=False, return_index=False, index=None, key='key_divisor')
            with row_2_col2:
                st.write('')

            with row_4_col1:
                st.write('')

            with row_4_col2:
                st.write('')

            with row_4_col3:
                form_submit_button_Professor = st.form_submit_button('Salvar')

            with row_4_col4:
                st.write('')

            with row_4_col5:
                st.write('')

            if form_submit_button_Professor:
                if not(st.session_state.form_Habilitado) and st.session_state.Edit == True:
                    if st.session_state.Matricula_prof and bool(Classes) and bool(Disciplinas):
                        ProfessorDAO.alterar_Professor(st.session_state.Matricula_prof, Classes, Disciplinas)
                        ut.fn_spinner_3('Aguarde, alterado registro...')  
                        # get_record_user_geral = registros_professor
                        get_record_user_atual = NavegadorRegistros(get_record_user_geral)
                        get_record_user = {}
                        get_record_user = get_record_user_atual.refresh(st.session_state.index)
                        
                        reset_session_state()
                        ut.Sucesso('', f'Matrícula "{st.session_state.Matricula_prof} - {st.session_state.Nome}",  alterado com sucesso')
                        st.rerun()
                    else:
                        ut.Alerta('', 'Parametros para Alterar um Professor incompleto') 
                else:
                    ut.Alerta('', 'É preciso clicar no botão editar.')
    else:
        with st.form(key='form_Professor_new', clear_on_submit=True):
            row_0_col1, row_0_col2 = st.columns([4, 4])
            row_1_col1, row_1_col2 = st.columns([4, 4])
            row_2_col1, row_2_col2 = st.columns([10, 0.01])
            row_4_col1, row_4_col2, row_4_col3, row_4_col4, row_4_col5 = st.columns([2, 2, 1, 2, 2])

            with row_0_col1:   
                # Filtrando apenas os professores cujas matrículas não estão no dicionário registros_professor
                professores_nao_registrados = {k: v for k, v in registros_funcionario.items() if v['Cargo'] == 'Professor(a)' and v['Matrícula'] not in [professor["Matrícula"] for professor in registros_professor.values()]}

                # Criação das opções do selectbox com matrícula e nome
                opcoes_professores = [f'{prof["Matrícula"]} - {prof["Nome"]}' for prof in professores_nao_registrados.values()]
                st.session_state.Professor = st.selectbox('Professor(a)', opcoes_professores, index=None, placeholder='Selecione um Professor(a)...')

                if not st.session_state.Professor:
                    st.error('O campo "Professor(a)" é Obrigatório.')
                    
            with row_0_col2:
                st.write('')     
                
            # Linha 01    
            with row_1_col1:
                st.write('')
                with st.expander("Classes", expanded=False):
                    Classes = []
                    Classes = sac.transfer(items=classes, label='', index=[None, None], format_func='title', titles=['Disponíveis', 'Selecionadas'], reload=True, align='center', color='rgb(20,80,90)', search=True, pagination=True)

            with row_1_col2:
                st.write('')
                with st.expander("Disciplinas", expanded=False):
                    Disciplinas = []
                    Disciplinas = sac.transfer(items=disciplinas, label='', index=[None, None], format_func='title', titles=['Disponíveis', 'Selecionadas'], reload=True, align='center', color='rgb(20,80,90)', search=True, pagination=True)
        

            with row_2_col1:
                sac.menu([sac.MenuItem(type='divider')], color='rgb(20,80,90)', open_all=False, return_index=False, index=None, key='key_divisor')
            with row_2_col2:
                st.write('')

            with row_4_col1:
                st.write('')

            with row_4_col2:
                st.write('')

            with row_4_col3:
                form_submit_button_Professor = st.form_submit_button('Salvar')

            with row_4_col4:
                st.write('')

            with row_4_col5:
                st.write('')
                    
            if form_submit_button_Professor:
                if st.session_state.Nome and st.session_state.Idade and st.session_state.Classe:
                    ProfessorDAO.adicionar_Professor(st.session_state.Nome, st.session_state.Idade, st.session_state.Classe)
                else:
                    ut.Alerta('', 'Parametros para incluir um novo Professor incompleto')
                    
    ut.Divisor('Copyright (c) 2024', '', 'rgb(20,80,90)', 'key_Professor2')
