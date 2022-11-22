class AcessoriosMaquinaAluguel():
    def __init__(self, acessorio, valor):
        self.__acessorio = acessorio
        self.__valor = valor

    @property
    def acessorio(self):
        return self.__acessorio

    @property
    def valor(self):
        return self.__valor

    @acessorio.setter
    def acessorio(self, equip):
        self.__acessorio = equip

    @valor.setter
    def valor(self, marc):
        self.__valor = marc
