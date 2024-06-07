import streamlit as st
import streamlit_antd_components as sac
import pages.Aluno.FormAluno as fa
import pages.Aluno.FormPesquisaAluno as fpa
import pages.Aluno.FormLancarNotas as fln
import pages.Funcionario.FormFuncionario as ff
import pages.Funcionario.FormPesquisaFuncionario as fpf
import pages.Professor.FormProfessor as fp
import pages.Professor.FormPesquisaProfessor as fpp
import pages.Escola.FormEscola as fe

from pages.Home.Create_Home import Create_Home    
from pages.Login.Login import login_page    
from Controllers.PadraoController import *  

def Main():
    # Menu
    with st.sidebar:
        st.image('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT7IXmgTxQAaJ1q3vrff6Hzq1wC7_ScfywO0w&usqp=CAU', width=None, use_column_width='auto') 
        selected_usu = sac.menu([
            sac.MenuItem(f'Bem-vindo, "{st.session_state.Apelido_L}"!',  description= st.session_state.Escola_L, icon=sac.BsIcon(name='person-bounding-box', color='rgb(20,80,90)')),   
            # Usuário Logado
            sac.MenuItem(type='divider'),
            sac.MenuItem('Logout', icon=sac.BsIcon(name='box-arrow-left', color='red')),
            sac.MenuItem(type='divider'),
        ], color='rgb(20,80,90)', open_all=False, return_index=False, index=0, key='Menu_login')
    
    if selected_usu == 'Logout':
        st.session_state.logged_in = False
        st.rerun()  
          
    with st.sidebar:
        selected = sac.menu([
            sac.MenuItem('Menu Principal', icon=sac.BsIcon(name='menu-button-wide-fill', color='rgb(20,80,90)')),   
            # Novo Escola
            sac.MenuItem(type='divider'),
            sac.MenuItem('Escola',  icon=sac.BsIcon(name='building-fill-add', color='rgb(20,80,90)'), description='Adicionar / Alterar Escola', disabled= not st.session_state.Suporte),
            sac.MenuItem(type='divider'),
            sac.MenuItem('Funcionários',  icon=sac.BsIcon(name='person-fill-add', color='rgb(20,80,90)'), description='Adicionar / Alterar Funcionários'), #, disabled= not st.session_state.Suporte),
            # Listar Funcionários
            sac.MenuItem('Listar Funcionários', icon=sac.BsIcon(name='person-lines-fill', color='rgb(20,80,90)'), description='Listar os Funcionários cadastrados'),
             # Novo Professor
            sac.MenuItem(type='divider'),
            sac.MenuItem('Professor',  icon=sac.BsIcon(name='mortarboard-fill', color='rgb(20,80,90)'), description='Adicionar / Alterar Professor'), #, disabled= not st.session_state.Suporte),
            sac.MenuItem('Listar Professor', icon=sac.BsIcon(name='person-lines-fill', color='rgb(20,80,90)'), description='Listar os Professores cadastrados'),

            # Novo Aluno
            sac.MenuItem(type='divider'),
            sac.MenuItem('Alunos',  icon=sac.BsIcon(name='person-fill', color='rgb(20,80,90)'), description='Adicionar / Alterar Alunos'), #, disabled= not st.session_state.Suporte),
            # Lançar Notas
            sac.MenuItem('Lançar Notas',  icon=sac.BsIcon(name='graph-up-arrow', color='rgb(20,80,90)'), description='Lançar as notas dos alunos'),
            # Listar Alunos
            sac.MenuItem('Listar Alunos', icon=sac.BsIcon(name='clipboard2-data', color='rgb(20,80,90)'), description='Listar os Alunos cadastrados'),
            sac.MenuItem(type='divider'),
        ], color='rgb(20,80,90)', open_all=False, return_index=False, index=0, key='Menu_principal')
    
    if selected == 'Menu Principal':
        Create_Home()
    elif selected == 'Escola':
        if __name__ == "__main__":
            fe.Form_Escola()  
    elif selected == 'Funcionários':
        if __name__ == "__main__":
            ff.Form_Funcionario()     
    elif selected == 'Listar Funcionários':
        if __name__ == "__main__":
            fpf.Form_PesquisaFuncionario()    
    elif selected == 'Professor':
        if __name__ == "__main__":
            fp.Form_Professor()
    elif selected == 'Listar Professor':
        if __name__ == "__main__":
            fpp.Form_PesquisaProfessor()               
    elif selected == 'Alunos':
        if __name__ == "__main__":
            fa.Form_Aluno()
    elif selected == 'Lançar Notas':
        if __name__ == "__main__":
            fln.Form_Lancar_Notas()            
    elif selected == 'Listar Alunos':
         if __name__ == "__main__":
            fpa.Form_PesquisaAluno()   
          
# Lógica para alternar entre as páginas com base na ação do usuário
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
 
st.set_page_config(
    page_title="Escola 2.0",
    page_icon=":school:",
    layout="wide",
    initial_sidebar_state="expanded"
)   
        
if __name__ == "__main__":
    if st.session_state.logged_in:        
        Main()
    else:
        opcao = st.radio("Escolha uma opção:", ["Login"], horizontal= True)
        if opcao == "Login":
            if __name__ == "__main__":
                login_page()
