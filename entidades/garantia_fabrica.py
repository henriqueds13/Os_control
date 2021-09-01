class GarantiaFabrica():
    def __int__(self, n_nota=0, tempo_garantia=0, data_compra=None, garantia_compl=0):
        self.__n_nota = n_nota
        self.__tempo_garantia = tempo_garantia
        self.__data_compra = data_compra
        self.__garantia_compl = garantia_compl

    @property
    def n_nota(self):
        return self.__n_nota

    @property
    def tempo_garantia(self):
        return self.__tempo_garantia

    @property
    def data_compra(self):
        return self.__data_compra

    @property
    def garantia_compl(self):
        return self.__garantia_compl

    @n_nota.setter
    def n_nota(self, num):
        self.__n_nota = num

    @tempo_garantia.setter
    def tempo_garantia(self, temp):
        self.__tempo_garantia = temp

    @data_compra.setter
    def data_compra(self, data):
        self.__data_compra = data

    @garantia_compl.setter
    def garantia_compl(self, garantia):
        self.__garantia_compl = garantia
    