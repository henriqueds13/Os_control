class Cliente():
    def __init__(self, nome, operador, celular='', cpf_cnpj='', tel_fixo='', rg_ie='', logradouro='', uf='SP', bairro='', complemento='',
                 cep=0000, cidade='', email='', whats='', contato='', indicacao=''):
        self.__nome = nome
        self.__operador = operador
        self.__celular = celular
        self.__cpf_cnpj = cpf_cnpj
        self.__tel_fixo = tel_fixo
        self.__rg_ie = rg_ie
        self.__logradouro = logradouro
        self.__uf = uf
        self.__bairro = bairro
        self.__complemento = complemento
        self.__cep = cep
        self.__cidade = cidade
        self.__email = email
        self.__whats = whats
        self.__contato = contato
        self.__indicacao = indicacao

    @property
    def nome(self):
        return self.__nome

    @property
    def operador(self):
        return self.__operador

    @property
    def celular(self):
        return self.__celular

    @property
    def cpf_cnpj(self):
        return self.__cpf_cnpj

    @property
    def tel_fixo(self):
        return self.__tel_fixo

    @property
    def rg_ie(self):
        return self.__rg_ie

    @property
    def logradouro(self):
        return self.__logradouro

    @property
    def uf(self):
        return self.__uf

    @property
    def bairro(self):
        return self.__bairro

    @property
    def complemento(self):
        return self.__complemento

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
    def contato(self):
        return self.__contato

    @property
    def indicacao(self):
        return self.__indicacao

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @operador.setter
    def operador(self, operador):
        self.__operador = operador

    @celular.setter
    def celular(self, celular):
        self.__celular = celular

    @cpf_cnpj.setter
    def cpf_cnpj(self, cpf_cnpj):
        self.__cpf_cnpj = cpf_cnpj

    @tel_fixo.setter
    def tel_fixo(self, tel_fixo):
        self.__tel_fixo = tel_fixo

    @rg_ie.setter
    def rg_ie(self, rg_ie):
        self.__rg_ie = rg_ie

    @logradouro.setter
    def logradouro(self, logradouro):
        self.__logradouro = logradouro

    @uf.setter
    def uf(self, uf):
        self.__uf = uf

    @bairro.setter
    def bairro(self, bairro):
        self.__bairro = bairro

    @complemento.setter
    def complemento(self, complemento):
        self.__complemento = complemento

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

    @contato.setter
    def contato(self, contato):
        self.__contato = contato

    @indicacao.setter
    def indicacao(self, indicacao):
        self.__indicacao = indicacao


