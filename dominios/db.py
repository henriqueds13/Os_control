from sqlalchemy import Column, String, Integer, ForeignKey, Float, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from fabricas import fabrica_conexao

fabrica = fabrica_conexao.FabricaConexão()
engine = fabrica.conectar()

Base = declarative_base()


class Cliente(Base):
    __tablename__ = 'cliente'
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(50), nullable=False)
    operador = Column(Integer, nullable=False)
    celular = Column(String(15), nullable=True)
    cpf_cnpj = Column(String(18), nullable=True)
    tel_fixo = Column(String(15), nullable=True)
    rg_ie = Column(String(15), nullable=True)
    logradouro = Column(String(50), nullable=True)
    uf = Column(String(2), nullable=True)
    bairro = Column(String(20), nullable=True)
    complemento = Column(String(30), nullable=True)
    cep = Column(Integer, nullable=True)
    cidade = Column(String(15), nullable=True)
    email = Column(String(50), nullable=True)
    whats = Column(String(15), nullable=True)
    contato = Column(String(15), nullable=True)
    indicacao = Column(String(15), nullable=True)

    def __repr__(self):
        return f"Cliente: Id {self.id},nome: {self.nome}, celular: {self.celular}, endereço: {self.logradouro} {self.bairro}/" \
               f"{self.cidade}, {self.uf}"


Base.metadata.create_all(engine)