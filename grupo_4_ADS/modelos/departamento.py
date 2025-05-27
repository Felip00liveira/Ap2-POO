from sqlalchemy import Column, Integer, String, Date, ForeignKey

from modelos.base import Base

class Departamento(Base.Base, Base):
    __tablename__ = "departamento"
    numero = Column(Integer, primary_key=True)
    nome = Column(String(100), nullable=False)
    nro_emp = Column(Integer)
    nss_emp = Column(Integer, ForeignKey("empregado.nss", use_alter=True, name="fk_departamento_empregado"), nullable=True)
    datainicio = Column(Date)