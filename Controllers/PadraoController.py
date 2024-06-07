import pandas as pd 

# criar lista de Login
login = []

login = [{"Apelido":'Suporte',"Password": '123'},
         {"Apelido":'Visitante',"Password": 'visitante123'},
         {"Apelido":'Maria',"Password": 'Maria@123'}
        ]
apelidos = ['Suporte', 'Visitante', 'Maria']

registros_escola = {
    1: {
        'Cód. Escola': 1, 
        'Nome Escola': 'Escola 01'
    },
    2: {
        'Cód. Escola': 2, 
        'Nome Escola': 'Escola 02'
    }
}

# Gerar lista de opções para o selectbox
opcoes_escola = [f"{dados['Cód. Escola']} - {dados['Nome Escola']}" for dados in registros_escola.values()]

registros_funcionario = {
     1: {
        'Matrícula': 1, 
        'Escola': 'Escola 01',
        'Nome': 'Emanuel Vasconcelos', 
        'Idade': 36, 
        'Cargo': 'Diretor(a)'
    },
     2: {
        'Matrícula': 2,
        'Escola': 'Escola 01', 
        'Nome': 'Anthony Gabriel Vasconcelos', 
        'Idade': 39, 
        'Cargo': 'Vice-Diretor(a)'
    },
     3: {
        'Matrícula': 3,
        'Escola': 'Escola 01', 
        'Nome': 'Vitor Camargo', 
        'Idade': 37, 
        'Cargo': 'Coordenador(a) Pedagógico(a)'
        
    },
     4: {
        'Matrícula': 4, 
        'Escola': 'Escola 01',
        'Nome': 'Emanuel Casa Grande',
        'Idade': 47, 
        'Cargo': 'Coordenador(a) Administrativo(a)'
    },
     5: {
        'Matrícula': 5, 
        'Escola': 'Escola 01',
        'Nome': 'Luiz Gustavo Moreira', 
        'Idade': 44, 
        'Cargo': 'Professor(a)'
    },
     6: {
        'Matrícula': 6,
        'Escola': 'Escola 01', 
        'Nome': 'Stephany Costela', 
        'Idade': 26, 
        'Cargo': 'Auxiliar Administrativo(a)'
        },
     7: {
        'Matrícula': 7,
        'Escola': 'Escola 01', 
        'Nome': 'Isadora Gonçalves', 
        'Idade': 60, 
        'Cargo': 'Secretário(a) Escolar'
    },
     8: {
        'Matrícula': 8, 
        'Escola': 'Escola 01',
        'Nome': 'Guilherme Montenegro', 
        'Idade': 31, 
        'Cargo': 'Servente'
    },
     9: {
        'Matrícula': 9, 
        'Escola': 'Escola 01',
        'Nome': 'Brayan Santos', 
        'Idade': 37, 
        'Cargo': 'Merendeira(o)'
    },
    10: {
        'Matrícula': 10,
        'Escola': 'Escola 01',
        'Nome': 'Pedro Lucas Santos', 
        'Idade': 34, 
        'Cargo': 'Bibliotecário(a)'
    },
    11: {
        'Matrícula': 11,
        'Escola': 'Escola 01',
        'Nome': 'Henry Guerra',
        'Idade': 23, 
        'Cargo': 'Monitor(a) de Alunos'
        },
    12: {
        'Matrícula': 12,
        'Escola': 'Escola 01',
        'Nome': 'Júlia Costela',
        'Idade': 24, 
        'Cargo': 'Técnico(a) de Informática'
    },
    13: {
        'Matrícula': 13,
        'Escola': 'Escola 01',
        'Nome': 'Enrico Moreira', 
        'Idade': 45, 
        'Cargo': 'Orientador(a) Educacional'
    },
    14: {
        'Matrícula': 14,
        'Escola': 'Escola 01',
        'Nome': 'Dra. Lara das Neves', 
        'Idade': 37, 
        'Cargo': 'Psicólogo(a) Escolar'
    },
    15: {
        'Matrícula': 15,
        'Escola': 'Escola 01',
        'Nome': 'Isadora Rodrigues', 
        'Idade': 20, 
        'Cargo': 'Fisioterapeuta'
    },
    16: {
        'Matrícula': 16,
        'Escola': 'Escola 01',
        'Nome': 'Sra. Rafaela Vargas', 
        'Idade': 32, 
        'Cargo': 'Nutricionista'
    },
    17: {
        'Matrícula': 17,
        'Escola': 'Escola 01',
        'Nome': 'Maria Angela', 
        'Idade': 44, 
        'Cargo': 'Professor(a)'
    },
    18: {
        'Matrícula': 18,
        'Escola': 'Escola 01',
        'Nome': 'Amanda Guedes', 
        'Idade': 46, 
        'Cargo': 'Professor(a)'
    },
    19: {
        'Matrícula': 19,
        'Escola': 'Escola 01',
        'Nome': 'Lidia silva', 
        'Idade': 40, 
        'Cargo': 'Professor(a)'
    },
    20: {
        'Matrícula': 20,
        'Escola': 'Escola 01',
        'Nome': 'Rafaela Santos', 
        'Idade': 38, 
        'Cargo': 'Professor(a)'
    },
    21: {
        'Matrícula': 21,
        'Escola': 'Escola 01',
        'Nome': 'Marcos Motta', 
        'Idade': 49, 
        'Cargo': 'Professor(a)'
    },
    # Escola 02
    22: {
        'Matrícula': 22,
        'Escola': 'Escola 02', 
        'Nome': 'Vanessa Silva', 
        'Idade': 36, 
        'Cargo': 'Diretor(a)'
    },
    23: {
        'Matrícula': 23, 
        'Escola': 'Escola 02', 
        'Nome': 'Gabriel Motta', 
        'Idade': 39, 
        'Cargo': 'Vice-Diretor(a)'
    },
    24: {
        'Matrícula': 24, 
        'Escola': 'Escola 02', 
        'Nome': 'Letícia Camargo', 
        'Idade': 37, 
        'Cargo': 'Coordenador(a) Pedagógico(a)'
        
    },
    25: {
        'Matrícula': 25, 
        'Escola': 'Escola 02', 
        'Nome': 'Amanda Coimbra',
        'Idade': 47, 
        'Cargo': 'Coordenador(a) Administrativo(a)'
    },
    26: {
        'Matrícula': 25, 
         'Escola': 'Escola 02', 
        'Nome': 'Luiz Medeiros', 
        'Idade': 44, 
        'Cargo': 'Professor(a)'
    },
    27: {
        'Matrícula': 27,
        'Escola': 'Escola 02',  
        'Nome': 'Stela Alves', 
        'Idade': 26, 
        'Cargo': 'Auxiliar Administrativo(a)'
        },
    28: {
        'Matrícula': 28, 
        'Escola': 'Escola 02', 
        'Nome': 'Isabella Gonçalves', 
        'Idade': 60, 
        'Cargo': 'Secretário(a) Escolar'
    },
    29: {
        'Matrícula': 29,
        'Escola': 'Escola 02',  
        'Nome': 'Matheus Gomes', 
        'Idade': 31, 
        'Cargo': 'Servente'
    },
    30: {
        'Matrícula': 30, 
        'Escola': 'Escola 02', 
        'Nome': 'Luis Campos', 
        'Idade': 37, 
        'Cargo': 'Merendeira(o)'
    },
    31: {
        'Matrícula': 31,
        'Escola': 'Escola 02', 
        'Nome': 'Lucas Santos', 
        'Idade': 34, 
        'Cargo': 'Bibliotecário(a)'
    },
    32: {
        'Matrícula': 32,
        'Escola': 'Escola 02', 
        'Nome': 'Aline Guerra',
        'Idade': 23, 
        'Cargo': 'Monitor(a) de Alunos'
        },
    33: {
        'Matrícula': 33,
        'Escola': 'Escola 02', 
        'Nome': 'Cleber Almeida',
        'Idade': 24, 
        'Cargo': 'Técnico(a) de Informática'
    },
    34: {
        'Matrícula': 34,
        'Escola': 'Escola 02', 
        'Nome': 'Mauricio Moreira', 
        'Idade': 45, 
        'Cargo': 'Orientador(a) Educacional'
    },
    35: {
        'Matrícula': 35,
        'Escola': 'Escola 02', 
        'Nome': 'Dra. Kelly Xavier', 
        'Idade': 37, 
        'Cargo': 'Psicólogo(a) Escolar'
    },
    36: {
        'Matrícula': 36,
        'Escola': 'Escola 02', 
        'Nome': 'Tatiana Carlota', 
        'Idade': 20, 
        'Cargo': 'Fisioterapeuta'
    },
    37: {
        'Matrícula': 37,
        'Escola': 'Escola 02', 
        'Nome': 'Gustavo Borges', 
        'Idade': 32, 
        'Cargo': 'Nutricionista'
    },
    38: {
        'Matrícula': 38,
        'Escola': 'Escola 02', 
        'Nome': 'Maria Aparecida', 
        'Idade': 44, 
        'Cargo': 'Professor(a)'
    },
    39: {
        'Matrícula': 39,
        'Escola': 'Escola 02', 
        'Nome': 'João Martinelli', 
        'Idade': 46, 
        'Cargo': 'Professor(a)'
    },
    40: {
        'Matrícula': 40,
        'Escola': 'Escola 02', 
        'Nome': 'Lilian Andrade', 
        'Idade': 40, 
        'Cargo': 'Professor(a)'
    },
    41: {
        'Matrícula': 41,
        'Escola': 'Escola 02', 
        'Nome': 'Meiry Frota', 
        'Idade': 38, 
        'Cargo': 'Professor(a)'
    },
    42: {
        'Matrícula': 42,
        'Escola': 'Escola 02', 
        'Nome': 'Tiago ventura', 
        'Idade': 49, 
        'Cargo': 'Professor(a)'
    }            
}

