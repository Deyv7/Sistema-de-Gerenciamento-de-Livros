from tkinter import *
from tkinter import Tk, ttk
from PIL import Image, ImageTk
from tkinter import messagebox
from datetime import datetime
# Importa funções do módulo view (certifique-se que elas estão implementadas em view.py)
from view import *

# Cores
co0 = "#2e2d2b"  # Preta
co1 = "#ffffff"  # Branca
co2 = "#4fa882"  # Verde
co3 = "#38576b"  # Valor
co4 = "#403d3d"  # Letra
co5 = "#0e6636"  # Profit
co6 = "#e9a178"
co7 = "#3fbfb9"  # Verde
co8 = "#263238"  # Verde
co9 = "#9e9df5"  # Verde
co10 = "#6e8faf"
co11 = "#f2f4f2"

# Criação da Janela Principal
window = Tk()
window.title("Sistema de Gerenciamento de Livros")
window.geometry('770x330')
window.configure(background=co1)
window.resizable(width=FALSE, height=FALSE)

style = ttk.Style(window)
style.theme_use("clam")

# Frames
frameUP = Frame(window, width=770, height=50, bg=co6, relief="flat")
frameUP.grid(row=0, column=0, columnspan=2, sticky=NSEW)

frameLeft = Frame(window, width=150, height=265, bg=co4, relief="solid")
frameLeft.grid(row=1, column=0, sticky=NSEW)

frameRight = Frame(window, width=600, height=265, bg=co1, relief="raised")
frameRight.grid(row=1, column=1, sticky=NSEW)

# Logo e Título no Cabeçalho
try:
    app_img = Image.open('./images/logo.png')
    app_img = app_img.resize((40, 40))
    app_img = ImageTk.PhotoImage(app_img)
    app_logo = Label(frameUP, image=app_img, width=1000, compound=LEFT, padx=5, anchor=NW, bg=co6, fg=co1)
    app_logo.place(x=5, y=0)
except Exception as e:
    print(f"Erro ao carregar a imagem: {e}")

app_ = Label(frameUP, text="Sistema de Gerenciamento de Livros", compound=LEFT, padx=5, anchor=NW,
             font=('Verdana 15 bold'), bg=co6, fg=co1)
app_.place(x=50, y=7)

app_line = Label(frameUP, width=770, padx=5, anchor=NW, font=('Verdana 1'), bg=co3, fg=co1)
app_line.place(x=0, y=47)

# Menu Lateral com botões para cada funcionalidade
img_user = Image.open('./images/user.png').resize((18, 18))
img_user = ImageTk.PhotoImage(img_user)
b_user = Button(frameLeft, image=img_user, text="Novo Usuário",
                command=lambda: control('novo usuario'),
                compound=LEFT, anchor=NW, font=('Ivy 11'),
                overrelief=RIDGE, relief=GROOVE, bg=co4, fg=co1)
b_user.grid(row=0, column=0, sticky=NSEW, padx=5, pady=6)

img_book = Image.open('./images/book.png').resize((18, 18))
img_book = ImageTk.PhotoImage(img_book)
b_book = Button(frameLeft, image=img_book, text="Novo Livro",
                command=lambda: control('novo livro'),
                compound=LEFT, anchor=NW, font=('Ivy 11'),
                overrelief=RIDGE, relief=GROOVE, bg=co4, fg=co1)
b_book.grid(row=1, column=0, sticky=NSEW, padx=5, pady=6)

img_see_user = Image.open('./images/user.png').resize((18, 18))
img_see_user = ImageTk.PhotoImage(img_see_user)
b_see_user = Button(frameLeft, image=img_see_user, command=lambda: control('ver usuarios'),
                    text="Exibir todos os Usuários", compound=LEFT, anchor=NW,
                    font=('Ivy 11'), overrelief=RIDGE, relief=GROOVE, bg=co4, fg=co1)
b_see_user.grid(row=2, column=0, sticky=NSEW, padx=5, pady=6)

img_see_book = Image.open('./images/book.png').resize((18, 18))
img_see_book = ImageTk.PhotoImage(img_see_book)
b_see_book = Button(frameLeft, image=img_see_book, command=lambda: control('ver livros'),
                    text="Exibir todos os Livros", compound=LEFT, anchor=NW,
                    font=('Ivy 11'), overrelief=RIDGE, relief=GROOVE, bg=co4, fg=co1)
