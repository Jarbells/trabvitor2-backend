from pydantic import BaseModel
from typing import Optional
from datetime import date

# SCHEMAS DE AUTENTICAÇÃO
class Token(BaseModel):
    access_token: str
    token_type: str

class UserCreate(BaseModel):
    email: str
    password: str

class UserResponse(BaseModel):
    id: int
    email: str
    class Config:
        orm_mode = True

# SCHEMAS DE ALUNOS
class AlunoBase(BaseModel):
    nome: str
    matricula: str
    email: str
    cpf: str
    curso: str
    status: Optional[str] = "Ativo"
    turma: Optional[str] = None
    telefone: Optional[str] = None
    data_nascimento: Optional[date] = None
    nome_mae: Optional[str] = None
    nome_pai: Optional[str] = None
    endereco_completo: Optional[str] = None

class AlunoCreate(AlunoBase):
    pass

class AlunoUpdate(BaseModel):
    # CAMPOS OPCIONAIS PARA ATUALIZAÇÃO PARCIAL
    nome: Optional[str] = None
    email: Optional[str] = None
    status: Optional[str] = None
    curso: Optional[str] = None
    # ADICIONE OUTROS CAMPOS SE NECESSÁRIO

class AlunoResponse(AlunoBase):
    id: int
    class Config:
        orm_mode = True # PERMITE LER OS DADOS DO SQLALCHEMY

# SCHEMAS DE PROFESSORES
class ProfessorBase(BaseModel):
    nome: str
    email: str
    cpf: str
    disciplina: str
    telefone: Optional[str] = None

class ProfessorCreate(ProfessorBase):
    pass

class ProfessorUpdate(BaseModel):
    nome: Optional[str] = None
    email: Optional[str] = None
    disciplina: Optional[str] = None
    telefone: Optional[str] = None

class ProfessorResponse(ProfessorBase):
    id: int
    class Config:
        orm_mode = True
