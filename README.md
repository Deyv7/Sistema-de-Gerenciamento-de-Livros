```markdown
# Sistema-de-Gerenciamento-de-Livros

## Descrição
O **Sistema de Gerenciamento de Livros** é uma aplicação desenvolvida em Python que possibilita o cadastro e o gerenciamento de livros, usuários e empréstimos para uma biblioteca. O sistema utiliza:
- **SQLite3** para armazenamento dos dados.
- **Tkinter** para a interface gráfica.
- **Pillow (PIL)** para manipulação de imagens utilizadas nos botões e ícones.

## Funcionalidades
- **Cadastro de Livros:** Insere novos livros com informações como título, autor, editora, ano de publicação e ISBN.
- **Cadastro de Usuários:** Permite o cadastro de novos usuários, registrando dados como primeiro nome, sobrenome, endereço, e-mail e telefone.
- **Empréstimos:** Registra e gerencia o empréstimo de livros.
- **Visualização:** Exibe os registros de livros, usuários e empréstimos por meio de tabelas e interface gráfica intuitiva.

## Tecnologias Utilizadas
- Python 3.12.4
- Tkinter
- SQLite3
- Pillow (PIL)

## Estrutura do Projeto

Sistema-de-Gerenciamento-de-Livros/
├── Livro/
│   ├── view.py       # Funções de conexão com o banco de dados, inserção e consulta de dados.
│   ├── main.py       # Arquivo principal que inicia a interface gráfica e controla o fluxo da aplicação.
│   └── ...           # Outros módulos ou scripts do sistema
├── images/
│   ├── save.png      # Imagem utilizada para o botão de salvar
│   └── ...           # Outras imagens ou ícones
└── README.md         # Este arquivo


## Instalação e Execução

1. **Clone o repositório:**
   ```bash
   git clone https://seu-repositorio-url/Sistema-de-Gerenciamento-de-Livros.git
   ```
2. **Acesse a pasta do projeto:**
   ```bash
   cd Sistema-de-Gerenciamento-de-Livros
   ```
3. **Instale as dependências (caso necessário):**
   ```bash
   pip install pillow
   ```
4. **Execute a aplicação:**
   - Se o arquivo principal estiver em `Livro/main.py`:
     ```bash
     python Livro/main.py
     ```

## Uso
- **Menu Principal:** A partir da interface gráfica, selecione as opções disponíveis para cadastrar novos usuários, livros ou realizar empréstimos.
- **Cadastro de Usuários:** Preencha os campos obrigatórios (primeiro nome, sobrenome, endereço, e-mail e telefone) e clique em "Salvar" para registrar o usuário.
- **Visualização de Dados:** Utilize as opções do menu para visualizar os registros existentes, que são apresentados em tabelas com rolagem.

## Contribuição
Contribuições são muito bem-vindas!  
Sinta-se à vontade para abrir issues ou enviar pull requests para melhorias ou correções.

## Licença
Distribuído sob a [MIT License](LICENSE).  
Veja o arquivo [LICENSE](LICENSE) para mais informações.