b_see_book.grid(row=3, column=0, sticky=NSEW, padx=5, pady=6)

img_loan = Image.open('./images/add.png').resize((18, 18))
img_loan = ImageTk.PhotoImage(img_loan)
b_loan = Button(frameLeft, image=img_loan, text="Realizar um Emprestimo",
               command=lambda: control('emprestimo'), compound=LEFT, anchor=NW,
               font=('Ivy 11'), overrelief=RIDGE, relief=GROOVE, bg=co4, fg=co1)
b_loan.grid(row=4, column=0, sticky=NSEW, padx=5, pady=6)

img_devolution = Image.open('./images/add.png').resize((18, 18))
img_devolution = ImageTk.PhotoImage(img_devolution)
b_devolution = Button(frameLeft, image=img_devolution, text="Devolução de Empréstimo",
                      command=lambda: control('devolucao'), compound=LEFT, anchor=NW,
                      font=('Ivy 11'), overrelief=RIDGE, relief=GROOVE, bg=co4, fg=co1)
b_devolution.grid(row=5, column=0, sticky=NSEW, padx=5, pady=6)

img_books_on_loan = Image.open('./images/add.png').resize((18, 18))
img_books_on_loan = ImageTk.PhotoImage(img_books_on_loan)
b_books_on_loan = Button(frameLeft, image=img_books_on_loan, text="Livros emprestados no momento",
                         command=lambda: control('livros emprestados'), compound=LEFT, anchor=NW,
                         font=('Ivy 11'), overrelief=RIDGE, relief=GROOVE, bg=co4, fg=co1)
b_books_on_loan.grid(row=6, column=0, sticky=NSEW, padx=5, pady=6)

# Função de controle do Menu: limpa o frameRight e chama a função desejada
def control(i):
    for widget in frameRight.winfo_children():
        widget.destroy()
    if i == 'novo usuario':
        new_user()
    elif i == 'novo livro':
        new_book()
    elif i == 'ver usuarios':
        see_user()
    elif i == 'ver livros':
        see_books()
    elif i == 'emprestimo':
        realize()
    elif i == 'devolucao':
        devolution()
    elif i == 'livros emprestados':
        borrowed_books()

############################
# FUNÇÕES PARA USUÁRIOS, LIVROS, EMPRÉSTIMOS, DEVOLUÇÃO
############################

