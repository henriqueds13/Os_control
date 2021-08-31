class Os():
    def __init__(self, equipamento, marca, modelo='', acessorios='', defeito='', estado_aparelho='',
                 n_serie='', tensao=None, status='EM SERVIÇO', desc_serv1='', desc_serv2='', desc_serv3='',
                 desc_serv4='',
                 desc_serv5='', desc_serv6='', desconto=None, obs1='', obs2='', obs3='',valor_mao_obra=0.00, qtd1=0, qtd2=0,
                 qtd3=0,
                 qtd4=0, qtd5=0, qtd6=0, valor_uni1=0, valor_uni2=0, valor_uni3=0, valor_uni4=0, valor_uni5=0,
                 valor_uni6=0):
        self.__equipamento = equipamento
        self.__marca = marca
        self.__modelo = modelo
        self.__acessorios = acessorios
        self.__defeito = defeito
        self.__estado_aparelho = estado_aparelho
        self.__n_serie = n_serie
        self.__tensao = tensao
        self.__status = status
        self.__desc_serv1 = desc_serv1
        self.__desc_serv2 = desc_serv2
        self.__desc_serv3 = desc_serv3
        self.__desc_serv4 = desc_serv4
        self.__desc_serv5 = desc_serv5
        self.__desc_serv6 = desc_serv6
        self.__desconto = desconto
        self.__obs1 = obs1
        self.__obs2 = obs2
        self.__obs3 = obs3
        self.__valor_mao_obra = valor_mao_obra
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

    @property
    def equipamento(self):
        return self.__equipamento

    @property
    def marca(self):
        return self.__marca

    @property
    def modelo(self):
        return self.__modelo

    @property
    def acessorios(self):
        return self.__acessorios

    @property
    def defeito(self):
        return self.__defeito

    @property
    def estado_aparelho(self):
        return self.__estado_aparelho

    @property
    def n_serie(self):
        return self.__n_serie

    @property
    def tensao(self):
        return self.__tensao

    @property
    def status(self):
        return self.__status

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
    def valor_mao_obra(self):
        return self.__valor_mao_obra

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

    @equipamento.setter
    def equipamento(self, equipamento):
        self.__equipamento = equipamento

    @marca.setter
    def marca(self, marca):
        self.__marca = marca

    @modelo.setter
    def modelo(self, modelo):
        self.__modelo = modelo

    @acessorios.setter
    def acessorios(self, acessorios):
        self.__acessorios = acessorios

    @defeito.setter
    def defeito(self, defeito):
        self.__defeito = defeito

    @estado_aparelho.setter
    def estado_aparelho(self, estado):
        self.__estado_aparelho = estado

    @n_serie.setter
    def n_serie(self, n_serie):
        self.__n_serie = n_serie

    @tensao.setter
    def tensao(self, tensao):
        self.__tensao = tensao

    @status.setter
    def status(self, status):
        self.__status = status

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

    @desconto.setter
    def desconto(self, desconto):
        self.__desconto = desconto

    @obs1.setter
    def obs1(self, obs):
        self.__obs1 = obs

    @obs2.setter
    def obs2(self, obs):
        self.__obs2 = obs

    @obs3.setter
    def obs3(self, obs):
        self.__obs3 = obs

    @valor_mao_obra.setter
    def valor_mao_obra(self, valor):
        self.__valor_mao_obra = valor

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
