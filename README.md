# Gestão Escolar - Backend (API)

API desenvolvida com **FastAPI** para o sistema de Gestão Escolar. Fornece serviços de autenticação, e gerenciamento de alunos e professores.

## Desenvolvido por: 
```
Francisco Jarbas dos Santos Sousa
Antônia Graziely Nobre Moreira
```

## Tecnologias

* **Python 3.10+**
* **FastAPI** (Framework Web)
* **SQLAlchemy** (ORM para Banco de Dados)
* **SQLite** (Banco de dados relacional)
* **Pydantic** (Validação de dados)
* **JWT** (Autenticação JSON Web Token)

## Instalação e Execução

### Preparar o Ambiente

Certifique-se de estar na pasta backend:

```bash
cd backend
python -m venv venv

```

Ative o ambiente virtual:

* **Linux/Mac:** `source venv/bin/activate`

### Instalar Dependências

```bash
pip install -r requirements.txt

```

### Rodar o Servidor

```bash
uvicorn app.main:app --reload

```

A API estará disponível em: `http://127.0.0.1:8000`

## Documentação Interativa

Acesse a documentação automática (Swagger UI) para testar as rotas:
**https://www.google.com/search?q=http://127.0.0.1:8000/docs**

## Como Autenticar (Testes)

1. Acesse `/docs`.
2. Use a rota **POST /registrar** para criar um usuário.
3. Clique no botão **Authorize** (cadeado) no topo.
4. Faça login com o email e senha criados.
5. Agora você tem acesso às rotas protegidas (POST, PUT, DELETE).
