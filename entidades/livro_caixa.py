class LivroCaixa():
    def __init__(self, data_abertura, data_fechamento, saldo_cn, saldo_cp, cheque, ccredito, cdebito, pix, dinheiro,
                 outros, operador, mes, ano, entrada, saida, entrada_cp, saida_cp):
        self.__data_abertura = data_abertura
        self.__data_fechamento = data_fechamento
        self.__saldo_cn = saldo_cn
        self.__saldo_cp = saldo_cp
        self.__dinheiro = dinheiro
        self.__cheque = cheque
        self.__cdebito = cdebito
        self.__ccredito = ccredito
        self.__pix = pix
        self.__outros = outros
        self.__operador = operador
        self.__mes = mes
        self.__ano = ano
        self.__entrada = entrada
        self.__saida = saida
        self.__entrada_cp = entrada_cp
        self.__saida_cp = saida_cp

    @property
    def dataAbertura(self):
        return self.__data_abertura

    @property
    def dataFechamento(self):
        return self.__data_fechamento

    @property
    def saldoCn(self):
        return self.__saldo_cn

    @property
    def saldoCp(self):
        return self.__saldo_cp

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
    def operador(self):
        return self.__operador

    @property
    def mes(self):
        return self.__mes

    @property
    def ano(self):
        return self.__ano

    @property
    def entrada(self):
        return self.__entrada

    @property
    def saida(self):
        return self.__saida

    @property
    def entradaCp(self):
        return self.__entrada_cp

    @property
    def saidaCp(self):
        return self.__saida_cp

    @dataAbertura.setter
    def dataAbertura(self, data):
        self.__data_abertura = data

    @dataFechamento.setter
    def dataFechamento(self, data):
        self.__data_fechamento = data

    @saldoCn.setter
    def saldoCn(self, saldo):
        self.__saldo_cn = saldo

    @saldoCp.setter
    def saldoCp(self, saldo):
        self.__saldo_cp = saldo

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

    @operador.setter
    def operador(self, op):
        self.__operador = op

    @mes.setter
    def mes(self, pag):
        self.__mes = pag

    @ano.setter
    def ano(self, op):
        self.__ano = op

    @entrada.setter
    def entrada(self, entr):
        self.__historico = entr

    @saida.setter
    def saida(self, said):
        self.__saida = said

    @entradaCp.setter
    def entradaCp(self, entrada):
        self.__entrada_cp = entrada

    @saidaCp.setter
    def saidaCp(self, saida):
        self.__saida_cp = saida