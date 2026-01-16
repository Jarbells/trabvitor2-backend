from pydantic import BaseModel
from typing import Optional, List
from datetime import date

# --- 1. User ---
class UserCreate(BaseModel):
    email: str
    password: str

class UserResponse(BaseModel):
    id: int
    email: str
    class Config:
        orm_mode = True

class Token(BaseModel):
    access_token: str
    token_type: str

# --- 2. Disciplina ---
class DisciplinaBase(BaseModel):
    nome: str
    codigo: str
    carga_horaria: int

class DisciplinaCreate(DisciplinaBase):
    pass

class DisciplinaResponse(DisciplinaBase):
    id: int
    class Config:
        orm_mode = True

# --- 3. Professor ---
class ProfessorBase(BaseModel):
    nome: str
    email: str
    cpf: str
    telefone: Optional[str] = None

class ProfessorCreate(ProfessorBase):
    pass

class ProfessorResponse(ProfessorBase):
    id: int
    class Config:
        orm_mode = True

# --- 4. Turma ---
class TurmaBase(BaseModel):
    codigo_turma: str
    semestre: str
    disciplina_id: int
    professor_id: int

class TurmaCreate(TurmaBase):
    pass

class TurmaResponse(TurmaBase):
    id: int
    # Podemos aninhar respostas para mostrar detalhes
    disciplina: Optional[DisciplinaResponse] = None 
    professor: Optional[ProfessorResponse] = None
    class Config:
        orm_mode = True

# --- 5. Aluno ---
class AlunoBase(BaseModel):
    nome: str
    matricula: str
    email: str
    cpf: str
    data_nascimento: Optional[date] = None
    turma_id: Optional[int] = None

class AlunoCreate(AlunoBase):
    pass

class AlunoResponse(AlunoBase):
    id: int
    turma: Optional[TurmaResponse] = None # Mostra detalhes da turma
    class Config:
        orm_mode = True
