from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# PARA SQLITE. SE FOSSE POSTGREESQL SERIA: postgresql://user:password@localhost/dbname
SQLALCHEMY_DATABASE_URL = "sqlite:///./gestao_escolar.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# DEPENDÊNCIA PARA OBTER A SESSÃO DO BANCO EM CADA REQUISIÇÃO
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
