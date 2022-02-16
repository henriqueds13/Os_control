class OsVenda():
    def __init__(self, cliente, operador, obs1, obs2, obs3, dinheiro, cheque, cdebito, ccredito, pix, outros,
               desconto, sub_total, data, hora, total):
        self.__cliente = cliente
        self.__obs1 = obs1
        self.__obs2 = obs2
        self.__obs3 = obs3
        self.__dinheiro = dinheiro
        self.__cheque = cheque
        self.__cdebito = cdebito
        self.__ccredito = ccredito
        self.__pix = pix
        self.__desconto = desconto
        self.__outros = outros
        self.__operador = operador
        self.__sub_total = sub_total
        self.__total = total
        self.__data = data
        self.__hora = hora

    @property
    def cliente(self):
        return self.__cliente

    @property
    def obs1(self):
        return self.__obs1

    @property
    def obs2(self):
        return self.__obs2

    @property
    def obs3(self):
        return self.__obs3

    @property
    def dinheiro(self):
        return self.__dinheiro

    @property
    def cheque(self):
        return self.__cheque

    @property
    def cdebito(self):
        return self.__cdebito

    @property
    def ccredito(self):
        return self.__ccredito

    @property
    def pix(self):
        return self.__pix

    @property
    def outros(self):
        return self.__outros

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
    def sub_total(self):
        return self.__sub_total

    @property
    def total(self):
        return self.__total

    @property
    def data(self):
        return self.__data

    @property
    def hora(self):
        return self.__hora

    @cliente.setter
    def cliente(self, cliente):
        self.__cliente = cliente

    @obs1.setter
    def obs1(self, obs):
        self.__obs1 = obs

    @obs2.setter
    def obs2(self, obs):
        self.__obs2 = obs

    @obs3.setter
    def obs3(self, obs):
        self.__obs3 = obs

    @dinheiro.setter
    def dinheiro(self, pag):
        self.__dinheiro = pag

    @cheque.setter
    def cheque(self, pag):
        self.__cheque = pag

    @cdebito.setter
    def cdebito(self, pag):
        self.__cdebito = pag

    @ccredito.setter
    def ccredito(self, pag):
        self.__ccredito = pag

    @pix.setter
    def pix(self, pag):
        self.__pix = pag

    @outros.setter
    def outros(self, pag):
        self.__outros = pag

    @desconto.setter
    def desconto(self, desc):
        self.__desconto = desc

    @operador.setter
    def operador(self, op):
        self.__operador = op

    @data.setter
    def data(self, data):
        self.__data = data

    @hora.setter
    def hora(self, hora):
        self.__hora = hora

    @sub_total.setter
    def sub_total(self, valor):
        self.__sub_total = valor

    @total.setter
    def total(self, valor):
        self.total = valor
