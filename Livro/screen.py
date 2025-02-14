from tkinter import *       # Importa o tkinter principal
from tkinter import ttk     # Importa o ttk para widgets modernos
from PIL import ImageTk, Image  # Para manipulação de images com Pillow

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
frameLeft.grid(row=1, column=1, sticky=NSEW)

frameRight = Frame(window, width=600, height=265, bg=co1, relief="raised")
frameRight.grid(row=1, column=1, sticky=NSEW)

#Logo -----------------------------------------------
# Abrindo Imagem Título no Cabeçalho
app_img = Image.open('./images/logo.png')
app_img = app_img.resize((40, 40))
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
img_user = img_user.resize(18, 18)
img_user = ImageTk.PhotoImage(img_user)
b_user = Button(frameLeft, image=img_user, text="Novo Usuário", compound=LEFT, anchor=NW, font=('Ivy 11'), overrelief=RIDGE, relief=GROOVE, bg=co4, fg=co1)
b_user.grid(row=0, column=0, sticky=NSEW, padx=5, pady=6)

#Novo Livro ------------------------------------------
img_book = Image.open('./images/book.png')
img_book = img_book.resize(18, 18)
img_book = ImageTk.PhotoImage(img_book)
b_book = Button(frameLeft, image=img_book, text="Novo Livro", compound=LEFT, anchor=NW, font=('Ivy 11'), overrelief=RIDGE, relief=GROOVE, bg=co4, fg=co1)
b_book.grid(row=1, column=0, sticky=NSEW, padx=5, pady=6)

# Ver Usuário ------------------------------------------
img_see_user = Image.open('./images/see_user.png')
img_see_user = img_see_user.resize(18, 18)
img_see_user = ImageTk.PhotoImage(img_see_user)
b_see_user = Button(frameLeft, image=img_see_user, text="Exibir todos os Usuários", compound=LEFT, anchor=NW, font=('Ivy 11'), overrelief=RIDGE, relief=GROOVE, bg=co4, fg=co1)
b_see_user.grid(row=2, column=0, sticky=NSEW, padx=5, pady=6)

# Realizar um Emprestimo ----------------------------
img_loan = Image.open('./images/add.png')
img_loan = img_loan.resize(18, 18)
img_loan = ImageTk.PhotoImage(img_loan)
b_loan = Button(frameLeft, image=img_loan, text="Realizar um Emprestimo", compound=LEFT, anchor=NW, font=('Ivy 11'), overrelief=RIDGE, relief=GROOVE, bg=co4, fg=co1)
b_loan.grid(row=4, column=0, sticky=NSEW, padx=5, pady=6)

# Devolução de Empréstimo ----------------------------
img_devolution = Image.open('./images/add.png')
img_devolution = img_devolution.resize(18, 18)
img_devolution = ImageTk.PhotoImage(img_devolution)
b_devolution = Button(frameLeft, image=img_devolution, text="Devolução de Empréstimo", compound=LEFT, anchor=NW, font=('Ivy 11'), overrelief=RIDGE, relief=GROOVE, bg=co4, fg=co1)
b_devolution.grid(row=5, column=0, sticky=NSEW, padx=5, pady=6)

# Livros emprestados no momento ----------------------
img_books_on_loan = Image.open('./images/add.png')
img_books_on_loan = img_books_on_loan.resize(18, 18)
img_books_on_loan = ImageTk.PhotoImage(img_books_on_loan)
b_books_on_loan = Button(frameLeft, image=img_books_on_loan, text="Livros emprestados no momento", compound=LEFT, anchor=NW, font=('Ivy 11'), overrelief=RIDGE, relief=GROOVE, bg=co4, fg=co1)
b_books_on_loan.grid(row=6, column=0, sticky=NSEW, padx=5, pady=6)

window.mainloop()