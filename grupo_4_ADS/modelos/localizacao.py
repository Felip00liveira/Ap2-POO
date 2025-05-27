from sqlalchemy import Column, Integer, String, ForeignKey

from modelos.base import Base

class Localizacao(Base.Base, Base):
    __tablename__ = "localizacao"
    localizacao = Column(String(100), primary_key=True)
    numero_dep = Column(Integer, primary_key=True)