# Sistema de Gestão Escolar - API Backend

Repositório referente à **Entrega 3** da disciplina de Desenvolvimento Web (QXD0020). Este projeto contém exclusivamente a API RESTful desenvolvida em **FastAPI**, responsável pela lógica de negócios, autenticação e persistência de dados.

> **Nota:** O Frontend (protótipo React da Entrega 2) encontra-se em um repositório separado ou branch distinta e não é necessário para a execução desta API.

## Integrantes
* **[Francisco Jarbas dos Santos Sousa]**
* **[Antônia Graziely Nobre Moreira]**

---

## Tecnologias Utilizadas

* **Linguagem:** Python 3.12+
* **Framework Web:** FastAPI
* **Banco de Dados:** SQLite (via SQLAlchemy ORM)
* **Autenticação:** JWT (JSON Web Tokens) com OAuth2
* **Criptografia:** Passlib (Bcrypt)
* **Validação:** Pydantic Schemas

---

## Funcionalidades Implementadas (Entrega 3)

O backend atende aos seguintes requisitos:

1.  **Arquitetura Modular:** Código organizado em `routers`, `services`, `models` e `schemas`.
2.  **CRUD Completo (5 Entidades):**
    * **Usuários:** Registro e Login.
    * **Alunos:** Gestão de dados acadêmicos e pessoais.
    * **Professores:** Cadastro de corpo docente.
    * **Disciplinas:** Cadastro de matérias e carga horária.
    * **Turmas:** Relacionamento entre Professor, Disciplina e Semestre.
3.  **Relacionamentos:** Banco de dados relacional com chaves estrangeiras (ex: Aluno pertence a uma Turma).
4.  **Segurança:** Rotas de escrita (POST/PUT/DELETE) protegidas por Token JWT.
5.  **Documentação:** Interface interativa Swagger UI gerada automaticamente.

---

## Guia de Instalação e Execução

Siga os passos abaixo para rodar a API localmente.

### I. Clonar e Entrar na Pasta
```bash
git clone [https://github.com/Jarbells/trabvitor2-backend.git](https://github.com/Jarbells/trabvitor2-backend.git)
cd trabvitor2-backend
# Se o código estiver dentro de uma subpasta 'backend', entre nela:
# cd backend

```

### II. Criar o Ambiente Virtual (Recomendado)

```bash
# Linux/Mac
python3 -m venv venv-backend
source venv-backend/bin/activate

# Windows (PowerShell)
python -m venv venv-backend
.\venv-backend\Scripts\activate

```

### III. Instalar Dependências

```bash
pip install -r requirements.txt

```

### IV. Executar o Servidor

```bash
uvicorn app.main:app --reload

```

* O servidor iniciará em: `http://127.0.0.1:8000`
* O banco de dados `gestao_escolar.db` será criado automaticamente na raiz na primeira execução.

---

## Como Testar (Documentação Interativa)

A melhor forma de validar a entrega é através do Swagger UI.

1. Acesse **http://127.0.0.1:8000/docs** no seu navegador.
2. **Passo 1 - Criar Conta:** Vá na rota `POST /registrar` e crie um usuário.
3. **Passo 2 - Login:** Clique no botão **"Authorize"** (cadeado verde) no topo direito. Insira o email e senha criados.
4. **Passo 3 - Testar Rotas:** Com o cadeado fechado (autenticado), você pode realizar operações de CRUD em Alunos, Turmas, etc.

---

## Estrutura do Projeto

```
/
├── app/
│   ├── main.py          # Configuração principal e Rotas
│   ├── auth.py          # Lógica de Autenticação JWT
│   ├── database.py      # Conexão com Banco de Dados
│   ├── models.py        # Modelos ORM (Tabelas)
│   ├── schemas.py       # Modelos Pydantic (Validação)
│   ├── routers/         # Endpoints da API
│   └── services/        # Regras de Negócio (CRUD)
├── requirements.txt     # Lista de bibliotecas
└── README.md            # Este arquivo

```

```

```