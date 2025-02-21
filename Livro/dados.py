import sqlite3

# Conexão com o DB ou criar um novo DB 
conn = sqlite3.connect('data.db')

#Criar tabela de Livros
conn.execute('CREATE TABLE livros(\
            id INTEGER PRIMARY KEY AUTOINCREMENT,\
            titulo TEXT NOT NULL,\
            autor TEXT NOT NULL,\
            editora TEXT NOT NULL,\
            ano_publicacao INTEGER NOT NULL,\
            isbn TEXT NOT NULL\
            )')

#Criar tabela de usuários
conn.execute('CREATE TABLE usuarios(\
            id INTEGER PRIMARY KEY AUTOINCREMENT,\
            nome TEXT NOT NULL,\
            sobrenome TEXT NOT NULL,\
            endereco TEXT NOT NULL,\
            email TEXT NOT NULL,\
            telefone TEXT NOT NULL\
            )')
#Criar tabela de emprestimos
conn.execute('CREATE TABLE emprestimos(\
            id INTEGER PRIMARY KEY AUTOINCREMENT,\
            id_livro INTEGER NOT NULL,\
            id_usuario INTEGER NOT NULL,\
            data_emprestimo TEXT,\
            data_devolucao TEXT,\
            FOREIGN KEY(id_livro) REFERENCES livros(id),\
            FOREIGN KEY(id_usuario) REFERENCES usuarios(id)\
            )')

