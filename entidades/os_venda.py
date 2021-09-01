class OsVenda():
    def __init(self, id_prod, operador, qtd=0, form_pag='', desconto=None,id_cliente=None ):
        self.__id_prod = id_prod
        self.__qtd = qtd
        self.__form_pag = form_pag
        self.__desconto = desconto
        self.__operador = operador
        self.__id_cliente = id_cliente
        self.__subvalor = 0
        self.__valor_final = 0

    @property
    def id_prod(self):
        return self.__id_prod

    @property
    def qtd(self):
        return self.__qtd

    @property
    def form_pag(self):
        return self.__form_pag

    @property
    def desconto(self):
        return self.__desconto

    @property
    def operador(self):
        return self.__operador

    @property
    def id_cliente(self):
        return self.__id_cliente

    @property
    def subvalor(self):
        return self.__subvalor

    @property
    def valor_final(self):
        return self.__valor_final

    @id_prod.setter
    def id_prod(self, id):
        self.__id_prod = id

    @qtd.setter
    def qtd(self, qtd):
        self.qtd = qtd

    @form_pag.setter
    def form_pag(self, pag):
        self.__form_pag = pag

    @desconto.setter
    def desconto(self, desc):
        self.__desconto = desc

    @operador.setter
    def operador(self, op):
        self.__operador = op

    @id_cliente.setter
    def id_cliente(self, id):
        self.__id_cliente = id

    @subvalor.setter
    def subvalor(self, valor):
        self.__subvalor = valor

    @valor_final.setter
    def valor_final(self, valor):
        self.__valor_final = valor