registros_professor = {
    1: {
        "Matrícula": 17,
        "Classe": ["1º Ano - Ensino Médio","2º Ano - Ensino Médio","3º Ano - Ensino Médio"],
        "Disciplinas": ["Matemática", "Geometria"]
    },
    2: {
        "Matrícula": 21,
        "Classe": ['1º Ano - Ensino Fundamental', '2º Ano - Ensino Fundamental','3º Ano - Ensino Fundamental','4º Ano - Ensino Fundamental',
          '5º Ano - Ensino Fundamental', '6º Ano - Ensino Fundamental','7º Ano - Ensino Fundamental','8º Ano - Ensino Fundamental',
          '9º Ano - Ensino Fundamental', '1º Ano - Ensino Médio','2º Ano - Ensino Médio','3º Ano - Ensino Médio'],
          "Disciplinas": ["Educação Física"]
    },
    3: {
        "Matrícula": 20,
        "Classe": ['1º Ano - Ensino Fundamental', '2º Ano - Ensino Fundamental','3º Ano - Ensino Fundamental','4º Ano - Ensino Fundamental',
          '5º Ano - Ensino Fundamental', '6º Ano - Ensino Fundamental','7º Ano - Ensino Fundamental','8º Ano - Ensino Fundamental',
          '9º Ano - Ensino Fundamental', '1º Ano - Ensino Médio','2º Ano - Ensino Médio','3º Ano - Ensino Médio'],
          "Disciplinas": ["História"]
    },
    4: {
        "Matrícula": 19,
        "Classe": ['1º Ano - Ensino Fundamental', '2º Ano - Ensino Fundamental','3º Ano - Ensino Fundamental','4º Ano - Ensino Fundamental',
          '5º Ano - Ensino Fundamental', '6º Ano - Ensino Fundamental','7º Ano - Ensino Fundamental','8º Ano - Ensino Fundamental',
          '9º Ano - Ensino Fundamental', '1º Ano - Ensino Médio','2º Ano - Ensino Médio','3º Ano - Ensino Médio'],
          "Disciplinas": ["Língua Portuguesa"]
    },
    5: {
        "Matrícula": 18,
        "Classe": ['1º Ano - Ensino Fundamental', '2º Ano - Ensino Fundamental','3º Ano - Ensino Fundamental','4º Ano - Ensino Fundamental',
          '5º Ano - Ensino Fundamental', '6º Ano - Ensino Fundamental','7º Ano - Ensino Fundamental','8º Ano - Ensino Fundamental',
          '9º Ano - Ensino Fundamental', '1º Ano - Ensino Médio','2º Ano - Ensino Médio','3º Ano - Ensino Médio'],
          "Disciplinas": ["Ciências", "Química"]
    },  
    6: {
        "Matrícula": 41,
        "Classe": ['6º Ano - Ensino Fundamental','7º Ano - Ensino Fundamental','8º Ano - Ensino Fundamental','9º Ano - Ensino Fundamental'],
          "Disciplinas": ["Língua Estrangeira"]
    },
    7: {
        "Matrícula": 42,
        "Classe": ['1º Ano - Ensino Fundamental', '2º Ano - Ensino Fundamental','3º Ano - Ensino Fundamental','4º Ano - Ensino Fundamental',
          '5º Ano - Ensino Fundamental'],
          "Disciplinas": ["Artes", "Filosofia", "Sociologia"]
    }  
}

