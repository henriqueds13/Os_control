class LivroCaixa():
    def __init__(self, data_abertura, data_fechamento, saldo_cn, saldo_cp, cheque, ccredito, cdebito, pix, dinheiro,
                 outros, operador, entrada, saida, entrada_cp, saida_cp, mes_caixa, quant_dinheiro, quant_cheque,
                 quant_cdebito, quant_ccredito, quant_pix, quant_outros):
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
        self.__entrada = entrada
        self.__saida = saida
        self.__entrada_cp = entrada_cp
        self.__saida_cp = saida_cp
        self.__mes_caixa = mes_caixa
        self.__quant_dinheiro = quant_dinheiro
        self.__quant_cheque = quant_cheque
        self.__quant_cdebito = quant_cdebito
        self.__quant_ccredito = quant_ccredito
        self.__quant_pix = quant_pix
        self.__quant_outros = quant_outros

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

    @property
    def mesCaixa(self):
        return self.__mes_caixa

    @property
    def quantDinheiro(self):
        return self.__quant_dinheiro

    @property
    def quantCheque(self):
        return self.__quant_cheque

    @property
    def quantCDebito(self):
        return self.__quant_cdebito

    @property
    def quantCCredito(self):
        return self.__quant_ccredito

    @property
    def quantPix(self):
        return self.__quant_pix

    @property
    def quantOutros(self):
        return self.__quant_outros

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

    @mesCaixa.setter
    def mesCaixa(self, saida):
        self.__mes_caixa = saida

    @quantDinheiro.setter
    def quantDinheiro(self, saida):
        self.__quant_dinheiro = saida

    @quantCheque.setter
    def quantCheque(self, saida):
        self.__quant_cheque = saida

    @quantCDebito.setter
    def quantCDebito(self, saida):
        self.__quant_cdebito = saida

    @quantCCredito.setter
    def quantCCredito(self, saida):
        self.__quant_ccredito = saida

    @quantPix.setter
    def quantPix(self, saida):
        self.__quant_pix = saida

    @quantOutros.setter
    def quantOutros(self, saida):
        self.__quant_outros = saida