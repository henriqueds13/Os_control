class Produto():
    def __init__(self, id_fabr, descricao, qtd=0, marca='', valor_compra=0, valor_venda=0,
               obs='', localizacao='', categoria='', un_medida='', estoque_min=0, caixa_peca=0, revendedor_id=0,
               utilizado = ''):
        self.__id_fabr = id_fabr
        self.__descricao = descricao
        self.__qtd = qtd
        self.__marca = marca
        self.__valor_compra = valor_compra
        self.__valor_venda = valor_venda
        self.__obs = obs
        self.__localizacao = localizacao
        self.__categoria = categoria
        self.__un_medida = un_medida
        self.__estoque_min = estoque_min
        self.__caixa_peca = caixa_peca
        self.__revendedor_id = revendedor_id
        self.__utilizado = utilizado

    @property
    def categoria(self):
        return self.__categoria

    @property
    def unMedida(self):
        return self.__un_medida

    @property
    def estoqueMin(self):
        return self.__estoque_min

    @property
    def caixaPeca(self):
        return self.__caixa_peca

    @property
    def revendedorId(self):
        return self.__revendedor_id

    @property
    def utilizado(self):
        return self.__utilizado

    @property
    def id_fabr(self):
        return self.__id_fabr

    @property
    def qtd(self):
        return self.__qtd

    @property
    def descricao(self):
        return self.__descricao

    @property
    def marca(self):
        return self.__marca

    @property
    def valor_compra(self):
        return self.__valor_compra

    @property
    def valor_venda(self):
        return self.__valor_venda

    @property
    def margem_lucro(self):
        return self.__margem_lucro

    @property
    def obs(self):
        return self.__obs

    @property
    def localizacao(self):
        return self.__localizacao

    @categoria.setter
    def categoria(self, categoria):
        self.__categoria = categoria

    @unMedida.setter
    def unMedida(self, un_medida):
        self.__un_medida = un_medida

    @estoqueMin.setter
    def estoqueMin(self, estoque):
        self.__estoque_min = estoque

    @revendedorId.setter
    def revendedorId(self, revendedor):
        self.__revendedor_id = revendedor

    @utilizado.setter
    def utlizado(self, utililizado):
        self.__utilizado = utililizado

    @id_fabr.setter
    def id_fabr(self, id_fabr):
        self.__id_fabr = id_fabr

    @id_fabr.setter
    def id_fabr(self, id_fabr):
        self.__id_fabr = id_fabr

    @descricao.setter
    def descricao(self, desc):
        self.__descricao = desc

    @qtd.setter
    def qtd(self, qtd):
        self.__qtd = qtd

    @marca.setter
    def marca(self, marca):
        self.__marca = marca

    @valor_compra.setter
    def valor_compra(self, valor):
        self.__valor_compra = valor

    @valor_venda.setter
    def valor_venda(self, valor):
        self.__valor_venda = valor

    @margem_lucro.setter
    def margem_lucro(self, margem):
        self.__margem_lucro = margem

    @obs.setter
    def obs(self, obs):
        self.__obs = obs

    @localizacao.setter
    def localizacao(self, localizacao):
        self.__localizacao = localizacao




