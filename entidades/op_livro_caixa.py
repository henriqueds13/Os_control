class OpLivroCaixa():
    def __init__(self, data, hora, tipo_op, historico, entrada, saida, entrada_cp, saida_cp, grupo,
                 cheque, ccredito, cdebito, pix, dinheiro, outros, operador, os, mes_caixa):
        self.__data = data
        self.__hora = hora
        self.__tipo_op = tipo_op
        self.__historico = historico
        self.__entrada = entrada
        self.__saida = saida
        self.__entrada_cp = entrada_cp
        self.__saida_cp = saida_cp
        self.__grupo = grupo
        self.__dinheiro = dinheiro
        self.__cheque = cheque
        self.__cdebito = cdebito
        self.__ccredito = ccredito
        self.__pix = pix
        self.__outros = outros
        self.__operador = operador
        self.__os = os
        self.__mes_caixa = mes_caixa

    @property
    def data(self):
        return self.__data

    @property
    def hora(self):
        return self.__hora

    @property
    def tipoOp(self):
        return self.__tipo_op

    @property
    def historico(self):
        return self.__historico

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
    def grupo(self):
        return self.__grupo


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
    def os(self):
        return self.__os


    @property
    def mesCaixa(self):
        return self.__mes_caixa

    @data.setter
    def data(self, dat):
        self.__data = dat

    @hora.setter
    def hora(self, hor):
        self.__hora = hor

    @tipoOp.setter
    def tipoOp(self, op):
        self.__tipo_op = op

    @historico.setter
    def historico(self, hist):
        self.__historico = hist

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

    @grupo.setter
    def grupo(self, grup):
        self.__grupo = grup


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

    @mesCaixa.setter
    def mesCaixa(self, vend):
        self.__mes_caixa = vend

    @os.setter
    def os(self, oss):
        self.__os = oss
