class MaquinaAluguel():
    def __init__(self, equipamento, marca, modelo, num_serie, valor, status, obs):

        self.__equipamento = equipamento
        self.__marca = marca
        self.__modelo = modelo
        self.__num_serie = num_serie
        self.__valor = valor
        self.__status = status
        self.__obs = obs

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
    def numSerie(self):
        return self.__num_serie

    @property
    def valor(self):
        return self.__valor

    @property
    def status(self):
        return self.__status

    @property
    def obs(self):
        return self.__obs

    @equipamento.setter
    def equipamento(self, equip):
        self.__equipamento = equip

    @marca.setter
    def marca(self, marc):
        self.__marca = marc

    @modelo.setter
    def modelo(self, marc):
        self.__modelo = marc

    @numSerie.setter
    def numSerie(self, num):
        self.__num_serie = num

    @valor.setter
    def valor(self, val):
        self.__valor = val

    @status.setter
    def status(self, stat):
        self.__status = stat

    @obs.setter
    def obs(self, ob):
        self.__obs = ob

