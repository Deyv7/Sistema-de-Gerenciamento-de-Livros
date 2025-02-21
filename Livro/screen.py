from tkinter import *
from tkinter import Tk, ttk
from PIL import Image, ImageTk
from tkinter import messagebox

# importando as funções da VIEW.PY
from view import *

# Cores
co0 = "#2e2d2b"  # Preta
co1 = "#ffffff"  # Branca
co2 = "#4fa882"  # Verde
co3 = "#38576b"  # Valor
co4 = "#403d3d"  # Letra
co5 = "#0e6636"  # Profit
co6 = "#e9a178"  #
co7 = "#3fbfb9"  # Verde
co8 = "#263238"  # Verde
co9 = "#9e9df5"  # Verde
co10 = "#6e8faf" #
co11 = "#f2f4f2" #

# Crinado a Janela ----------------------------------

window = Tk()
window.title("")
window.geometry('770x330')
window.configure(background=co1)
window.resizable(width=FALSE, height=FALSE)

style= ttk.Style(window)
style.theme_use("clam")

#Frame -----------------------------------------------

frameUP = Frame(window, width=770, height=50, bg=co6, relief="flat")
frameUP.grid(row=0, column=0, columnspan=2, sticky=NSEW)

frameLeft = Frame(window, width=150, height=265, bg=co4, relief="solid")
frameLeft.grid(row=1, column=0, sticky=NSEW)

frameRight = Frame(window, width=600, height=265, bg=co1, relief="raised")
frameRight.grid(row=1, column=1, sticky=NSEW)

#Logo -----------------------------------------------
# Abrindo Imagem Título no Cabeçalho
app_img = Image.open('./images/logo.png')
app_img = app_img.resize(((40, 40)))
app_img = ImageTk.PhotoImage(app_img)

app_logo = Label(frameUP, image=app_img, width=1000, compound=LEFT, padx=5, anchor=NW, bg=co6, fg=co1)
app_logo.place(x=5, y=0)

app_=Label(frameUP, text="Sistema de Gerenciamento de Livros", compound=LEFT, padx=5, anchor=NW, font=('Verdana 15 bold'), bg=co6, fg=co1)
app_.place(x=50, y=7)

#Linha de borda do cabeçalho
app_line = Label(frameUP, width=770, padx=5, anchor=NW, font=('Verdana 1'), bg=co3, fg=co1)
app_line.place(x=0, y=47)

#Menu -----------------------------------------------

#Novo Usuário
img_user = Image.open('./images/user.png')
img_user = img_user.resize((18, 18))
img_user = ImageTk.PhotoImage(img_user)
b_user = Button(frameLeft, image=img_user, text="Novo Usuário", command=lambda:control('novo usuario'), compound=LEFT, anchor=NW, font=('Ivy 11'), overrelief=RIDGE, relief=GROOVE, bg=co4, fg=co1)
b_user.grid(row=0, column=0, sticky=NSEW, padx=5, pady=6)

#Novo Livro ------------------------------------------
img_book = Image.open('./images/book.png')
img_book = img_book.resize((18, 18))
img_book = ImageTk.PhotoImage(img_book)
b_book = Button(frameLeft, image=img_book, text="Novo Livro", compound=LEFT, anchor=NW, font=('Ivy 11'), overrelief=RIDGE, relief=GROOVE, bg=co4, fg=co1)
b_book.grid(row=1, column=0, sticky=NSEW, padx=5, pady=6)

# Ver Usuário ------------------------------------------
img_see_user = Image.open('./images/user.png')
img_see_user = img_see_user.resize((18, 18))
img_see_user = ImageTk.PhotoImage(img_see_user)
b_see_user = Button(frameLeft, image=img_see_user, command=lambda:control('ver usuarios'), text="Exibir todos os Usuários", compound=LEFT, anchor=NW, font=('Ivy 11'), overrelief=RIDGE, relief=GROOVE, bg=co4, fg=co1)
b_see_user.grid(row=2, column=0, sticky=NSEW, padx=5, pady=6)

