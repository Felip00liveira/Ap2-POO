from sqlalchemy import Column, Integer, String, Date, ForeignKey

from modelos.base import Base

class Dependente(Base.Base, Base):
    __tablename__ = "dependente"
    nss_emp = Column(Integer, primary_key=True)
    nome = Column(String(100), primary_key=True)
    sexo = Column(String(1))
    datanasc = Column(Date)
    tiporel = Column(String(50))