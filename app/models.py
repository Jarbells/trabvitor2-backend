from sqlalchemy import Column, Integer, String, Date
from .database import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)

class Aluno(Base):
    __tablename__ = "alunos"
    
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, index=True)
    matricula = Column(String, unique=True, index=True)
    email = Column(String)
    cpf = Column(String, unique=True)
    curso = Column(String)
    status = Column(String, default="Ativo") # ATIVO, TRANCADO, FORMANDO
    turma = Column(String, nullable=True)
    
    # DADOS PESSOAIS/EXTRAS
    telefone = Column(String, nullable=True)
    data_nascimento = Column(Date, nullable=True)
    nome_mae = Column(String, nullable=True)
    nome_pai = Column(String, nullable=True)
    
    # ENDEREÇO (SIMPLIFICADO PARA EXEMPLO)
    endereco_completo = Column(String, nullable=True)

class Professor(Base):
    __tablename__ = "professores"
    
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    cpf = Column(String, unique=True)
    disciplina = Column(String) # POSSO FAZER UMA RELAÇÃO DE DISCIPLINAS DEPOIS
    telefone = Column(String, nullable=True)