# Realizar um Emprestimo ----------------------------
img_loan = Image.open('./images/add.png')
img_loan = img_loan.resize((18, 18))
img_loan = ImageTk.PhotoImage(img_loan)
b_loan = Button(frameLeft, image=img_loan, text="Realizar um Emprestimo", compound=LEFT, anchor=NW, font=('Ivy 11'), overrelief=RIDGE, relief=GROOVE, bg=co4, fg=co1)
b_loan.grid(row=4, column=0, sticky=NSEW, padx=5, pady=6)

# Devolução de Empréstimo ----------------------------
img_devolution = Image.open('./images/add.png')
img_devolution = img_devolution.resize((18, 18))
img_devolution = ImageTk.PhotoImage(img_devolution)
b_devolution = Button(frameLeft, image=img_devolution, text="Devolução de Empréstimo", compound=LEFT, anchor=NW, font=('Ivy 11'), overrelief=RIDGE, relief=GROOVE, bg=co4, fg=co1)
b_devolution.grid(row=5, column=0, sticky=NSEW, padx=5, pady=6)

# Livros emprestados no momento ----------------------
img_books_on_loan = Image.open('./images/add.png')
img_books_on_loan = img_books_on_loan.resize((18, 18))
img_books_on_loan = ImageTk.PhotoImage(img_books_on_loan)
b_books_on_loan = Button(frameLeft, image=img_books_on_loan, text="Livros emprestados no momento", compound=LEFT, anchor=NW, font=('Ivy 11'), overrelief=RIDGE, relief=GROOVE, bg=co4, fg=co1)
b_books_on_loan.grid(row=6, column=0, sticky=NSEW, padx=5, pady=6)

# Função para controlar o MENU -----------------------
def control(i):
    #Novo usuário
    if i == 'novo usuario':
        for widget in frameRight.winfo_children():
            widget.destroy()
        #chamando a função novo usuário
        new_user()

    #Novo Livro
    if i == 'novo livro':
        for widget in frameRight.winfo_children():
            widget.destroy()
        #chamando a função novo livro
        pass

    #Ver Usuários
    if i == 'ver usuarios':
        for widget in frameRight.winfo_children():
            widget.destroy()
        #chamando a função ver usuários
        see_user()

    #Ver Livros
    if i == 'ver livros':
        for widget in frameRight.winfo_children():
            widget.destroy()
        #chamando a função ver livros
        pass

# Linha de borda do cabeçalho ------------------------
app_line = Label(frameUP, width=770, padx=5, anchor=NW, font=('Verdana 1'), bg=co3, fg=co1)
app_line.place(x=0, y=47)

