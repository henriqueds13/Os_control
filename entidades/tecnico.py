class Tecnico():
    def __init__(self, nome, senha_tecnico):
        self.__nome = nome
        self.__senha_tecnico = senha_tecnico


    @property
    def nome(self):
        return self.__nome

    @property
    def senha_tecnico(self):
        return self.__senha_tecnico

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @senha_tecnico.setter
    def senha_tecnico(self, senha):
        self.__senha_tecnico = senha