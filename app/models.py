from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)

class Disciplina(Base):
    __tablename__ = "disciplinas"
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, unique=True, index=True)
    codigo = Column(String, unique=True)
    carga_horaria = Column(Integer)
    # Relacionamento
    turmas = relationship("Turma", back_populates="disciplina")

class Professor(Base):
    __tablename__ = "professores"
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    cpf = Column(String, unique=True)
    telefone = Column(String, nullable=True)
    # Relacionamento
    turmas = relationship("Turma", back_populates="professor")

class Turma(Base):
    __tablename__ = "turmas"
    id = Column(Integer, primary_key=True, index=True)
    codigo_turma = Column(String, unique=True, index=True) # Ex: 2026.1-MAT
    semestre = Column(String) # Ex: 2026.1
    
    # Foreign Keys
    disciplina_id = Column(Integer, ForeignKey("disciplinas.id"))
    professor_id = Column(Integer, ForeignKey("professores.id"))
    
    # Relacionamentos
    disciplina = relationship("Disciplina", back_populates="turmas")
    professor = relationship("Professor", back_populates="turmas")
    alunos = relationship("Aluno", back_populates="turma")

class Aluno(Base):
    __tablename__ = "alunos"
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, index=True)
    matricula = Column(String, unique=True, index=True)
    email = Column(String)
    cpf = Column(String, unique=True)
    data_nascimento = Column(Date, nullable=True)
        
    turma_id = Column(Integer, ForeignKey("turmas.id"), nullable=True)
    
    # Relacionamento
    turma = relationship("Turma", back_populates="alunos")
