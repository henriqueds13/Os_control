class Produto():
    def __init__(self, id_fabr, descricao, qtd=0, marca='', valor_compra=0, valor_venda=0,
               obs='', localizacao=''):
        self.__id_fabr = id_fabr
        self.__descricao = descricao
        self.__qtd = qtd
        self.__marca = marca
        self.__valor_compra = valor_compra
        self.__valor_venda = valor_venda
        self.__obs = obs
        self.__localizacao = localizacao

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




