# Importar bibliotecas
import streamlit as st
import pandas as pd
import sqlite3

# Conecta no banco de dados
con = sqlite3.connect('dsadb2.db')



# Abre um cursor para percorrer os dados no banco de dados
cursor = con.cursor()

cursor.execute('''
INSERT INTO estudantes_dsa (nome, sobrenome, nota_exame1, nota_exame2, tipo_sistema_operacional) VALUES
('Xavier', 'Murphy', 86.0, 89.0, 'Linux'),
('Yara', 'Bailey', 80.5, 81.0, 'Windows'),
('Alice', 'Smith', 80.5, 85.0, 'Windows'),
('Quincy', 'Roberts', 86.5, 90.0, 'Mac'),
('Bob', 'Johnson', 75.0, 88.0, 'Linux'),
('Carol', 'Williams', 90.0, 90.5, 'Mac'),
('Grace', 'Miller', 95.5, 93.0, 'Windows'),
('Nina', 'Carter', 80.5, 81.0, 'Windows'),
('Ursula', 'Kim', 80.0, 82.5, 'Linux'),
('Eve', 'Jones', 90.0, 88.0, 'Mac'),
('Frank', 'Garcia', 79.0, 82.0, 'Linux'),
('Helen', 'Davis', 90.0, 89.5, 'Mac'),
('Grace', 'Rodriguez', 89.0, 88.0, 'Windows'),
('Jack', 'Martinez', 90.0, 80.0, 'Linux'),
('Karen', 'Hernandez', 93.5, 91.0, 'Windows'),
('Leo', 'Lewis', 82.0, 85.5, 'Mac'),
('Mallory', 'Nelson', 91.0, 89.0, 'Linux'),
('Oscar', 'Mitchell', 88.0, 87.5, 'Linux'),
('Paul', 'Perez', 94.0, 92.0, 'Windows'),
('Rita', 'Gomez', 77.0, 80.0, 'Linux'),
('Steve', 'Freeman', 89.5, 88.5, 'Windows'),
('Troy', 'Reed', 90.0, 92.0, 'Mac'),
('Victor', 'Morgan', 90.0, 85.0, 'Windows'),
('Oscar', 'Bell', 85.5, 87.0, 'Mac'),
('Zane', 'Rivera', 89.0, 90.5, 'Mac'),
('Aria', 'Wright', 75.0, 76.5, 'Linux'),
('Bruce', 'Cooper', 90.0, 84.0, 'Windows'),
('Karen', 'Peterson', 90.0, 92.5, 'Mac'),
('Dave', 'Brown', 88.5, 89.0, 'Windows'),
('Derek', 'Wood', 86.0, 87.5, 'Linux');''')

cursor.execute("SELECT * FROM estudantes_dsa")

# List comprehension para visualizar os nomes das colunas
nomes_colunas = [description[0] for description in cursor.description]

df = pd.DataFrame(cursor.fetchall(), columns=nomes_colunas)

# Fecha o cursor e encerra a conexão
cursor.close()
con.close()

df1 = df.copy()
df2 = df.copy()
df3 = df.copy()
df4 = df.copy()


# Configuração do Streamlit
st.set_page_config(page_title=" Portfolio de Analises de dados", layout="wide")

# importando a logogmarca
#st.image('logomarca.png')

# Interface do Streamlit
#st.write('# Fundamentos Básicos da linguagem SQL')
st.write('<h1 style="color: #141444;">SQL Para Análise de Dados e Data Science</h1>', unsafe_allow_html=True)

# Criando o schema, tabela e inserindo registro
st.markdown('<h2 style="color: #141444;">Criação de Schema, Tabela e Inserindo registros</h2>', unsafe_allow_html=True)
# Criando schema
schema = st.checkbox('1 - Criação de Schema')
if schema:
    st.code('''CREATE SCHEMA cap03 AUTHORIZATION cabral''',language='sql')
# Criando tabela
tabela = st.checkbox('2 - Criação de Tabela Funcionario')
if tabela:
    st.code(
    '''CREATE TABLE cap04.funcionarios (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(50),
    sobrenome VARCHAR(50),
    salario DECIMAL(10, 2),
    departamento VARCHAR(50),
    data_contratacao DATE
);''',language='sql')

