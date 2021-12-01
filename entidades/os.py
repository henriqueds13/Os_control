class Os():
    def __init__(self, equipamento, marca, modelo='', acessorios='', defeito='', estado_aparelho='',
                 n_serie='', tensao=None, status='EM SERVIÇO', chassi='', andamento='', data_entrada=None,
                 hora_entrada=None, dias='', data_orc=None, conclusao=None, operador='', log='', codigo1='', codigo2='',
                 codigo3='', codigo4='', codigo5='', codigo6='', codigo7='', codigo8='', codigo9='',
                 desc_serv1='', desc_serv2='', desc_serv3='',
                 desc_serv4='',
                 desc_serv5='', desc_serv6='', desc_serv7='', desc_serv8='', desc_serv9='', desconto=None, obs1='',
                 obs2='', obs3='',valor_mao_obra=0, qtd1=0, qtd2=0,
                 qtd3=0,
                 qtd4=0, qtd5=0, qtd6=0, qtd7=0, qtd8=0, qtd9=0, valor_uni1=0, valor_uni2=0, valor_uni3=0, valor_uni4=0,
                 valor_uni5=0,
                 valor_uni6=0, valor_uni7=0, valor_uni8=0, valor_uni9=0, valor_total1=0, valor_total2=0, valor_total3=0,
                 valor_total4=0, valor_total5=0, valor_total6=0, valor_total7=0, valor_total8=0, valor_total9=0,
                 caixa_peca1=0, caixa_peca2=0, caixa_peca3=0, caixa_peca4=0, caixa_peca5=0, caixa_peca6=0,
                 caixa_peca7=0, caixa_peca8=0, caixa_peca9=0, caixa_peca_total=0, tecnico='', total=0, defeitos='',
                 cheque=0, ccredito=0, cdebito=0, pix=0, dinheiro=0, outros=0, obs_pagamento1='', obs_pagamento2='',
                 obs_pagamento3='', data_garantia=None):

        self.__total = total
        self.__defeitos = defeitos
        self.__cheque = cheque
        self.__ccredito = ccredito
        self.__cdebito = cdebito
        self.__pix = pix
        self.__dinheiro = dinheiro
        self.__outros = outros
        self.__obs_pagamento1 = obs_pagamento1
        self.__obs_pagamento2 = obs_pagamento2
        self.__obs_pagamento3 = obs_pagamento3
        self.__data_garantia = data_garantia
        self.__caixa_peca1 = caixa_peca1
        self.__caixa_peca2 = caixa_peca2
        self.__caixa_peca3 = caixa_peca3
        self.__caixa_peca4 = caixa_peca4
        self.__caixa_peca5 = caixa_peca5
        self.__caixa_peca6 = caixa_peca6
        self.__caixa_peca7 = caixa_peca7
        self.__caixa_peca8 = caixa_peca8
        self.__caixa_peca9 = caixa_peca9
        self.__caixa_peca_total = caixa_peca_total
        self.__valor_total1 = valor_total1
        self.__valor_total2 = valor_total2
        self.__valor_total3 = valor_total3
        self.__valor_total4 = valor_total4
        self.__valor_total5 = valor_total5
        self.__valor_total6 = valor_total6
        self.__valor_total7 = valor_total7
        self.__valor_total8 = valor_total8
        self.__valor_total9 = valor_total9
        self.__chassi = chassi
        self.__andamento = andamento
        self.__data_entrada = data_entrada
        self.__hora_entrada = hora_entrada
        self.__dias = dias
        self.__data_orc = data_orc
        self.__conclusao = conclusao
        self.__operador = operador
        self.__log = log
        self.__codigo1 = codigo1
        self.__codigo2 = codigo2
        self.__codigo3 = codigo3
        self.__codigo4 = codigo4
        self.__codigo5 = codigo5
        self.__codigo6 = codigo6
        self.__codigo7 = codigo7
        self.__codigo8 = codigo8
        self.__codigo9 = codigo9
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
        self.__desc_serv7 = desc_serv7
        self.__desc_serv8 = desc_serv8
        self.__desc_serv9 = desc_serv9
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
        self.__qtd7 = qtd7
        self.__qtd8 = qtd8
        self.__qtd9 = qtd9
        self.__valor_uni1 = valor_uni1
        self.__valor_uni2 = valor_uni2
        self.__valor_uni3 = valor_uni3
        self.__valor_uni4 = valor_uni4
        self.__valor_uni5 = valor_uni5
        self.__valor_uni6 = valor_uni6
        self.__valor_uni7 = valor_uni7
        self.__valor_uni8 = valor_uni8
        self.__valor_uni9 = valor_uni9
        self.__tecnico = tecnico

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
    def desc_serv7(self):
        return self.__desc_serv7

    @property
    def desc_serv8(self):
        return self.__desc_serv8

    @property
    def desc_serv9(self):
        return self.__desc_serv9

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
    def qtd7(self):
        return self.__qtd7

    @property
    def qtd8(self):
        return self.__qtd8

    @property
    def qtd9(self):
        return self.__qtd9

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

    @property
    def valor_uni7(self):
        return self.__valor_uni7

    @property
    def valor_uni8(self):
        return self.__valor_uni8

    @property
    def valor_uni9(self):
        return self.__valor_uni9

    @property
    def tecnico(self):
        return self.__tecnico

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

    @tecnico.setter
    def tecnico(self, tecnico):
        self.__tecnico = tecnico