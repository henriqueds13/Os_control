class Empresa():
    def __init__(self, nome, nome_fantasia, sigla, celular, cnpj, tel_fixo, ie, im, logradouro, uf, cep, cidade, email,
                 whats, tel_comercial, complemento1, complemento2, complemento3, autorizada1, autorizada2, autorizada3,
                 autorizada4, autorizada5, autorizada6, autorizada7, autorizada8, autorizada9, autorizada10,
                 autorizada11, autorizada12):

        self.__nome = nome
        self.__nome_fantasia = nome_fantasia
        self.__sigla = sigla
        self.__celular = celular
        self.__cnpj = cnpj
        self.__tel_fixo = tel_fixo
        self.__ie = ie
        self.__logradouro = logradouro
        self.__uf = uf
        self.__im = im
        self.__tel_comercial = tel_comercial
        self.__cep = cep
        self.__cidade = cidade
        self.__email = email
        self.__whats = whats
        self.__complemento1 = complemento1
        self.__complemento2 = complemento2
        self.__complemento3 = complemento3
        self.__autorizada1 = autorizada1
        self.__autorizada2 = autorizada2
        self.__autorizada3 = autorizada3
        self.__autorizada4 = autorizada4
        self.__autorizada5 = autorizada5
        self.__autorizada6 = autorizada6
        self.__autorizada7 = autorizada7
        self.__autorizada8 = autorizada8
        self.__autorizada9 = autorizada9
        self.__autorizada10 = autorizada10
        self.__autorizada11 = autorizada11
        self.__autorizada12 = autorizada12

    @property
    def nome(self):
        return self.__nome

    @property
    def celular(self):
        return self.__celular

    @property
    def cnpj(self):
        return self.__cnpj

    @property
    def tel_fixo(self):
        return self.__tel_fixo

    @property
    def ie(self):
        return self.__ie

    @property
    def logradouro(self):
        return self.__logradouro

    @property
    def uf(self):
        return self.__uf

    @property
    def sigla(self):
        return self.__sigla

    @property
    def complemento1(self):
        return self.__complemento1

    @property
    def cep(self):
        return self.__cep

    @property
    def cidade(self):
        return self.__cidade

    @property
    def email(self):
        return self.__email

    @property
    def whats(self):
        return self.__whats

    @property
    def im(self):
        return self.__im

    @property
    def tel_comercial(self):
        return self.__tel_comercial

    @property
    def nome_fantasia(self):
        return self.__nome_fantasia

    @property
    def complemento2(self):
        return self.__complemento2

    @property
    def complemento3(self):
        return self.__complemento3

    @property
    def autorizada1(self):
        return self.__autorizada1

    @property
    def autorizada2(self):
        return self.__autorizada2

    @property
    def autorizada3(self):
        return self.__autorizada3

    @property
    def autorizada4(self):
        return self.__autorizada4

    @property
    def autorizada5(self):
        return self.__autorizada5

    @property
    def autorizada6(self):
        return self.__autorizada6

    @property
    def autorizada7(self):
        return self.__autorizada7

    @property
    def autorizada8(self):
        return self.__autorizada8

    @property
    def autorizada9(self):
        return self.__autorizada9

    @property
    def autorizada10(self):
        return self.__autorizada10

    @property
    def autorizada11(self):
        return self.__autorizada11

    @property
    def autorizada12(self):
        return self.__autorizada12

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @tel_comercial.setter
    def tel_comercial(self, tel_comercial):
        self.__tel_comercial = tel_comercial

    @nome_fantasia.setter
    def nome_fantasia(self, operador):
        self.__nome_fatasia = operador

    @celular.setter
    def celular(self, celular):
        self.__celular = celular

    @cnpj.setter
    def cnpj(self, cpf_cnpj):
        self.__cnpj = cpf_cnpj

    @tel_fixo.setter
    def tel_fixo(self, tel_fixo):
        self.__tel_fixo = tel_fixo

    @ie.setter
    def ie(self, ie):
        self.__ie = ie

    @logradouro.setter
    def logradouro(self, logradouro):
        self.__logradouro = logradouro

    @uf.setter
    def uf(self, uf):
        self.__uf = uf

    @sigla.setter
    def sigla(self, uf):
        self.__sigla = uf

    @im.setter
    def im(self, bairro):
        self.__im = bairro

    @complemento1.setter
    def complemento1(self, complemento):
        self.__complemento1 = complemento

    @complemento2.setter
    def complemento2(self, complemento):
        self.__complemento2 = complemento

    @complemento3.setter
    def complemento3(self, complemento):
        self.__complemento3 = complemento

    @cep.setter
    def cep(self, cep):
        self.__cep = cep

    @cidade.setter
    def cidade(self, cidade):
        self.__cidade = cidade

    @email.setter
    def email(self, email):
        self.__email = email

    @whats.setter
    def whats(self, whats):
        self.__whats = whats

    @autorizada1.setter
    def autorizada1(self, indicacao):
        self.__autorizada1 = indicacao

    @autorizada2.setter
    def autorizada2(self, indicacao):
        self.__autorizada2 = indicacao

    @autorizada3.setter
    def autorizada3(self, indicacao):
        self.__autorizada3 = indicacao

    @autorizada4.setter
    def autorizada4(self, indicacao):
        self.__autorizada4 = indicacao

    @autorizada5.setter
    def autorizada5(self, indicacao):
        self.__autorizada5 = indicacao

    @autorizada6.setter
    def autorizada6(self, indicacao):
        self.__autorizada6 = indicacao

    @autorizada7.setter
    def autorizada7(self, indicacao):
        self.__autorizada7 = indicacao

    @autorizada8.setter
    def autorizada8(self, indicacao):
        self.__autorizada8 = indicacao

    @autorizada9.setter
    def autorizada9(self, indicacao):
        self.__autorizada9 = indicacao

    @autorizada10.setter
    def autorizada10(self, indicacao):
        self.__autorizada10 = indicacao

    @autorizada11.setter
    def autorizada11(self, indicacao):
        self.__autorizada11 = indicacao

    @autorizada12.setter
    def autorizada12(self, indicacao):
        self.__autorizada12 = indicacao