# Lista para armazenar Nomes
registros_alunos = {
    1: {
        "Matrícula": 1,
        "Escola": "Escola 01",
        "Nome": "João Silva",
        "Idade": 15,
        "Classe": "9º Ano - Ensino Fundamental",
        "Notas": {"Matemática": 85, "Língua Portuguesa": 78, "Ciências": 92, "História": 93}
    },
    2: {
        "Matrícula": 2,
        "Escola": "Escola 01",
        "Nome": "Maria Oliveira",
        "Idade": 14,
        "Classe": "8º Ano - Ensino Fundamental",
        "Notas": {"Matemática": 90, "Língua Portuguesa": 82, "Ciências": 88, "História": 84}
    },
    3: {
        "Matrícula": 3,
        "Escola": "Escola 01",
        "Nome": "Carlos Santos",
        "Idade": 16,
        "Classe": "9º Ano - Ensino Fundamental",
        "Notas": {"Matemática": 59, "Língua Portuguesa": 80, "Ciências": 75, "História": 78}
    },
    4: {
        "Matrícula": 4,
        "Escola": "Escola 01",
        "Nome": "Ana Pereira",
        "Idade": 15,
        "Classe": "9º Ano - Ensino Fundamental",
        "Notas": {"Matemática": 92, "Língua Portuguesa": 85, "Ciências": 90, "História": 88}
    },
    5: {
        "Matrícula": 5,
        "Escola": "Escola 01",
        "Nome": "Pedro Costa",
        "Idade": 14,
        "Classe": "8º Ano - Ensino Fundamental",
        "Notas": {"Matemática": 88, "Língua Portuguesa": 79, "Ciências": 84, "História": 80}
    },
    6: {
        "Matrícula": 6,
        "Escola": "Escola 02",
        "Nome": "Igor Xavier",
        "Idade": 17,
        "Classe": "9º Ano - Ensino Fundamental",
        "Notas": {"Matemática": 59, "Língua Portuguesa": 80, "Ciências": 75, "História": 78}
    },
    7: {
        "Matrícula": 7,
        "Escola": "Escola 02",
        "Nome": "Juliana Alves",
        "Idade": 15,
        "Classe": "7º Ano - Ensino Fundamental",
        "Notas": {"Matemática": 92, "Língua Portuguesa": 85, "Ciências": 90, "História": 88}
    },
    8: {
        "Matrícula": 8,
        "Escola": "Escola 02",
        "Nome": "Gabriel Santos",
        "Idade": 16,
        "Classe": "8º Ano - Ensino Fundamental",
        "Notas": {"Matemática": 88, "Língua Portuguesa": 79, "Ciências": 84, "História": 80}
    }
}


