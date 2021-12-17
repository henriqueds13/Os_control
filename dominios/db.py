from sqlalchemy import Column, String, Integer, ForeignKey, Float, Table, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from fabricas import fabrica_conexao

fabrica = fabrica_conexao.FabricaConexão()
engine = fabrica.conectar()

Base = declarative_base()

produto_os = Table('produto_os', Base.metadata,
                   Column('id_produto', Integer, ForeignKey('produto.id_prod')),
                   Column('id_os', Integer, ForeignKey('ordem_de_servico.id'))
                   )
produto_venda = Table('produto_venda', Base.metadata,
                      Column('id_produto', Integer, ForeignKey('produto.id_prod')),
                      Column('id_venda', Integer, ForeignKey('os_venda.id_venda'))
                      )


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
    tel_comercial = Column(String(15), nullable=True)
    indicacao = Column(String(15), nullable=True)

    oss = relationship('OS', back_populates='cliente', cascade='delete')




class OS(Base):
    __tablename__ = 'ordem_de_servico'
    id = Column(Integer, primary_key=True)
    equipamento = Column(String(20), nullable=False)
    marca = Column(String(15), nullable=False)
    modelo = Column(String(15))
    n_serie = Column(String(20))
    chassi = Column(String(15))
    tensao = Column(Integer)
    defeito = Column(String(50))
    estado_aparelho = Column(String(50))
    acessorios = Column(String(50))
    status = Column(String(15))
    andamento = Column(String(500))
    data_entrada = Column(Date)
    hora_entrada = Column(String(10))
    dias = Column(String(9))
    data_orc = Column(Date)
    conclusão = Column(Date)
    operador = Column(String(20))
    log = Column(String(500))
    codigo1 = Column(String(15))
    codigo2 = Column(String(15))
    codigo3 = Column(String(15))
    codigo4 = Column(String(15))
    codigo5 = Column(String(15))
    codigo6 = Column(String(15))
    codigo7 = Column(String(15))
    codigo8 = Column(String(15))
    codigo9 = Column(String(15))
    caixa_peca1 = Column(Float)
    caixa_peca2 = Column(Float)
    caixa_peca3 = Column(Float)
    caixa_peca4 = Column(Float)
    caixa_peca5 = Column(Float)
    caixa_peca6 = Column(Float)
    caixa_peca7 = Column(Float)
    caixa_peca8 = Column(Float)
    caixa_peca9 = Column(Float)
    caixa_peca_total = Column(Float)
    desc_serv1 = Column(String(50))
    desc_serv2 = Column(String(50))
    desc_serv3 = Column(String(50))
    desc_serv4 = Column(String(50))
    desc_serv5 = Column(String(50))
    desc_serv6 = Column(String(50))
    desc_serv7 = Column(String(50))
    desc_serv8 = Column(String(50))
    desc_serv9 = Column(String(50))
    qtd1 = Column(Integer)
    qtd2 = Column(Integer)
    qtd3 = Column(Integer)
    qtd4 = Column(Integer)
    qtd5 = Column(Integer)
    qtd6 = Column(Integer)
    qtd7 = Column(Integer)
    qtd8 = Column(Integer)
    qtd9 = Column(Integer)
    valor_uni1 = Column(Float)
    valor_uni2 = Column(Float)
    valor_uni3 = Column(Float)
    valor_uni4 = Column(Float)
    valor_uni5 = Column(Float)
    valor_uni6 = Column(Float)
    valor_uni7 = Column(Float)
    valor_uni8 = Column(Float)
    valor_uni9 = Column(Float)
    valor_tot1 = Column(Float)
    valor_tot2 = Column(Float)
    valor_tot3 = Column(Float)
    valor_tot4 = Column(Float)
    valor_tot5 = Column(Float)
    valor_tot6 = Column(Float)
    valor_tot7 = Column(Float)
    valor_tot8 = Column(Float)
    valor_tot9 = Column(Float)
    desconto = Column(Float)
    valor_mao_obra = Column(Float)
    total = Column(Float)
    obs1 = Column(String(30))
    obs2 = Column(String(30))
    obs3 = Column(String(30))
    defeitos = Column(String(500))
    cheque = Column(Float)
    ccredito = Column(Float)
    cdebito = Column(Float)
    pix = Column(Float)
    dinheiro = Column(Float)
    outros = Column(Float)
    obs_pagamento1 = Column(String(50))
    obs_pagamento2 = Column(String(50))
    obs_pagamento3 = Column(String(50))
    data_garantia = Column(Date)
    notaFiscal = Column(Integer)
    loja = Column(String(50))
    garantia_compl = Column(Integer)
    data_compra = Column(Date)
    aparelho_na_oficina = Column(Integer)

    tecnico_id = Column(Integer, ForeignKey('tecnico.id'))
    tecnico = relationship('Tecnico', back_populates='ostec')

    cliente_id = Column(Integer, ForeignKey('cliente.id'), nullable=False)
    cliente = relationship('Cliente', back_populates='oss')

    produtos = relationship('Produto', secondary='produto_os', back_populates='os_prod')

    def __repr__(self):
        return f"[Equipamento: {self.equipamento} / Marca: {self.marca} / Modelo: {self.modelo} / Tensao: {self.tensao} / defeito: {self.defeito} / tecnico: {self.tecnico}]"


class Tecnico(Base):
    __tablename__ = 'tecnico'
    id = Column(Integer, primary_key=True)
    nome = Column(String(30), nullable=False)
    senha_tecnico = Column(Integer, nullable=False)

    ostec = relationship('OS', back_populates='tecnico')

    def __repr__(self):
        return f"Nome: {self.nome}  Senha: {self.senha_tecnico}"



class OsVenda(Base):
    __tablename__ = 'os_venda'
    id_venda = Column(Integer, primary_key=True)
    id_cliente = Column(Integer, ForeignKey('cliente.id'))
    id_prod = Column(Integer, nullable=False)
    qtd = Column(Integer, nullable=False)
    desconto = Column(Integer)
    form_pag = Column(String(20), nullable=False)
    subvalor = Column(Integer, nullable=False)
    valor_final = Column(Integer, nullable=False)

    produto = relationship('Produto', secondary='produto_venda', back_populates='venda_prod')


class Produto(Base):
    __tablename__ = 'produto'
    id_prod = Column(Integer, primary_key=True)
    id_fabr = Column(Integer)
    descricao = Column(String(50), nullable=False)
    qtd = Column(Integer, nullable=False)
    marca = Column(String(20))
    valor_compra = Column(Integer)
    valor_venda = Column(Integer)
    obs = Column(String(50), nullable=True)
    localizacao = Column(String(15))

    os_prod = relationship('OS', secondary='produto_os', back_populates='produtos')
    venda_prod = relationship('OsVenda', secondary='produto_venda', back_populates='produto')

    def __repr__(self):
        return f"Produto: {self.descricao} Quantidade: {self.qtd} Valor: {self.valor_venda}"

Base.metadata.create_all(engine)
