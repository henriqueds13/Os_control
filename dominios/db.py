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

class OS(Base):
    __tablename__ = 'ordem_de_servico'
    id = Column(Integer, primary_key=True)
    equipamento = Column(String(20), nullable=False)
    marca = Column(String(15), nullable=False)
    modelo = Column(String(15))
    n_serie = Column(String(20))
    tensao = Column(Integer)
    defeito = Column(String(50))
    estado_aparelho = Column(String(50))
    acessorios = Column(String(50))
    status = Column(String(15))
    desc_serv1 = Column(String(50))
    desc_serv2 = Column(String(50))
    desc_serv3 = Column(String(50))
    desc_serv4 = Column(String(50))
    desc_serv5 = Column(String(50))
    desc_serv6 = Column(String(50))
    qtd1 = Column(Integer)
    qtd2 = Column(Integer)
    qtd3 = Column(Integer)
    qtd4 = Column(Integer)
    qtd5 = Column(Integer)
    qtd6 = Column(Integer)
    valor_uni1 = Column(Float)
    valor_uni2 = Column(Float)
    valor_uni3 = Column(Float)
    valor_uni4 = Column(Float)
    valor_uni5 = Column(Float)
    valor_uni6 = Column(Float)
    desconto = Column(Float)
    valor_mao_obra = Column(Float)
    obs1 = Column(String(30))
    obs2 = Column(String(30))
    obs3 = Column(String(30))

    tecnico_id = Column(Integer, ForeignKey('tecnico.id'))
    cliente_id = Column(Integer, ForeignKey('cliente.id'), nullable=False)

    def __repr__(self):
        return f"Equipamento"

class Tecnico(Base):
    __tablename__ = 'tecnico'
    id = Column(Integer, primary_key=True)
    nome = Column(String(30), nullable=False)
    senha_tecnico = Column(Integer, nullable=False)



Base.metadata.create_all(engine)