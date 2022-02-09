class ProdutoVenda():
    def __init__(self, id_fabr, descricao, qtd, valor_uni, id_estoque, id_venda):
        self.__id_fabr = id_fabr
        self.__descricao = descricao
        self.__qtd = qtd
        self.__valor_un = valor_uni
        self.__id_estoque = id_estoque
        self.__id_venda = id_venda

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
    def valor_unit(self):
        return self.__valor_un

    @property
    def id_estoque(self):
        return self.__id_estoque

    @property
    def id_venda(self):
        return self.__id_venda

    @id_fabr.setter
    def id_fabr(self, id_fabr):
        self.__id_fabr = id_fabr

    @id_fabr.setter
    def id_fabr(self, id_fabr):
        self.__id_fabr = id_fabr

    @descricao.setter
    def descricao(self, desc):
        self.__descricao = desc

    @valor_unit.setter
    def valor_unit(self, valor):
        self.__valor_un = valor

    @id_estoque.setter
    def id_estoque(self, id):
        self.__id_estoque = id

    @id_venda.setter
    def id_venda(self, id):
        self.__id_venda = id