classes = ['1º Ano - Ensino Fundamental', '2º Ano - Ensino Fundamental','3º Ano - Ensino Fundamental','4º Ano - Ensino Fundamental',
          '5º Ano - Ensino Fundamental', '6º Ano - Ensino Fundamental','7º Ano - Ensino Fundamental','8º Ano - Ensino Fundamental',
          '9º Ano - Ensino Fundamental', '1º Ano - Ensino Médio','2º Ano - Ensino Médio','3º Ano - Ensino Médio']

classe_p = ['Todas'] + classes

disciplinas = ['Língua Portuguesa', 'Matemática', 'Ciências', 'História', 'Geografia', 'Língua Estrangeira', 'Educação Física', 'Artes', 'Educação Ambiental', 'Filosofia', 'Sociologia', 'Ensino Religioso', 'Geometria', 'Física', 'Química']

disciplinas_p = ['Todas'] + disciplinas

cargos_escola = [
    "Diretor(a)",
    "Vice-Diretor(a)",
    "Coordenador(a) Pedagógico(a)",
    "Coordenador(a) Administrativo(a)",
    "Professor(a)",
    "Auxiliar Administrativo(a)",
    "Secretário(a) Escolar",
    "Servente",
    "Merendeira(o)",
    "Bibliotecário(a)",
    "Monitor(a) de Alunos",
    "Técnico(a) de Informática",
    "Orientador(a) Educacional",
    "Psicólogo(a) Escolar",
    "Fisioterapeuta",
    "Nutricionista"
]

cargos_escola_p = ['Todos'] + cargos_escola

