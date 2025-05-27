from sqlalchemy import Column, Integer, Float, String, Date, ForeignKey

from modelos.base import Base

class Empregado(Base.Base, Base):
    __tablename__ = "empregado"
    nss = Column(Integer, primary_key=True)
    pnome = Column(String(50), nullable=False)
    mnome = Column(String(50))
    snome = Column(String(50), nullable=False)
    sexo = Column(String(1))
    datanasc = Column(Date)
    salario = Column(Float)
    endereco = Column(String)
    numero_dep = Column(Integer, ForeignKey("departamento.numero", use_alter=True, name="fk_empregado_departamento"), nullable=True)
    nss_supervisor = Column(Integer, ForeignKey('empregado.nss'), nullable=True)