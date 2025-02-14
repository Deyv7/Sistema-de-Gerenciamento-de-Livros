import sqlite3

#Conexão com o DB ou criar um novo DB
def connect():
    conn = sqlite3.connect("dados.db")
    return conn

#Função para --->INSERIR<--- um novo Livro
def insert_book(titulo, autor, editora, ano_publicacao, isbn):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO livros (titulo, autor, editora, ano_publicacao, isbn)\
                    VALUES (?, ?, ?, ?, ?)", (titulo, autor, editora, ano_publicacao, isbn))
    conn.commit()
    conn.close()

#Função para --->INSERIR<--- um novo Usuário
def insert_user(nome, sobrenome, endereco, email, telefone):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO usuarios (nome, sobrenome, endereco, email, telefone)\
                    VALUES (?, ?, ?, ?, ?)", (nome, sobrenome, endereco, email, telefone))
    conn.commit()
    conn.close()

#Função para --->EXIBIR<-- todos os Livros
def show_books():
    conn = connect()
    livros = conn.execute("SELECT * FROM livros").fetchall()
    conn.close()
    if not livros:
        print("Nenhum livro encontrado na biblioteca.")
        return
    print("Livros na blibioteca:")
    for livro in livros:
        print(f"ID: {livro[0]}\nTitulo: {livro[1]}\nAutor: {livro[2]}\nEditora: {livro[3]}\nAno de publicacao: {livro[4]}\nISBN: {livro[5]}")
    
#Exemplo das funções
# insert_book("O Senhor dos Aneis", "J. R. R. Tolkien", "Editora A", 1954, "978-3-16-148410-0")
# insert_user("Joaquim", "Silva", "Rua das Flores, 123", "vY5n0@example.com", "123-456-7890")
# Está comentado pelo fato depois que criar as conexões vamos inserir essas
# informações nas tabelas
# show_books()

# Função para --->REALIZAR<--- emprestimos de Livros
def insert_loan(id_livro, id_usuario, data_emprestimo, data_devolucao):
    conn = connect()
    conn.execute ("INSERT INTO emprestimos (id_livro, id_usuario, data_emprestimo, data_devolucao)\
                    VALUES (?, ?, ?, ?)", (id_livro, id_usuario, data_emprestimo, data_devolucao))
    conn.commit()
    conn.close()

#Função para exibir todos os livros emprestados no momento
def get_books_on_loan():
    conn = connect()
    result = conn.execute("SELECT livros.titulo, usuarios.nome, emprestimos.id, usuarios.sobrenome, emprestimos.data_emprestimo, emprestimos.data_devolucao\
                          FROM livros\
                          INNER JOIN emprestimos ON livros.id = emprestimos.id_livro\
                          INNER JOIN usuarios ON emprestimos.id_usuario = usuarios.id\
                          WHERE emprestimos.data_devolucao IS NULL").fetchall()
    conn.close()
    return result

# #Exemplo das funções
# insert_book("O Senhor dos Aneis", "J. R. R. Tolkien", "Editora A", 1954, "978-3-16-148410-0")
# insert_user("Joaquim", "Silva", "Rua das Flores, 123", "vY5n0@example.com", "123-456-7890")
# insert_loan(1, 1, "2022-01-01", "None")
# print(get_books_on_loan())

