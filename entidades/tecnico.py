class Tecnico():
    def __init__(self, nome, senha_tecnico, INI, EM, BX, CE, USU, CON, FIN):
        self.__nome = nome
        self.__senha_tecnico = senha_tecnico
        self.__INI = INI
        self.__EM = EM
        self.__BX = BX
        self.__CE = CE
        self.__USU = USU
        self.__CON = CON
        self.__FIN = FIN

    @property
    def nome(self):
        return self.__nome

    @property
    def senha_tecnico(self):
        return self.__senha_tecnico

    @property
    def INI(self):
        return self.__INI

    @property
    def EM(self):
        return self.__EM

    @property
    def BX(self):
        return self.__BX

    @property
    def CE(self):
        return self.__CE

    @property
    def USU(self):
        return self.__USU

    @property
    def CON(self):
        return self.__CON

    @property
    def FIN(self):
        return self.__FIN

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @senha_tecnico.setter
    def senha_tecnico(self, senha):
        self.__senha_tecnico = senha

    @INI.setter
    def INI(self, sigla):
        self.__INI = sigla

    @EM.setter
    def EM(self, sigla):
        self.__EM = sigla

    @BX.setter
    def BX(self, sigla):
        self.__BX = sigla

    @CE.setter
    def CE(self, sigla):
        self.__CE = sigla

    @USU.setter
    def USU(self, sigla):
        self.__USU = sigla

    @CON.setter
    def CON(self, sigla):
        self.__CON = sigla

    @FIN.setter
    def FIN(self, sigla):
        self.__FIN = sigla