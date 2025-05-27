from sqlalchemy import Column, Integer, Float 

from modelos.base import Base

class TrabalhaEm(Base.Base, Base):
    __tablename__ = "trabalha_em"
    nss_emp = Column(Integer, primary_key=True)
    numero_proj = Column(Integer, primary_key=True)
    horas = Column(Float)