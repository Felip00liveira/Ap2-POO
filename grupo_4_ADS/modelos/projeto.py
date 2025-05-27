from sqlalchemy import Column, Integer, String, ForeignKey

from modelos.base import Base

class Projeto(Base.Base, Base):
    __tablename__ = "projeto"
    numero = Column(Integer, primary_key=True)
    nome = Column(String(100), nullable=False)
    localizacao = Column(String(100))
    numero_dep = Column(Integer, ForeignKey('departamento.numero'), nullable=True)