class Estoque():
    def __init__(self, revendedor, obs1, obs2, obs3, nota, frete, tipo_op, operador, total, produtos):
        self.__revendedor = revendedor
        self.__obs1 = obs1
        self.__obs2 = obs2
        self.__obs3 = obs3
        self.__nota = nota
        self.__frete = frete
        self.__tipo_op = tipo_op
        self.__operador = operador
        self.__total = total
        self.__produtos = produtos

    @property
    def revendedor(self):
        return self.__revendedor

    @property
    def obs1(self):
        return self.__obs1

    @property
    def obs2(self):
        return self.__obs2

    @property
    def obs3(self):
        return self.__obs1

    @property
    def nota(self):
        return self.__nota

    @property
    def frete(self):
        return self.__frete

    @property
    def tipoOp(self):
        return self.__tipo_op

    @property
    def operador(self):
        return self.__operador

    @property
    def total(self):
        return self.__total

    @property
    def produtos(self):
        return self.__produtos

    @revendedor.setter
    def revendedor(self, revend):
        self.__revendedor = revend

    @obs1.setter
    def obs1(self, obs):
        self.__obs1 = obs

    @obs2.setter
    def obs2(self, obs):
        self.__obs2 = obs

    @revendedor.setter
    def obs3(self, obs):
        self.obs3 = obs

    @nota.setter
    def nota(self, nota):
        self.__nota = nota

    @tipoOp.setter
    def tipoOp(self, tipoOp):
        self.__tipo_op = tipoOp

    @frete.setter
    def frete(self, frete):
        self.__frete = frete

    @operador.setter
    def operador(self, operador):
        self.__operador = operador

    @total.setter
    def total(self, total):
        self.__total = total

    @produtos.setter
    def produtos(self, produtos):
        self.__produtos = produtos