# Inserindo Registro na Tabela
registro = st.checkbox('3 - Inserindo Registro')
if registro:
    st.code('''
    INSERT INTO cap03.estudantes_dsa (nome, sobrenome, nota_exame1, nota_exame2, tipo_sistema_operacional) VALUES
('Xavier', 'Murphy', 86.0, 89.0, 'Linux'),
('Yara', 'Bailey', 80.5, 81.0, 'Windows'),
('Alice', 'Smith', 80.5, 85.0, 'Windows'),
('Quincy', 'Roberts', 86.5, 90.0, 'Mac'),
('Bob', 'Johnson', 75.0, 88.0, 'Linux'),
('Carol', 'Williams', 90.0, 90.5, 'Mac'),
('Grace', 'Miller', 95.5, 93.0, 'Windows'),
('Nina', 'Carter', 80.5, 81.0, 'Windows'),
('Ursula', 'Kim', 80.0, 82.5, 'Linux'),
('Eve', 'Jones', 90.0, 88.0, 'Mac'),
('Frank', 'Garcia', 79.0, 82.0, 'Linux'),
('Helen', 'Davis', 90.0, 89.5, 'Mac'),
('Grace', 'Rodriguez', 89.0, 88.0, 'Windows'),
('Jack', 'Martinez', 90.0, 80.0, 'Linux'),
('Karen', 'Hernandez', 93.5, 91.0, 'Windows'),
('Leo', 'Lewis', 82.0, 85.5, 'Mac'),
('Mallory', 'Nelson', 91.0, 89.0, 'Linux'),
('Oscar', 'Mitchell', 88.0, 87.5, 'Linux'),
('Paul', 'Perez', 94.0, 92.0, 'Windows'),
('Rita', 'Gomez', 77.0, 80.0, 'Linux'),
('Steve', 'Freeman', 89.5, 88.5, 'Windows'),
('Troy', 'Reed', 90.0, 92.0, 'Mac'),
('Victor', 'Morgan', 90.0, 85.0, 'Windows'),
('Oscar', 'Bell', 85.5, 87.0, 'Mac'),
('Zane', 'Rivera', 89.0, 90.5, 'Mac'),
('Aria', 'Wright', 75.0, 76.5, 'Linux'),
('Bruce', 'Cooper', 90.0, 84.0, 'Windows'),
('Karen', 'Peterson', 90.0, 92.5, 'Mac'),
('Dave', 'Brown', 88.5, 89.0, 'Windows'),
('Derek', 'Wood', 86.0, 87.5, 'Linux');
''')
  
# Respondendo perguntas
st.markdown('<h2 style="color: #141444;">Respondendo Perguntas</h2>', unsafe_allow_html=True)

# Pergunta 1
consulta_select = st.checkbox('1 - Query SELECT - Consultado Tabela')
consulta_select_df = df1
if consulta_select:
    st.write('**Query**')
    st.code('SELECT * FROM cap03.estudantes_dsa')
    st.write('**Tabela**')
    st.dataframe(consulta_select_df)

# Pergunta 2
consulta_order_by = st.checkbox('2 - Query ORDER BY - Ordenando Tabela por nome')
consulta_order_by_df = df2.sort_values(by="nome")
if consulta_order_by:
    st.write('**Query**')
    st.code('SELECT * FROM cap03.estudantes_dsa ORDER BY nome')
    st.write('**Tabela**')
    st.dataframe(consulta_order_by_df.head())


# Pergunta 3
consulta_where = st.checkbox('3 - Query WHERE - Filtrando por Sistema Operacional')
consulta_where_df = df3
if consulta_where:
    st.write('**Query**')
    st.code('''SELECT * FROM cap03.estudantes_dsa 
            WHERE tipo_sistema_operacional = 'Linux'
            ORDER BY nome''')
    st.write('**Filtrando por Sitema Operacional Linux**')
    st.dataframe(df3[df3['tipo_sistema_operacional'].isin(["Linux"])])
    st.write('**Gráfico de Barra Usuários por Sistema Operacional**')
    st.bar_chart(df3['tipo_sistema_operacional'].value_counts(),color='#141444',horizontal=False)
    st.write('**Gráfico de Linha Usuários por Sistema Operacional**')
    st.line_chart(df3['tipo_sistema_operacional'].value_counts())
    st.write('**Gráfico de Area Usuários por Sistema Operacional**')
    st.area_chart(df3['tipo_sistema_operacional'].value_counts())
