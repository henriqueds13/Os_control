class Aluguel():
    def __init__(self, data, cliente, equipamento, caixa_peca1, caixa_peca2, caixa_peca3, caixa_peca4, caixa_peca5,
                 caixa_peca6, valor_uni1, valor_uni2, valor_uni3, valor_uni4, valor_uni5, valor_uni6, qtd1, qtd2, qtd3,
                 qtd4, qtd5, qtd6, desc_serv1, desc_serv2, desc_serv3, desc_serv4, desc_serv5, desc_serv6, obs1, obs2,
                 obs3, cheque, dinheiro, pix, outros, ccredito, cdebito, desconto, caixa_peca_total, valor_total, dias,
                 data_entrega, operador, alug_pago):

        self.__data = data
        self.__cliente = cliente
        self.__equipamento = equipamento
        self.__desconto = desconto
        self.__caixa_peca_total = caixa_peca_total
        self.__valor_total = valor_total
        self.__dias = dias
        self.__data_entrega = data_entrega
        self.__operador = operador
        self.__alug_pago = alug_pago
        self.__caixa_peca1 = caixa_peca1
        self.__caixa_peca2 = caixa_peca2
        self.__caixa_peca3 = caixa_peca3
        self.__caixa_peca4 = caixa_peca4
        self.__caixa_peca5 = caixa_peca5
        self.__caixa_peca6 = caixa_peca6
        self.__desc_serv1 = desc_serv1
        self.__desc_serv2 = desc_serv2
        self.__desc_serv3 = desc_serv3
        self.__desc_serv4 = desc_serv4
        self.__desc_serv5 = desc_serv5
        self.__desc_serv6 = desc_serv6
        self.__obs1 = obs1
        self.__obs2 = obs2
        self.__obs3 = obs3
        self.__qtd1 = qtd1
        self.__qtd2 = qtd2
        self.__qtd3 = qtd3
        self.__qtd4 = qtd4
        self.__qtd5 = qtd5
        self.__qtd6 = qtd6
        self.__valor_uni1 = valor_uni1
        self.__valor_uni2 = valor_uni2
        self.__valor_uni3 = valor_uni3
        self.__valor_uni4 = valor_uni4
        self.__valor_uni5 = valor_uni5
        self.__valor_uni6 = valor_uni6
        self.__cheque = cheque
        self.__ccredito = ccredito
        self.__cdebito = cdebito
        self.__pix = pix
        self.__dinheiro = dinheiro
        self.__outros = outros

    @property
    def data(self):
        return self.__data

    @property
    def cliente(self):
        return self.__cliente

    @property
    def valorTotal(self):
        return self.__valor_total

    @property
    def dataEntrega(self):
        return self.__data_entrega

    @property
    def alugPago(self):
        return self.__alug_pago

    @property
    def cheque(self):
        return self.__cheque

    @property
    def ccredito(self):
        return self.__ccredito

    @property
    def cdebito(self):
        return self.__cdebito

    @property
    def pix(self):
        return self.__pix

    @property
    def dinheiro(self):
        return self.__dinheiro

    @property
    def outros(self):
        return self.__outros

    @property
    def caixaPeca1(self):
        return self.__caixa_peca1

    @property
    def caixaPeca2(self):
        return self.__caixa_peca2

    @property
    def caixaPeca3(self):
        return self.__caixa_peca3

    @property
    def caixaPeca4(self):
        return self.__caixa_peca4

    @property
    def caixaPeca5(self):
        return self.__caixa_peca5

    @property
    def caixaPeca6(self):
        return self.__caixa_peca6

    @property
    def caixaPecaTotal(self):
        return self.__caixa_peca_total

    @property
    def dias(self):
        return self.__dias

    @property
    def operador(self):
        return self.__operador

    @property
    def equipamento(self):
        return self.__equipamento

    @property
    def desc_serv1(self):
        return self.__desc_serv1

    @property
    def desc_serv2(self):
        return self.__desc_serv2

    @property
    def desc_serv3(self):
        return self.__desc_serv3

    @property
    def desc_serv4(self):
        return self.__desc_serv4

    @property
    def desc_serv5(self):
        return self.__desc_serv5

    @property
    def desc_serv6(self):
        return self.__desc_serv6

    @property
    def desconto(self):
        return self.__desconto

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
    def qtd1(self):
        return self.__qtd1

    @property
    def qtd2(self):
        return self.__qtd2

    @property
    def qtd3(self):
        return self.__qtd3

    @property
    def qtd4(self):
        return self.__qtd4

    @property
    def qtd5(self):
        return self.__qtd5

    @property
    def qtd6(self):
        return self.__qtd6

    @property
    def valor_uni1(self):
        return self.__valor_uni1

    @property
    def valor_uni2(self):
        return self.__valor_uni2

    @property
    def valor_uni3(self):
        return self.__valor_uni3

    @property
    def valor_uni4(self):
        return self.__valor_uni4

    @property
    def valor_uni5(self):
        return self.__valor_uni5

    @property
    def valor_uni6(self):
        return self.__valor_uni6

    @cheque.setter
    def cheque(self, cheque):
        self.__cheque = cheque

    @ccredito.setter
    def ccredito(self, ccredito):
        self.__ccredito = ccredito

    @cdebito.setter
    def cdebito(self, cdebito):
        self.__cdebito = cdebito

    @pix.setter
    def pix(self, pix):
        self.__pix = pix

    @dinheiro.setter
    def dinheiro(self, dinheiro):
        self.dinheiro = dinheiro

    @outros.setter
    def outros(self, outros):
        self.__outros = outros

    @caixaPeca1.setter
    def caixaPeca1(self, caixa_peca1):
        self.__caixa_peca1 = caixa_peca1

    @caixaPeca2.setter
    def caixaPeca2(self, caixa_peca2):
        self.__caixa_peca2 = caixa_peca2

    @caixaPeca3.setter
    def caixaPeca3(self, caixa_peca3):
        self.__caixa_peca3 = caixa_peca3

    @caixaPeca4.setter
    def caixaPeca4(self, caixa_peca4):
        self.__caixa_peca4 = caixa_peca4

    @caixaPeca5.setter
    def caixaPeca5(self, caixa_peca5):
        self.__caixa_peca5 = caixa_peca5

    @caixaPeca6.setter
    def caixaPeca6(self, caixa_peca6):
        self.__caixa_peca6 = caixa_peca6

    @caixaPecaTotal.setter
    def caixaPecaTotal(self, caixa_total):
        self.__caixa_peca_total = caixa_total

    @data.setter
    def data(self, dat):
        self.__data = dat

    @dataEntrega.setter
    def dataEntrega(self, data):
        self.__data_entrega = data

    @dias.setter
    def dias(self, dias):
        self.__dias = dias

    @operador.setter
    def operador(self, operador):
        self.__operador = operador

    @equipamento.setter
    def equipamento(self, equipamento):
        self.__equipamento = equipamento

    @cliente.setter
    def cliente(self, cli):
        self.__cliente = cli

    @desc_serv4.setter
    def desc_serv4(self, desc):
        self.__desc_serv4 = desc

    @desc_serv1.setter
    def desc_serv1(self, desc):
        self.__desc_serv1 = desc

    @desc_serv2.setter
    def desc_serv2(self, desc):
        self.__desc_serv2 = desc

    @desc_serv3.setter
    def desc_serv3(self, desc):
        self.__desc_serv3 = desc

    @desc_serv5.setter
    def desc_serv5(self, desc):
        self.__desc_serv5 = desc

    @desc_serv6.setter
    def desc_serv6(self, desc):
        self.__desc_serv6 = desc

    @obs1.setter
    def obs1(self, obs):
        self.__obs1 = obs

    @obs2.setter
    def obs2(self, obs):
        self.__obs2 = obs

    @obs3.setter
    def obs3(self, obs):
        self.__obs3 = obs

    @qtd1.setter
    def qtd1(self, qtd):
        self.__qtd1 = qtd

    @qtd2.setter
    def qtd2(self, qtd):
        self.__qtd2 = qtd

    @qtd3.setter
    def qtd3(self, qtd):
        self.__qtd3 = qtd

    @qtd4.setter
    def qtd4(self, qtd):
        self.__qtd4 = qtd

    @qtd5.setter
    def qtd5(self, qtd):
        self.__qtd5 = qtd

    @qtd6.setter
    def qtd6(self, qtd):
        self.__qtd6 = qtd

    @valor_uni1.setter
    def valor_uni1(self, valor):
        self.__valor_uni1 = valor

    @valor_uni2.setter
    def valor_uni2(self, valor):
        self.__valor_uni2 = valor

    @valor_uni3.setter
    def valor_uni3(self, valor):
        self.__valor_uni3 = valor

    @valor_uni4.setter
    def valor_uni4(self, valor):
        self.__valor_uni4 = valor

    @valor_uni5.setter
    def valor_uni5(self, valor):
        self.__valor_uni5 = valor

    @valor_uni6.setter
    def valor_uni6(self, valor):
        self.__valor_uni6 = valor

    @valorTotal.setter
    def valorTotal(self, valor):
        self.__valor_total = valor

    @alugPago.setter
    def alugPago(self, valor):
        self.__alug_pago = valor

    @desconto.setter
    def desconto(self, valor):
        self.__desconto = valor