# Novo Usuário ------------------------------------------
def new_user():
    global img_save
    def add_user():
        first_name = e_f_name.get()
        last_name = e_l_name.get()
        address = e_address.get()
        email = e_email.get()
        phone = e_phone.get()

        lista = [first_name,last_name,address,email,phone]

        #verificando caso um campo esteja vazio ou não
        for i in lista:
            if i == '':
                messagebox.showerror("Erro", "Preencha todos os campos!")
                return
        # Inserindo os dados no DB
        insert_user(first_name, last_name, address, email, phone)
        messagebox.showinfo("Sucesso", "Usuário cadastrado com sucesso!")
        print(f"Usuário {first_name} {last_name} cadastrado com sucesso!")
        # Limpando os campos de entradas
        e_f_name.delete(0, END)
        e_l_name.delete(0, END)
        e_address.delete(0, END)
        e_email.delete(0, END)
        e_phone.delete(0, END)

    #Criando o frame de inserção de usuários
    app_ = Label(frameRight, text="Inserir Novo Usuário", compound=LEFT, padx=5, pady=10, anchor=NW, font=('Verdana 15 bold'), bg=co1, fg=co4)
    app_.grid(row=0, column=0, columnspan=4, sticky=NSEW)
    app_line = Label(frameRight, width=400, height=1, anchor=NW, font=('Verdana 1'), bg=co3, fg=co1)
    app_line.grid(row=1, column=0, columnspan=4, sticky=NSEW)
    #Primeiro Nome
    l_p_name = Label(frameRight, text="Primeiro Nome ", anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
    l_p_name.grid(row=2, column=0, sticky=NSEW, padx=5, pady=5)
    e_f_name = Entry(frameRight, width=25, justify='left', relief='solid')
    e_f_name.grid(row=2, column=1, sticky=NSEW, padx=5, pady=5)
    #Sobrenome
    l_l_name = Label(frameRight, text="Sobrenome ", anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
    l_l_name.grid(row=3, column=0, sticky=NSEW, padx=5, pady=5)
    e_l_name = Entry(frameRight, width=25, justify='left', relief='solid')
    e_l_name.grid(row=3, column=1, sticky=NSEW, padx=5, pady=5)
    #Endereço
    l_address = Label(frameRight, text="Endereço do usuário ", anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
    l_address.grid(row=4, column=0, sticky=NSEW, padx=5, pady=5)
    e_address = Entry(frameRight, width=25, justify='left', relief='solid')
    e_address.grid(row=4, column=1, sticky=NSEW, padx=5, pady=5)
    #E-mail
    l_email = Label(frameRight, text="E-mail ", anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
    l_email.grid(row=5, column=0, sticky=NSEW, padx=5, pady=5)
    e_email = Entry(frameRight, width=25, justify='left', relief='solid')
    e_email.grid(row=5, column=1, sticky=NSEW, padx=5, pady=5)
    #Telefone
    l_phone = Label(frameRight, text="Telefone ", anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
    l_phone.grid(row=6, column=0, sticky=NSEW, padx=5, pady=5)
    e_phone = Entry(frameRight, width=25, justify='left', relief='solid')
    e_phone.grid(row=6, column=1, sticky=NSEW, padx=5, pady=5)
    #Botão Salvar
    img_save = Image.open('./images/save.png')
    img_save = img_save.resize((18, 18))
    img_save = ImageTk.PhotoImage(img_save)
    b_save = Button(frameRight, image=img_save, compound=LEFT, width=100, anchor=NW, command=add_user, text="Salvar", bg=co1, fg=co4, overrelief=RIDGE, relief=GROOVE, font=('Ivy 11'))
    b_save.grid(row=7, column=0, columnspan=4, sticky=NSEW, padx=5, pady=5)

# Função para --->VER<--- Usuários
def see_user():
    app_ = Label(frameRight,text="Todos os usuários do banco de dados",width=50,compound=LEFT, padx=5,pady=10, relief=FLAT, anchor=NW, font=('Verdana 12'),bg=co1, fg=co4)
    app_.grid(row=0, column=0, columnspan=3, sticky=NSEW)
    l_linha = Label(frameRight, width=400, height=1,anchor=NW, font=('Verdana 1 '), bg=co3, fg=co1)
    l_linha.grid(row=1, column=0, columnspan=3, sticky=NSEW)

    dados = get_user()

    #creating a treeview with dual scrollbars
    list_header = ['ID','Nome','Sobrenome','Endereço','Email','Telefone']
    
    global tree
    
    tree = ttk.Treeview(frameRight, selectmode="extended",
                        columns=list_header, show="headings")
    
    vsb = ttk.Scrollbar(frameRight, orient="vertical", command=tree.yview)
    hsb = ttk.Scrollbar(frameRight, orient="horizontal", command=tree.xview)
    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)

    tree.grid(column=0, row=2, sticky='nsew')
    vsb.grid(column=1, row=2, sticky='ns')
    hsb.grid(column=0, row=3, sticky='ew')
    frameRight.grid_rowconfigure(0, weight=12)

    hd=["nw","nw","nw","nw","nw","nw"]
    h=[20,80,80,120,120,76,100]
    n=0

    for col in list_header:
        tree.heading(col, text=col, anchor='nw')
        #adjust the column's width to the header string
        tree.column(col, width=h[n],anchor=hd[n])
        
        n+=1

    for item in dados:
        tree.insert('', 'end', values=item)

#



window.mainloop()

