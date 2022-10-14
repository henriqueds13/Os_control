class Calevent():
    def __init__(self, data, descrição, conta):

        self.__data = data
        self.__descrição = descrição
        self.conta = conta

    @property
    def data(self):
        return self.__data

    @property
    def descrição(self):
        return self.__descrição

    @property
    def conta(self):
        return self.__conta


    @data.setter
    def data(self, dt):
        self.__data = dt

    @descrição.setter
    def descrição(self, descr):
        self.__descrição = descr

    @conta.setter
    def conta(self, cont):
        self.__conta = cont