# Função para gerar nova matrícula
def gerar_nova_matricula(parametro_record_dict: dict):
    if parametro_record_dict:
        nova_matricula = max(parametro_record_dict.keys()) + 1
    else:
        nova_matricula = 1
    return nova_matricula

def style_df_notas(val):
    try:
        if isinstance(val, list):
            # Verificar cada valor na lista e aplicar o estilo de acordo com o valor
            styles = []
            for v in val:
                v_float = float(v)
                if v_float >= 90:
                    styles.append('color: green')
                elif v_float >= 70:
                    styles.append('color: orange')
                else:
                    styles.append('color: red')
            return styles
        else:
            # Se for apenas um valor, aplicar o estilo diretamente
            v_float = float(val)
            if v_float >= 90:
                return 'color: green'
            elif v_float >= 70:
                return 'color: orange'
            else:
                return 'color: red'
    except (ValueError, TypeError):
        return ''  # Se não puder converter para float ou for um tipo inválido, não aplicar estilo


# Função para estilizar linhas alternadas
def zebra_style(row):
    return ['background-color: #f2f2f2' if row.name % 2 == 0 else '' for _ in row]

# Função para estilizar o DataFrame
def style_df(df):
    # Aplicar estilo apenas nas colunas de notas
    notas_cols = [col for col in df.columns if col not in ['Matrícula', 'Nome', 'Idade', 'Classe']]
    styled_df = df.style.applymap(style_df_notas, subset=pd.IndexSlice[:, notas_cols])
    styled_df = styled_df.apply(zebra_style, axis=1)
    return styled_df

# Função para carregar as opções dos funcionarios com base na escola selecionada
def carregar_opcoes_professores(escola_selecionada):
    if escola_selecionada:
        # Filtra apenas os professores que pertencem à escola selecionada
        professores = {
            k: v for k, v in registros_funcionario.items() 
            if v['Cargo'] == 'Professor(a)' and v['Escola'] == escola_selecionada
        }
        
        # Lista de opções para o selectbox
        opcoes_professores = [
            f'{prof["Matrícula"]} - {registros_funcionario[prof["Matrícula"]]["Nome"]}' 
            for prof in registros_professor.values() if prof["Matrícula"] in professores
        ]
    else:
        # Se nenhuma escola for selecionada, carrega todos os professores
        opcoes_professores = [
            f'{prof["Matrícula"]} - {registros_funcionario[prof["Matrícula"]]["Nome"]}' 
            for prof in registros_professor.values() if prof["Matrícula"] in registros_funcionario
        ]
    
    return opcoes_professores

def carregar_opcoes_funcionarios(escola_selecionada):
    if escola_selecionada:
        # Filtra apenas os funcionarios que pertencem à escola selecionada
        funcionarios = {
            k: v for k, v in registros_funcionario.items() 
            if v['Escola'] == escola_selecionada
        }
        
        # Lista de opções para o selectbox
        opcoes_funcionarios = [
            f'{prof["Matrícula"]} - {registros_funcionario[prof["Matrícula"]]["Nome"]}' 
            for prof in registros_funcionario.values() if prof["Matrícula"] in funcionarios
        ]
    else:
        # Se nenhuma escola for selecionada, carrega todos os funcionarios
        opcoes_funcionarios = [
            f'{prof["Matrícula"]} - {registros_funcionario[prof["Matrícula"]]["Nome"]}' 
            for prof in registros_professor.values() if prof["Matrícula"] in registros_funcionario
        ]
    
    return opcoes_funcionarios

def carregar_opcoes_alunos(escola_selecionada):
    if escola_selecionada:
        # Filtra apenas os alunos que pertencem à escola selecionada
        alunos = {
            k: v for k, v in registros_alunos.items() 
            if v['Escola'] == escola_selecionada
        }
        
        # Lista de opções para o selectbox
        opcoes_alunos = [
            f'{aluno["Matrícula"]} - {registros_alunos[aluno["Matrícula"]]["Nome"]}' 
            for aluno in registros_alunos.values() if aluno["Matrícula"] in alunos
        ]
    else:
        # Se nenhuma escola for selecionada, carrega todos os alunos
        opcoes_alunos = [
            f'{aluno["Matrícula"]} - {registros_alunos[aluno["Matrícula"]]["Nome"]}' 
            for aluno in registros_alunos.values() if aluno["Matrícula"] in registros_alunos
        ]
    
    return opcoes_alunos