# Função para INSERIR um novo Usuário
def new_user():
    global img_save
    def add_user():
        first_name = e_f_name.get()
        last_name = e_l_name.get()
        address = e_address.get()
        email = e_email.get()
        phone = e_phone.get()
        if '' in [first_name, last_name, address, email, phone]:
            messagebox.showerror("Erro", "Preencha todos os campos!")
            return
        insert_user(first_name, last_name, address, email, phone)
        messagebox.showinfo("Sucesso", f"Usuário '{first_name} {last_name}' cadastrado com sucesso!")
        e_f_name.delete(0, END)
        e_l_name.delete(0, END)
        e_address.delete(0, END)
        e_email.delete(0, END)
        e_phone.delete(0, END)
    title = Label(frameRight, text="Inserir Novo Usuário", compound=LEFT, padx=5, pady=10,
                  anchor=NW, font=('Verdana 15 bold'), bg=co1, fg=co4)
    title.grid(row=0, column=0, columnspan=4, sticky=NSEW)
    sep = Label(frameRight, width=400, height=1, anchor=NW, font=('Verdana 1'), bg=co3, fg=co1)
    sep.grid(row=1, column=0, columnspan=4, sticky=NSEW)
    l_f_name = Label(frameRight, text="Primeiro Nome ", anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
    l_f_name.grid(row=2, column=0, padx=5, pady=5, sticky=NSEW)
    e_f_name = Entry(frameRight, width=25, justify='left', relief='solid')
    e_f_name.grid(row=2, column=1, padx=5, pady=5, sticky=NSEW)
    l_l_name = Label(frameRight, text="Sobrenome ", anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
    l_l_name.grid(row=3, column=0, padx=5, pady=5, sticky=NSEW)
    e_l_name = Entry(frameRight, width=25, justify='left', relief='solid')
    e_l_name.grid(row=3, column=1, padx=5, pady=5, sticky=NSEW)
    l_address = Label(frameRight, text="Endereço do usuário ", anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
    l_address.grid(row=4, column=0, padx=5, pady=5, sticky=NSEW)
    e_address = Entry(frameRight, width=25, justify='left', relief='solid')
    e_address.grid(row=4, column=1, padx=5, pady=5, sticky=NSEW)
    l_email = Label(frameRight, text="E-mail ", anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
    l_email.grid(row=5, column=0, padx=5, pady=5, sticky=NSEW)
    e_email = Entry(frameRight, width=25, justify='left', relief='solid')
    e_email.grid(row=5, column=1, padx=5, pady=5, sticky=NSEW)
    l_phone = Label(frameRight, text="Telefone ", anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
    l_phone.grid(row=6, column=0, padx=5, pady=5, sticky=NSEW)
    e_phone = Entry(frameRight, width=25, justify='left', relief='solid')
    e_phone.grid(row=6, column=1, padx=5, pady=5, sticky=NSEW)
    img_save = Image.open('./images/save.png').resize((18, 18))
    img_save = ImageTk.PhotoImage(img_save)
    b_save = Button(frameRight, image=img_save, compound=LEFT, width=100, anchor=NW,
                    command=add_user, text="Salvar", bg=co1, fg=co4,
                    font=('Ivy 11'), overrelief=RIDGE, relief=GROOVE)
    b_save.grid(row=7, column=0, columnspan=4, padx=5, pady=5, sticky=NSEW)

# Função para VER Usuários
def see_user():
    title = Label(frameRight, text="Todos os usuários do banco de dados", width=50,
                  compound=LEFT, padx=5, pady=10, relief=FLAT, anchor=NW,
                  font=('Verdana 12'), bg=co1, fg=co4)
    title.grid(row=0, column=0, columnspan=3, sticky=NSEW)
    sep = Label(frameRight, width=400, height=1, anchor=NW, font=('Verdana 1'), bg=co3, fg=co1)
    sep.grid(row=1, column=0, columnspan=3, sticky=NSEW)
    dados = get_user()
    list_header = ['ID','Nome','Sobrenome','Endereço','Email','Telefone']
    global tree
    tree = ttk.Treeview(frameRight, selectmode="extended", columns=list_header, show="headings")
    vsb = ttk.Scrollbar(frameRight, orient="vertical", command=tree.yview)
    hsb = ttk.Scrollbar(frameRight, orient="horizontal", command=tree.xview)
    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
    tree.grid(row=2, column=0, sticky='nsew')
    vsb.grid(row=2, column=1, sticky='ns')
    hsb.grid(row=3, column=0, sticky='ew')
    frameRight.grid_rowconfigure(0, weight=12)
    col_widths = [20,80,80,120,120,76]
    for i, col in enumerate(list_header):
        tree.heading(col, text=col, anchor='nw')
        tree.column(col, width=col_widths[i], anchor='nw')
    for item in dados:
        tree.insert('', 'end', values=item)

# Função para INSERIR um novo Livro
def new_book():
    global img_salvar
    def add():
        title_val = e_titlo.get()
        author = e_autor.get()
        publisher = e_editora.get()
        year = e_ano.get()
        isbn = e_isbn.get()
        if '' in [title_val, author, publisher, year, isbn]:
            messagebox.showerror('Erro', 'Preencha todos os campos')
            return
        insert_book(title_val, author, publisher, year, isbn)
        messagebox.showinfo("Sucesso", "Livro inserido com sucesso")
        e_titlo.delete(0, END)
        e_autor.delete(0, END)
        e_editora.delete(0, END)
        e_ano.delete(0, END)
        e_isbn.delete(0, END)
    title_lbl = Label(frameRight, text="Inserir um novo livro", width=50,
                      compound=LEFT, padx=5, pady=10, font=('Verdana 12'),
                      bg=co1, fg=co4)
    title_lbl.grid(row=0, column=0, columnspan=3, sticky=NSEW)
    sep = Label(frameRight, width=400, height=1, anchor=NW, font=('Verdana 1'), bg=co3, fg=co1)
    sep.grid(row=1, column=0, columnspan=3, sticky=NSEW)
    l_titlo = Label(frameRight, text="Título do livro ", anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
    l_titlo.grid(row=2, column=0, padx=5, pady=5, sticky=NSEW)
    e_titlo = Entry(frameRight, width=25, justify='left', relief='solid')
    e_titlo.grid(row=2, column=1, padx=5, pady=5, sticky=NSEW)
    l_autor = Label(frameRight, text="Autor do título*", anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
    l_autor.grid(row=3, column=0, padx=5, pady=5, sticky=NSEW)
    e_autor = Entry(frameRight, width=25, justify='left', relief='solid')
    e_autor.grid(row=3, column=1, padx=5, pady=5, sticky=NSEW)
    l_editora = Label(frameRight, text="Editora do livro* ", anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
    l_editora.grid(row=4, column=0, padx=5, pady=5, sticky=NSEW)
    e_editora = Entry(frameRight, width=25, justify='left', relief='solid')
    e_editora.grid(row=4, column=1, padx=5, pady=5, sticky=NSEW)
    l_ano = Label(frameRight, text="Ano de publicação do livro* ", anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
    l_ano.grid(row=5, column=0, padx=5, pady=5, sticky=NSEW)
    e_ano = Entry(frameRight, width=25, justify='left', relief='solid')
    e_ano.grid(row=5, column=1, padx=5, pady=5, sticky=NSEW)
    l_isbn = Label(frameRight, text="ISBN do livro* ", anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
    l_isbn.grid(row=6, column=0, padx=5, pady=5, sticky=NSEW)
    e_isbn = Entry(frameRight, width=25, justify='left', relief='solid')
    e_isbn.grid(row=6, column=1, padx=5, pady=5, sticky=NSEW)
    img_salvar = Image.open("./images/save.png").resize((18, 18))
    img_salvar = ImageTk.PhotoImage(img_salvar)
    b_salvar = Button(frameRight, command=add, image=img_salvar, compound=LEFT,
                      width=100, anchor=NW, text="Salvar", bg=co1, fg=co4,
                      font=('Ivy 11'), overrelief=RIDGE, relief=GROOVE)
    b_salvar.grid(row=7, column=1, pady=5, sticky=NSEW)

# Função para VER Livros
def see_books():
    title = Label(frameRight, text="Todos os livros", width=50, compound=LEFT,
                  padx=5, pady=10, relief=FLAT, anchor=NW, font=('Verdana 12'),
                  bg=co1, fg=co4)
    title.grid(row=0, column=0, columnspan=3, sticky=NSEW)
    sep = Label(frameRight, width=400, height=1, anchor=NW, font=('Verdana 1'), bg=co3, fg=co1)
    sep.grid(row=1, column=0, columnspan=3, sticky=NSEW)
    dados = show_books()
    if dados is None:
        dados = []
        messagebox.showinfo("Aviso", "Nenhum livro encontrado!")
    list_header = ['ID', 'Titulo', 'Autor', 'Editora', 'Ano', 'ISBN']
    global tree
    tree = ttk.Treeview(frameRight, selectmode="extended", columns=list_header, show="headings")
    vsb = ttk.Scrollbar(frameRight, orient="vertical", command=tree.yview)
    hsb = ttk.Scrollbar(frameRight, orient="horizontal", command=tree.xview)
    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
    tree.grid(column=0, row=2, sticky='nsew')
    vsb.grid(column=1, row=2, sticky='ns')
    hsb.grid(column=0, row=3, sticky='ew')
    frameRight.grid_rowconfigure(0, weight=12)
    hd = ["nw", "nw", "nw", "nw", "nw", "nw"]
    widths = [20, 165, 110, 100, 50, 50]
    for n, col in enumerate(list_header):
        tree.heading(col, text=col, anchor='nw')
        tree.column(col, width=widths[n], anchor=hd[n])
    for item in dados:
        tree.insert('', 'end', values=item)

# Função para REALIZAR Empréstimos de Livros com seleção de usuário e livro disponível
def realize():
    global tree
    # Limpa o frameRight para montar a interface de empréstimo
    for widget in frameRight.winfo_children():
        widget.destroy()

    # Título da interface
    title_label = Label(frameRight, text="Realizar Empréstimo", font=('Verdana 12 bold'), bg=co1, fg=co4)
    title_label.pack(pady=5)

    # Criando um frame para conter as tabelas lado a lado
    table_frame = Frame(frameRight, bg=co1)
    table_frame.pack(fill=BOTH, expand=True, padx=5, pady=5)

    ###############################
    # 1. SEÇÃO - SELEÇÃO DE USUÁRIO
    ###############################
    user_frame = Frame(table_frame, bg=co1, bd=2, relief=GROOVE)
    user_frame.pack(side=LEFT, padx=5, pady=5, fill=BOTH, expand=True)

    user_label = Label(user_frame, text="Usuários:", font=('Ivy 10 bold'), bg=co1, fg=co4)
    user_label.pack(anchor=W)

    user_tree = ttk.Treeview(user_frame, columns=['ID', 'Nome', 'Sobrenome'], show="headings", selectmode="browse", height=7)
    
    column_widths = [40, 120, 120]  # Ajustando os tamanhos das colunas
    for col, width in zip(['ID', 'Nome', 'Sobrenome'], column_widths):
        user_tree.heading(col, text=col)
        user_tree.column(col, width=width, anchor="center")

    user_tree.pack(side=LEFT, fill=BOTH, expand=True)

    # Scrollbar vertical para usuários
    user_scroll = ttk.Scrollbar(user_frame, orient="vertical", command=user_tree.yview)
    user_tree.configure(yscrollcommand=user_scroll.set)
    user_scroll.pack(side=RIGHT, fill=Y)

    # Preenchendo os usuários na Treeview
    for user in get_user():
        user_tree.insert('', 'end', values=(user[0], user[1], user[2]))

    ###############################
    # 2. SEÇÃO - SELEÇÃO DE LIVRO
    ###############################
    book_frame = Frame(table_frame, bg=co1, bd=2, relief=GROOVE)
    book_frame.pack(side=RIGHT, padx=5, pady=5, fill=BOTH, expand=True)

    book_label = Label(book_frame, text="Livros Disponíveis:", font=('Ivy 10 bold'), bg=co1, fg=co4)
    book_label.pack(anchor=W)

    book_tree = ttk.Treeview(book_frame, columns=['ID', 'Título', 'Autor'], show="headings", selectmode="browse", height=7)
    
    column_widths = [40, 140, 100]  # Ajustando os tamanhos das colunas
    for col, width in zip(['ID', 'Título', 'Autor'], column_widths):
        book_tree.heading(col, text=col)
        book_tree.column(col, width=width, anchor="center")

    book_tree.pack(side=LEFT, fill=BOTH, expand=True)

    # Scrollbar vertical para livros
    book_scroll = ttk.Scrollbar(book_frame, orient="vertical", command=book_tree.yview)
    book_tree.configure(yscrollcommand=book_scroll.set)
    book_scroll.pack(side=RIGHT, fill=Y)

    # Preenchendo os livros disponíveis na Treeview
    for book in get_available_books():
        book_tree.insert('', 'end', values=(book[0], book[1], book[2]))

    ###############################
    # 3. BOTÃO PARA REALIZAR O EMPRÉSTIMO
    ###############################
    def perform_loan():
        selected_user = user_tree.focus()
        selected_book = book_tree.focus()

        if selected_user and selected_book:
            user_values = user_tree.item(selected_user, 'values')
            book_values = book_tree.item(selected_book, 'values')

            if user_values and book_values:
                user_id = user_values[0]
                book_id = book_values[0]
                hoje = datetime.today().strftime("%Y-%m-%d")

                insert_loan(user_id, book_id, hoje, None)

                messagebox.showinfo("Sucesso", f"Empréstimo realizado para {user_values[1]} {user_values[2]} - Livro: {book_values[1]}")

                # Atualiza a lista de livros disponíveis (remove o livro emprestado)
                book_tree.delete(*book_tree.get_children())
                for book in get_available_books():
                    book_tree.insert('', 'end', values=(book[0], book[1], book[2]))

            else:
                messagebox.showerror("Erro", "Erro ao recuperar dados selecionados.")
        else:
            messagebox.showerror("Erro", "Selecione um usuário e um livro antes de confirmar o empréstimo.")

    # Botão para realizar o empréstimo
    btn_perform_loan = Button(frameRight, text="Realizar Empréstimo", command=perform_loan, font=('Ivy 10 bold'), bg=co2, fg=co1)
    btn_perform_loan.pack(pady=10)



# Função para Devolução de Empréstimo
def devolution():
    global img_salvar
    def add():
        loan_id = e_id_emprestimo.get()
        return_date = e_data_retorno.get()
        if '' in [loan_id, return_date]:
            messagebox.showerror('Erro', 'Preencha todos os campos')
            return
        return_loan(loan_id, return_date)
        messagebox.showinfo("Sucesso", "Livro retornado com sucesso")
        e_id_emprestimo.delete(0, END)
        e_data_retorno.delete(0, END)
    title = Label(frameRight, text="Atualizar a data de devolução do empréstimo", width=50,
                  compound=LEFT, padx=5, pady=10, font=('Verdana 12'), bg=co1, fg=co4)
    title.grid(row=0, column=0, columnspan=3, sticky=NSEW)
    sep = Label(frameRight, width=400, height=1, anchor=NW, font=('Verdana 1'), bg=co3, fg=co1)
    sep.grid(row=1, column=0, columnspan=3, sticky=NSEW)
    l_id_emprestimo = Label(frameRight, text="ID empréstimo*", anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
    l_id_emprestimo.grid(row=2, column=0, padx=5, pady=5, sticky=NSEW)
    e_id_emprestimo = Entry(frameRight, width=25, justify='left', relief='solid')
    e_id_emprestimo.grid(row=2, column=1, padx=5, pady=5, sticky=NSEW)
    l_data_retorno = Label(frameRight, text="Nova data de devolução (formato: AAAA-MM-DD)*", anchor=NW,
                           font=('Ivy 10'), bg=co1, fg=co4)
    l_data_retorno.grid(row=3, column=0, padx=5, pady=5, sticky=NSEW)
    e_data_retorno = Entry(frameRight, width=25, justify='left', relief='solid')
    e_data_retorno.grid(row=3, column=1, padx=5, pady=5, sticky=NSEW)
    img_salvar = Image.open("./images/save.png").resize((18, 18))
    img_salvar = ImageTk.PhotoImage(img_salvar)
    b_salvar = Button(frameRight, command=add, image=img_salvar, compound=LEFT,
                      width=100, anchor=NW, text="Salvar", bg=co1, fg=co4,
                      font=('Ivy 11'), overrelief=RIDGE, relief=GROOVE)
    b_salvar.grid(row=7, column=1, pady=5, sticky=NSEW)

# Função para Exibir Livros Emprestados
def borrowed_books():
    title = Label(frameRight, text="Todos os livros emprestados no momento", width=50,
                  compound=LEFT, padx=5, pady=10, relief=FLAT, anchor=NW,
                  font=('Verdana 12'), bg=co1, fg=co4)
    title.grid(row=0, column=0, columnspan=3, sticky=NSEW)
    sep = Label(frameRight, width=400, height=1, anchor=NW, font=('Verdana 1'), bg=co3, fg=co1)
    sep.grid(row=1, column=0, columnspan=3, sticky=NSEW)
    dados = []
    books_on_loan = get_books_on_loan()
    for book in books_on_loan:
        # Formata os dados conforme desejado: [ID do empréstimo, Título, Nome completo do usuário, Data de empréstimo, Data de devolução]
        dado = [f"{book[2]}", f"{book[0]}", f"{book[1]} {book[3]}", f"{book[4]}", f"{book[5]}"]
        dados.append(dado)
    list_header = ['ID', 'Titulo', 'Nome do usuário', 'D.emprestimo', 'D.devolução']
    global tree
    tree = ttk.Treeview(frameRight, selectmode="extended", columns=list_header, show="headings")
    vsb = ttk.Scrollbar(frameRight, orient="vertical", command=tree.yview)
    hsb = ttk.Scrollbar(frameRight, orient="horizontal", command=tree.xview)
    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
    tree.grid(column=0, row=2, sticky='nsew')
    vsb.grid(column=1, row=2, sticky='ns')
    hsb.grid(column=0, row=3, sticky='ew')
    frameRight.grid_rowconfigure(0, weight=12)
    hd = ["nw", "nw", "ne", "nw", "ne"]
    widths = [20, 175, 120, 90, 90]
    n = 0
    for col in list_header:
        tree.heading(col, text=col, anchor='nw')
        tree.column(col, width=widths[n], anchor=hd[n])
        n += 1
    for item in dados:
        tree.insert('', 'end', values=item)

window.mainloop()
